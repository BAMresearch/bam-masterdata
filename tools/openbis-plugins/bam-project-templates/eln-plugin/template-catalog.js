(function (root, factory) {
  "use strict";
  var moduleValue = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = moduleValue;
  } else {
    root.BamTemplateCatalog = moduleValue;
  }
}(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  var LIMITS = Object.freeze({
    catalogBytes: 1024 * 1024,
    templates: 100,
    collections: 100,
    objects: 500,
    properties: 100,
    code: 128,
    title: 255,
    description: 10000,
    templateText: 10000,
    resolvedProperty: 10000
  });

  var CODE_PATTERN = /^[A-Z0-9][A-Z0-9._-]*$/;
  var PROPERTY_CODE_PATTERN = /^\$?[A-Z0-9][A-Z0-9._-]*$/;
  var CONTROL_CHARACTER_PATTERN = /[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/;
  var PLACEHOLDER_PATTERN = /\{\{[^{}]+\}\}/g;
  var DANGEROUS_KEYS = Object.freeze({
    "__proto__": true,
    "constructor": true,
    "prototype": true
  });

  // This policy is executable code, not template data. Expanding it therefore
  // requires a reviewed release instead of an uploaded JSON file.
  var POLICY = Object.freeze({
    collectionTypes: Object.freeze({ "COLLECTION": true }),
    objectTypes: Object.freeze({
      "DOCUMENT": true,
      "MEASUREMENT": true
    }),
    propertyCodes: Object.freeze({
      "$NAME": true,
      "$DEFAULT_OBJECT_TYPE": true,
      "DESCRIPTION": true,
      "DOCUMENT_TYPE": true,
      "NOTES": true
    }),
    placeholders: Object.freeze({
      "{{PROJECT_CODE}}": true,
      "{{PROJECT_TITLE}}": true,
      "{{PROJECT_DESCRIPTION}}": true,
      "{{PROJECT_DESCRIPTION_OR_TITLE}}": true
    })
  });

  function CatalogError(message) {
    this.name = "CatalogError";
    this.message = message;
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, CatalogError);
    }
  }
  CatalogError.prototype = Object.create(Error.prototype);
  CatalogError.prototype.constructor = CatalogError;

  function fail(message) {
    throw new CatalogError(message);
  }

  function isPlainObject(value) {
    if (value === null || typeof value !== "object" || Array.isArray(value)) {
      return false;
    }
    var prototype = Object.getPrototypeOf(value);
    return prototype === Object.prototype || prototype === null;
  }

  function ownKeys(value) {
    return Object.keys(value);
  }

  function assertAllowedKeys(value, allowed, label) {
    ownKeys(value).forEach(function (key) {
      if (DANGEROUS_KEYS[key] || !allowed[key]) {
        fail(label + " enthält ein nicht erlaubtes Feld: " + key);
      }
    });
  }

  function text(value, label, maximum, required) {
    if (typeof value !== "string") {
      fail(label + " muss Text sein.");
    }
    var normalized = value.trim();
    if (required && normalized.length === 0) {
      fail(label + " darf nicht leer sein.");
    }
    if (normalized.length > maximum) {
      fail(label + " ist zu lang.");
    }
    if (CONTROL_CHARACTER_PATTERN.test(normalized)) {
      fail(label + " enthält Steuerzeichen.");
    }
    return normalized;
  }

  function optionalText(value, label, maximum) {
    if (value === undefined || value === null) {
      return "";
    }
    return text(value, label, maximum, false);
  }

  function code(value, label) {
    var normalized = text(value, label, LIMITS.code, true).toUpperCase();
    if (!CODE_PATTERN.test(normalized)) {
      fail(label + " enthält nicht erlaubte Zeichen.");
    }
    return normalized;
  }

  function validateProperties(value, owner) {
    if (!isPlainObject(value)) {
      fail(owner + ": properties muss ein JSON-Objekt sein.");
    }
    var keys = ownKeys(value);
    if (keys.length > LIMITS.properties) {
      fail(owner + " definiert zu viele Properties.");
    }
    var result = Object.create(null);
    keys.forEach(function (rawPropertyCode) {
      if (DANGEROUS_KEYS[rawPropertyCode]) {
        fail(owner + " enthält einen gefährlichen Property-Schlüssel.");
      }
      var propertyCode = text(
        rawPropertyCode, owner + " Property-Code", LIMITS.code, true
      ).toUpperCase();
      if (!PROPERTY_CODE_PATTERN.test(propertyCode) || !POLICY.propertyCodes[propertyCode]) {
        fail(owner + " enthält einen nicht freigegebenen Property-Code: " + propertyCode);
      }
      var rawValue = text(
        value[rawPropertyCode], owner + " Property-Wert", LIMITS.templateText, false
      );
      var placeholders = rawValue.match(PLACEHOLDER_PATTERN) || [];
      placeholders.forEach(function (placeholder) {
        if (!POLICY.placeholders[placeholder]) {
          fail(owner + " enthält einen nicht freigegebenen Platzhalter: " + placeholder);
        }
      });
      var remainder = rawValue;
      Object.keys(POLICY.placeholders).forEach(function (placeholder) {
        remainder = remainder.split(placeholder).join("");
      });
      if (remainder.indexOf("{{") !== -1 || remainder.indexOf("}}") !== -1) {
        fail(owner + " enthält einen fehlerhaften Platzhalter.");
      }
      result[propertyCode] = rawValue;
    });
    return result;
  }

  function validateCollection(value, seenCodes) {
    if (!isPlainObject(value)) {
      fail("Jede Collection muss ein JSON-Objekt sein.");
    }
    assertAllowedKeys(value, {
      code: true, type: true, properties: true
    }, "Collection");
    var collectionCode = code(value.code, "Collection-Code");
    if (seenCodes[collectionCode]) {
      fail("Doppelter Collection-Code: " + collectionCode);
    }
    seenCodes[collectionCode] = true;
    var typeCode = code(value.type || "COLLECTION", "Collection-Typ");
    if (!POLICY.collectionTypes[typeCode]) {
      fail("Nicht freigegebener Collection-Typ: " + typeCode);
    }
    return {
      code: collectionCode,
      type: typeCode,
      properties: validateProperties(value.properties || {}, "Collection " + collectionCode)
    };
  }

  function validateObject(value, seenCodes, collectionCodes) {
    if (!isPlainObject(value)) {
      fail("Jedes Object muss ein JSON-Objekt sein.");
    }
    assertAllowedKeys(value, {
      code: true, type: true, collection: true, properties: true
    }, "Object");
    var objectCode = code(value.code, "Object-Code");
    if (seenCodes[objectCode]) {
      fail("Doppelter Object-Code: " + objectCode);
    }
    seenCodes[objectCode] = true;
    var typeCode = code(value.type, "Object-Typ");
    if (!POLICY.objectTypes[typeCode]) {
      fail("Nicht freigegebener Object-Typ: " + typeCode);
    }
    var collectionCode = value.collection === undefined ? "" :
      code(value.collection, "Collection-Verweis");
    if (collectionCode && !collectionCodes[collectionCode]) {
      fail("Object " + objectCode + " verweist auf eine unbekannte Collection.");
    }
    return {
      code: objectCode,
      type: typeCode,
      collection: collectionCode,
      properties: validateProperties(value.properties || {}, "Object " + objectCode)
    };
  }

  function validateTemplate(value, templateCodes) {
    if (!isPlainObject(value)) {
      fail("Jedes Template muss ein JSON-Objekt sein.");
    }
    assertAllowedKeys(value, {
      code: true,
      label: true,
      description: true,
      discipline: true,
      version: true,
      status: true,
      collections: true,
      objects: true
    }, "Template");
    var templateCode = code(value.code, "Template-Code");
    if (templateCodes[templateCode]) {
      fail("Doppelter Template-Code: " + templateCode);
    }
    templateCodes[templateCode] = true;
    var status = text(value.status, "Template-Status", 20, true).toLowerCase();
    if (status !== "released") {
      fail("Nur freigegebene Templates dürfen ausgeliefert werden: " + templateCode);
    }
    if (!Array.isArray(value.collections) || value.collections.length > LIMITS.collections) {
      fail("Template " + templateCode + " enthält ungültige oder zu viele Collections.");
    }
    if (!Array.isArray(value.objects) || value.objects.length > LIMITS.objects) {
      fail("Template " + templateCode + " enthält ungültige oder zu viele Objects.");
    }
    var collectionCodes = Object.create(null);
    var objectCodes = Object.create(null);
    var collections = value.collections.map(function (item) {
      return validateCollection(item, collectionCodes);
    });
    var objects = value.objects.map(function (item) {
      return validateObject(item, objectCodes, collectionCodes);
    });
    return {
      code: templateCode,
      label: text(value.label, "Template-Name", LIMITS.title, true),
      description: text(
        value.description, "Template-Beschreibung", LIMITS.description, true
      ),
      discipline: optionalText(value.discipline, "Fachbereich", LIMITS.title),
      version: text(value.version, "Template-Version", 40, true),
      status: status,
      collections: collections,
      objects: objects
    };
  }

  function deepFreeze(value) {
    if (value && typeof value === "object" && !Object.isFrozen(value)) {
      Object.freeze(value);
      ownKeys(value).forEach(function (key) { deepFreeze(value[key]); });
    }
    return value;
  }

  function resolveProperties(properties, variables) {
    var result = Object.create(null);
    ownKeys(properties).forEach(function (propertyCode) {
      var resolved = properties[propertyCode]
        .split("{{PROJECT_CODE}}").join(variables.projectCode)
        .split("{{PROJECT_TITLE}}").join(variables.projectTitle)
        .split("{{PROJECT_DESCRIPTION}}").join(variables.projectDescription)
        .split("{{PROJECT_DESCRIPTION_OR_TITLE}}").join(
          variables.projectDescription || variables.projectTitle
        );
      if (resolved.length > LIMITS.resolvedProperty) {
        fail("Ein aufgelöster Property-Wert ist zu lang.");
      }
      if (resolved) {
        result[propertyCode] = resolved;
      }
    });
    return result;
  }

  function create(document) {
    if (!isPlainObject(document)) {
      fail("Der Template-Katalog muss ein JSON-Objekt sein.");
    }
    assertAllowedKeys(document, {
      schemaVersion: true, defaultTemplate: true, templates: true
    }, "Template-Katalog");
    if (document.schemaVersion !== 1) {
      fail("Nicht unterstützte Katalogversion.");
    }
    if (!Array.isArray(document.templates) || document.templates.length === 0 ||
        document.templates.length > LIMITS.templates) {
      fail("Der Template-Katalog enthält keine oder zu viele Templates.");
    }
    var templateCodes = Object.create(null);
    var templates = document.templates.map(function (item) {
      return validateTemplate(item, templateCodes);
    });
    var defaultTemplate = document.defaultTemplate === null ||
      document.defaultTemplate === undefined ? "" :
      code(document.defaultTemplate, "Standard-Template");
    if (defaultTemplate && !templateCodes[defaultTemplate]) {
      fail("Das konfigurierte Standard-Template existiert nicht.");
    }
    var templatesByCode = Object.create(null);
    templates.forEach(function (template) {
      templatesByCode[template.code] = template;
    });
    deepFreeze(templates);

    return Object.freeze({
      listTemplates: function () {
        return templates.slice();
      },
      getDefaultTemplateCode: function () {
        return defaultTemplate;
      },
      buildPlan: function (input) {
        if (!isPlainObject(input)) {
          fail("Projektdaten müssen als Objekt übergeben werden.");
        }
        assertAllowedKeys(input, {
          spaceCode: true,
          projectCode: true,
          projectTitle: true,
          projectDescription: true,
          templateCode: true
        }, "Projektdaten");
        var variables = {
          spaceCode: code(input.spaceCode, "Space-Code"),
          projectCode: code(input.projectCode, "Projekt-Code"),
          projectTitle: text(input.projectTitle, "Projekttitel", LIMITS.title, true),
          projectDescription: optionalText(
            input.projectDescription, "Projektbeschreibung", LIMITS.description
          )
        };
        var selectedCode = optionalText(
          input.templateCode, "Template-Code", LIMITS.code
        ).toUpperCase();
        if (selectedCode && !CODE_PATTERN.test(selectedCode)) {
          fail("Template-Code enthält nicht erlaubte Zeichen.");
        }
        var template = selectedCode ? templatesByCode[selectedCode] : null;
        if (selectedCode && !template) {
          fail("Unbekanntes oder nicht freigegebenes Template: " + selectedCode);
        }
        var projectKey = "project";
        var collections = template ? template.collections.map(function (item) {
          return {
            creationKey: "collection:" + item.code,
            projectCreationKey: projectKey,
            code: item.code,
            type: item.type,
            properties: resolveProperties(item.properties, variables)
          };
        }) : [];
        var objects = template ? template.objects.map(function (item) {
          return {
            creationKey: "object:" + item.code,
            projectCreationKey: projectKey,
            collectionCreationKey: item.collection ? "collection:" + item.collection : "",
            code: item.code,
            type: item.type,
            spaceCode: variables.spaceCode,
            properties: resolveProperties(item.properties, variables)
          };
        }) : [];
        return deepFreeze({
          templateCode: selectedCode,
          project: {
            creationKey: projectKey,
            spaceCode: variables.spaceCode,
            code: variables.projectCode,
            title: variables.projectTitle,
            description: variables.projectDescription
          },
          collections: collections,
          objects: objects
        });
      }
    });
  }

  return Object.freeze({
    create: create,
    CatalogError: CatalogError,
    limits: LIMITS
  });
}));
