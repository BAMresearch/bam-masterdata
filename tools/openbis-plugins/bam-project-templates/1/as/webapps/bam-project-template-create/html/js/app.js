(function () {
  "use strict";

  var state = {
    catalog: null,
    adapter: null,
    submitting: false
  };

  function byId(id) {
    return document.getElementById(id);
  }

  function setText(element, value) {
    element.textContent = value == null ? "" : String(value);
  }

  function show(element, visible) {
    element.hidden = !visible;
  }

  function option(value, label) {
    var node = document.createElement("option");
    node.value = value;
    setText(node, label);
    return node;
  }

  function userMessage(error) {
    if (!error) {
      return "Unbekannter Fehler.";
    }
    return error.message ? String(error.message) : String(error);
  }

  async function loadCatalog() {
    var response = await fetch("./templates.json", {
      cache: "no-store",
      credentials: "same-origin"
    });
    if (!response.ok) {
      throw new Error("Template-Katalog konnte nicht geladen werden.");
    }
    var body = await response.text();
    if (body.length > window.BamTemplateCatalog.limits.catalogBytes) {
      throw new Error("Template-Katalog überschreitet die erlaubte Größe.");
    }
    return window.BamTemplateCatalog.create(JSON.parse(body));
  }

  function renderSpaces(spaces) {
    var select = byId("space-code");
    select.replaceChildren();
    if (!spaces.length) {
      select.appendChild(option("", "Kein sichtbarer Space"));
      select.disabled = true;
      byId("create-button").disabled = true;
      return;
    }
    select.appendChild(option("", "Space auswählen …"));
    spaces.forEach(function (space) {
      var label = space.description ? space.code + " — " + space.description : space.code;
      select.appendChild(option(space.code, label));
    });
  }

  function renderTemplates() {
    var select = byId("template-code");
    state.catalog.listTemplates().forEach(function (template) {
      select.appendChild(option(template.code, template.label));
    });
    select.value = state.catalog.getDefaultTemplateCode();
    renderPreview();
  }

  function treeNode(code, type, kind) {
    var wrapper = document.createElement("div");
    wrapper.className = "tree-node";
    var icon = document.createElement("span");
    icon.className = "node-icon";
    icon.setAttribute("aria-hidden", "true");
    setText(icon, kind === "collection" ? "C" : "O");
    var copy = document.createElement("span");
    copy.className = "node-copy";
    var strong = document.createElement("strong");
    setText(strong, code);
    var detail = document.createElement("span");
    setText(detail, type);
    copy.append(strong, detail);
    wrapper.append(icon, copy);
    return wrapper;
  }

  function stat(value, label) {
    var node = document.createElement("div");
    node.className = "summary-stat";
    var number = document.createElement("strong");
    var text = document.createElement("span");
    setText(number, value);
    setText(text, label);
    node.append(number, text);
    return node;
  }

  function renderPreview() {
    var selectedCode = byId("template-code").value;
    var template = state.catalog.listTemplates().find(function (item) {
      return item.code === selectedCode;
    });
    var content = byId("preview-content");
    content.replaceChildren();
    var version = byId("template-version");

    if (!template) {
      setText(
        byId("template-description"),
        "Es wird ausschließlich das Projekt angelegt. Die weitere Struktur bleibt manuell."
      );
      show(version, false);
      var empty = document.createElement("div");
      empty.className = "preview-empty";
      var title = document.createElement("strong");
      var detail = document.createElement("span");
      setText(title, "Leeres Projekt");
      setText(detail, "Keine Collections oder Objects werden automatisch erzeugt.");
      empty.append(title, detail);
      content.appendChild(empty);
      return;
    }

    setText(byId("template-description"), template.description);
    setText(version, "v" + template.version);
    show(version, true);

    var summary = document.createElement("div");
    summary.className = "structure-summary";
    summary.append(
      stat(template.collections.length, "Collections"),
      stat(template.objects.length, "Objects")
    );
    content.appendChild(summary);

    var tree = document.createElement("ul");
    tree.className = "tree";
    template.objects.filter(function (item) {
      return !item.collection;
    }).forEach(function (item) {
      var row = document.createElement("li");
      row.appendChild(treeNode(item.code, item.type, "object"));
      tree.appendChild(row);
    });
    template.collections.forEach(function (collection) {
      var row = document.createElement("li");
      row.appendChild(treeNode(collection.code, collection.type, "collection"));
      var children = document.createElement("ul");
      template.objects.filter(function (item) {
        return item.collection === collection.code;
      }).forEach(function (item) {
        var child = document.createElement("li");
        child.appendChild(treeNode(item.code, item.type, "object"));
        children.appendChild(child);
      });
      if (children.childNodes.length) {
        row.appendChild(children);
      }
      tree.appendChild(row);
    });
    content.appendChild(tree);
  }

  function formInput() {
    return {
      spaceCode: byId("space-code").value,
      projectCode: byId("project-code").value,
      projectTitle: byId("project-title").value,
      projectDescription: byId("project-description").value,
      templateCode: byId("template-code").value
    };
  }

  function markNativeValidity() {
    var firstInvalid = null;
    ["space-code", "project-code", "project-title"].forEach(function (id) {
      var field = byId(id);
      var invalid = !field.value.trim();
      field.setAttribute("aria-invalid", invalid ? "true" : "false");
      if (invalid && !firstInvalid) {
        firstInvalid = field;
      }
    });
    if (firstInvalid) {
      firstInvalid.focus();
      throw new Error("Bitte füllen Sie alle Pflichtfelder aus.");
    }
  }

  function setSubmitting(value) {
    state.submitting = value;
    var button = byId("create-button");
    button.disabled = value;
    button.classList.toggle("is-busy", value);
    setText(button.querySelector(".button-label"), value ? "Wird angelegt …" : "Projekt anlegen");
    setText(byId("form-status"), value ? "Transaktion läuft" : "");
  }

  function showSubmitError(message) {
    var error = byId("submit-error");
    setText(error, message);
    show(error, Boolean(message));
  }

  async function submit(event) {
    event.preventDefault();
    if (state.submitting) {
      return;
    }
    showSubmitError("");
    try {
      markNativeValidity();
      var plan = state.catalog.buildPlan(formInput());
      setSubmitting(true);
      var result = await state.adapter.createProject(plan);
      setText(byId("success-identifier"), result.projectIdentifier);
      var structure = result.templateCode ?
        result.collectionCount + " Collection(s) und " + result.objectCount + " Object(s)" :
        "keine automatische Template-Struktur";
      setText(
        byId("success-summary"),
        "openBIS hat das Projekt und " + structure + " vollständig gespeichert."
      );
      show(byId("workspace"), false);
      show(byId("success-state"), true);
      byId("success-state").focus();
    } catch (error) {
      showSubmitError(userMessage(error));
    } finally {
      setSubmitting(false);
    }
  }

  function resetForm() {
    byId("project-form").reset();
    byId("template-code").value = state.catalog.getDefaultTemplateCode();
    byId("description-count").textContent = "0 / 10000";
    ["space-code", "project-code", "project-title"].forEach(function (id) {
      byId(id).removeAttribute("aria-invalid");
    });
    showSubmitError("");
    renderPreview();
    show(byId("success-state"), false);
    show(byId("workspace"), true);
    byId("space-code").focus();
  }

  function bindEvents() {
    byId("template-code").addEventListener("change", renderPreview);
    byId("project-code").addEventListener("input", function (event) {
      var start = event.target.selectionStart;
      event.target.value = event.target.value.toUpperCase();
      event.target.setSelectionRange(start, start);
      event.target.removeAttribute("aria-invalid");
    });
    byId("space-code").addEventListener("change", function (event) {
      event.target.removeAttribute("aria-invalid");
    });
    byId("project-title").addEventListener("input", function (event) {
      event.target.removeAttribute("aria-invalid");
    });
    byId("project-description").addEventListener("input", function (event) {
      setText(byId("description-count"), event.target.value.length + " / 10000");
    });
    byId("project-form").addEventListener("submit", submit);
    byId("create-another-button").addEventListener("click", resetForm);
  }

  async function start() {
    bindEvents();
    try {
      state.adapter = window.BamOpenbisAdapter.fromEmbeddedContext(window);
      var loaded = await Promise.all([
        loadCatalog(),
        state.adapter.listVisibleSpaces()
      ]);
      state.catalog = loaded[0];
      renderSpaces(loaded[1]);
      renderTemplates();
      show(byId("loading-state"), false);
      show(byId("workspace"), true);
    } catch (error) {
      show(byId("loading-state"), false);
      setText(byId("startup-error"), userMessage(error));
      show(byId("error-state"), true);
    }
  }

  document.addEventListener("DOMContentLoaded", start);
}());
