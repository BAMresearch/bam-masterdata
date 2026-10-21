(function (root, factory) {
  "use strict";
  var moduleValue = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = moduleValue;
  } else {
    root.BamOpenbisAdapter = moduleValue;
  }
}(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  function AdapterError(code, message, cause) {
    this.name = "AdapterError";
    this.code = code;
    this.message = message;
    this.cause = cause || null;
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, AdapterError);
    }
  }
  AdapterError.prototype = Object.create(Error.prototype);
  AdapterError.prototype.constructor = AdapterError;

  function requireFunction(value, name) {
    if (typeof value !== "function") {
      throw new AdapterError("INCOMPATIBLE_CLIENT", "openBIS-Klasse fehlt: " + name);
    }
  }

  function checkSdk(sdk) {
    [
      "CreationId",
      "EntityTypePermId",
      "ExperimentCreation",
      "ProjectCreation",
      "SampleCreation",
      "SpacePermId",
      "SpaceSearchCriteria",
      "SpaceFetchOptions",
      "CreateProjectsOperation",
      "CreateExperimentsOperation",
      "CreateSamplesOperation",
      "SynchronousOperationExecutionOptions"
    ].forEach(function (name) { requireFunction(sdk[name], name); });
  }

  function applyProperties(creation, properties) {
    Object.keys(properties).forEach(function (propertyCode) {
      creation.setProperty(propertyCode, properties[propertyCode]);
    });
  }

  function messageFrom(error) {
    if (!error) {
      return "Unbekannter openBIS-Fehler.";
    }
    if (typeof error.getMessage === "function") {
      return String(error.getMessage());
    }
    if (error.message) {
      return String(error.message);
    }
    return String(error);
  }

  function create(client, sdk) {
    if (!client || typeof client.searchSpaces !== "function" ||
        typeof client.executeOperations !== "function") {
      throw new AdapterError("INCOMPATIBLE_CLIENT", "Ungültiger openBIS-V3-Client.");
    }
    checkSdk(sdk);

    return Object.freeze({
      listVisibleSpaces: async function () {
        try {
          var result = await client.searchSpaces(
            new sdk.SpaceSearchCriteria(), new sdk.SpaceFetchOptions()
          );
          return result.getObjects().map(function (space) {
            return {
              code: String(space.getCode()),
              description: String(space.getDescription() || "")
            };
          }).sort(function (left, right) {
            return left.code.localeCompare(right.code);
          });
        } catch (error) {
          throw new AdapterError(
            "SPACE_SEARCH_FAILED",
            "Spaces konnten nicht geladen werden: " + messageFrom(error),
            error
          );
        }
      },

      createProject: async function (plan) {
        var project = new sdk.ProjectCreation();
        project.setCreationId(new sdk.CreationId(plan.project.creationKey));
        project.setCode(plan.project.code);
        project.setSpaceId(new sdk.SpacePermId(plan.project.spaceCode));
        // Projects have no title field; the ELN shows the description's first line
        // as the title, so the description follows after a blank line.
        project.setDescription(plan.project.description ?
          plan.project.title + "\n\n" + plan.project.description : plan.project.title);

        var collectionCreations = plan.collections.map(function (item) {
          var creation = new sdk.ExperimentCreation();
          creation.setCreationId(new sdk.CreationId(item.creationKey));
          creation.setTypeId(new sdk.EntityTypePermId(item.type));
          creation.setProjectId(new sdk.CreationId(item.projectCreationKey));
          creation.setCode(item.code);
          applyProperties(creation, item.properties);
          return creation;
        });

        var objectCreations = plan.objects.map(function (item) {
          var creation = new sdk.SampleCreation();
          creation.setCreationId(new sdk.CreationId(item.creationKey));
          creation.setTypeId(new sdk.EntityTypePermId(item.type));
          creation.setSpaceId(new sdk.SpacePermId(item.spaceCode));
          creation.setProjectId(new sdk.CreationId(item.projectCreationKey));
          if (item.collectionCreationKey) {
            creation.setExperimentId(new sdk.CreationId(item.collectionCreationKey));
          }
          creation.setCode(item.code);
          applyProperties(creation, item.properties);
          return creation;
        });

        var operations = [new sdk.CreateProjectsOperation([project])];
        if (collectionCreations.length) {
          operations.push(new sdk.CreateExperimentsOperation(collectionCreations));
        }
        if (objectCreations.length) {
          operations.push(new sdk.CreateSamplesOperation(objectCreations));
        }

        try {
          await client.executeOperations(
            operations, new sdk.SynchronousOperationExecutionOptions()
          );
        } catch (error) {
          throw new AdapterError(
            "CREATE_FAILED",
            "Projekt konnte nicht angelegt werden: " + messageFrom(error),
            error
          );
        }

        return Object.freeze({
          projectIdentifier: "/" + plan.project.spaceCode + "/" + plan.project.code,
          templateCode: plan.templateCode,
          collectionCount: collectionCreations.length,
          objectCount: objectCreations.length
        });
      }
    });
  }

  function fromEmbeddedContext(root) {
    if (!root || !root.openbis || typeof root.openbis.openbis !== "function") {
      throw new AdapterError(
        "CLIENT_MISSING", "Die openBIS-JavaScript-V3-Bibliothek ist nicht verfügbar."
      );
    }
    var apiUrl = root.location.origin +
      "/openbis/openbis/rmi-application-server-v3.json";
    var client = new root.openbis.openbis(apiUrl);
    if (typeof client.getWebAppContext !== "function" ||
        typeof client.loginFromContext !== "function") {
      throw new AdapterError(
        "CONTEXT_UNSUPPORTED", "Diese openBIS-Version unterstützt keine Webapp-Sitzung."
      );
    }
    var context = client.getWebAppContext();
    if (!context || !context.getSessionId()) {
      throw new AdapterError(
        "CONTEXT_REQUIRED",
        "Bitte öffnen Sie diese Anwendung innerhalb der openBIS-Oberfläche."
      );
    }
    client.loginFromContext();

    // openBIS 20.10 supplies the context in the initial URL. Remove it from
    // browser history immediately; the V3 facade already holds the session.
    if (root.history && typeof root.history.replaceState === "function") {
      root.history.replaceState(null, root.document.title, root.location.pathname);
    }
    return create(client, root.openbis);
  }

  return Object.freeze({
    create: create,
    fromEmbeddedContext: fromEmbeddedContext,
    AdapterError: AdapterError
  });
}));
