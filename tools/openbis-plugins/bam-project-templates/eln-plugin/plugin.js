/*
 * BAM project templates for the ELN "New Project" form.
 *
 * Adds a template choice to the normal create form through the documented
 * afterViewPaint hook. With a template selected, Save creates the project and
 * the template's collections and objects in one executeOperations() call with
 * the user's own session. Without a template the ELN saves as usual.
 * No server-side code and no changes to ELN files.
 */
(function () {
  "use strict";

  var BASE = "./plugins/bam-project-templates/";
  var SDK_MODULES = {
    CreationId: "as/dto/common/id/CreationId",
    EntityTypePermId: "as/dto/entitytype/id/EntityTypePermId",
    ExperimentCreation: "as/dto/experiment/create/ExperimentCreation",
    ProjectCreation: "as/dto/project/create/ProjectCreation",
    SampleCreation: "as/dto/sample/create/SampleCreation",
    SpacePermId: "as/dto/space/id/SpacePermId",
    SpaceSearchCriteria: "as/dto/space/search/SpaceSearchCriteria",
    SpaceFetchOptions: "as/dto/space/fetchoptions/SpaceFetchOptions",
    CreateProjectsOperation: "as/dto/project/create/CreateProjectsOperation",
    CreateExperimentsOperation: "as/dto/experiment/create/CreateExperimentsOperation",
    CreateSamplesOperation: "as/dto/sample/create/CreateSamplesOperation",
    SynchronousOperationExecutionOptions: "as/dto/operation/SynchronousOperationExecutionOptions"
  };
  var NO_TEMPLATE_HELP =
    "Legt nur das Projekt an. Collections und Objekte werden anschließend manuell erstellt.";

  function loadScript(name) {
    return new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = BASE + name;
      script.onload = resolve;
      script.onerror = function () { reject(new Error("Could not load " + name)); };
      document.head.appendChild(script);
    });
  }

  // Catalog and engine load once; every form reuses the validated catalog.
  var ready = null;
  function load() {
    if (!ready) {
      ready = Promise.all([loadScript("template-catalog.js"), loadScript("openbis-adapter.js")])
        .then(function () {
          return fetch(BASE + "templates.json", { cache: "no-store", credentials: "same-origin" });
        })
        .then(function (response) {
          if (!response.ok) {
            throw new Error("Template catalog could not be loaded.");
          }
          return response.json();
        })
        .then(function (document) {
          return window.BamTemplateCatalog.create(document);
        });
      ready.catch(function () { ready = null; });
    }
    return ready;
  }

  function loadSdk() {
    var names = Object.keys(SDK_MODULES);
    return new Promise(function (resolve, reject) {
      require(names.map(function (name) { return SDK_MODULES[name]; }), function () {
        var sdk = {};
        for (var i = 0; i < names.length; i++) {
          sdk[names[i]] = arguments[i];
        }
        resolve(sdk);
      }, reject);
    });
  }

  function escapeHtml(value) {
    return $("<div>").text(value).html();
  }

  // The ELN stores the project description as rich text: title as an escaped
  // paragraph, followed by the sanitized description.
  function richDescription(project) {
    var title = "<p>" + escapeHtml(project.title) + "</p>";
    return project.description ? title + DOMPurify.sanitize(project.description) : title;
  }

  // Form state per ELN view id. The ELN copies the painted form, so element
  // data and handlers would be lost; attributes and delegated events survive.
  var states = Object.create(null);
  var templates = [];

  function attach(model, $container) {
    // ELN 20.10 shows these always-visible create sections from an async
    // callback that can run before the form is in the page, leaving it empty.
    $container.find('[id^="project-identification-info-"], [id^="project-description-"]').show();
    var $code = $container.find('[id^="project-code-id-"]').first();
    var $anchor = $code.closest(".form-group");
    var section = $code.closest('[id^="project-identification-info-"]').attr("id");
    if (!$anchor.length || !section) {
      return;
    }
    var viewId = section.slice("project-identification-info-".length);
    states[viewId] = { model: model, templateCode: "", title: "" };

    var $title = FormUtil._getInputField("text", null, "Project Title", null, false);
    $title.addClass("bam-project-title").attr("data-view-id", viewId);
    var $titleRow = FormUtil.getFieldForComponentWithLabel($title, "Project Title");
    $titleRow.addClass("bam-project-title-row").hide();
    var $select = $("<select>", { "class": "form-control bam-project-template", "data-view-id": viewId });
    $select.append($("<option>", { value: "", text: "Kein Template – Projekt manuell anlegen" }));
    var $help = $("<p>", { "class": "help-block bam-project-template-help" }).text(NO_TEMPLATE_HELP);
    var $selectRow = FormUtil.getFieldForComponentWithLabel($select, "Project Template");
    $selectRow.append($help);
    $anchor.after($selectRow, $titleRow);

    load().then(function (catalog) {
      templates = catalog.listTemplates();
      var select = document.querySelector('select.bam-project-template[data-view-id="' + viewId + '"]');
      templates.forEach(function (template) {
        $(select).append($("<option>", { value: template.code, text: template.label }));
      });
    }, function () {
      var select = document.querySelector('select.bam-project-template[data-view-id="' + viewId + '"]');
      $(select).prop("disabled", true);
      $(select).closest(".form-group").parent().find(".bam-project-template-help")
        .text("Projekt-Templates konnten nicht geladen werden.");
    });
  }

  document.addEventListener("change", function (event) {
    var select = event.target;
    if (!select.matches || !select.matches("select.bam-project-template")) {
      return;
    }
    var state = states[select.getAttribute("data-view-id")];
    if (!state) {
      return;
    }
    state.templateCode = select.value;
    state.model.isFormDirty = true;
    var template = templates.filter(function (t) { return t.code === state.templateCode; })[0];
    var section = select.closest('[id^="project-identification-info-"]');
    $(section).find(".bam-project-template-help").text(template ? template.description : NO_TEMPLATE_HELP);
    $(section).find(".bam-project-title-row").toggle(Boolean(template));
  });

  document.addEventListener("input", function (event) {
    var input = event.target;
    if (input.matches && input.matches("input.bam-project-title")) {
      var state = states[input.getAttribute("data-view-id")];
      if (state) {
        state.title = input.value;
      }
    }
  });

  function createFromTemplate(state) {
    var project = state.model.project;
    Util.blockUI();
    Promise.all([load(), loadSdk()]).then(function (loaded) {
      var plan = loaded[0].buildPlan({
        spaceCode: project.spaceCode || "",
        projectCode: project.code || "",
        projectTitle: state.title || "",
        projectDescription: project.description || "",
        templateCode: state.templateCode
      });
      var adapter = window.BamOpenbisAdapter.create(
        mainController.openbisV3, loaded[1], { projectDescription: richDescription }
      );
      return adapter.createProject(plan);
    }).then(function (result) {
      state.model.isFormDirty = false;
      Util.showSuccess("Project created from template.", function () {
        mainController.tabContent.closeCurrentTab();
        mainController.changeView("showProjectPageFromIdentifier", result.projectIdentifier);
        mainController.sideMenu.refreshCurrentNode();
        Util.unblockUI();
      });
    }, function (error) {
      Util.showError(error && error.message ? error.message : String(error), function () {
        Util.unblockUI();
      });
    });
  }

  // Runs before the ELN's own Save handler. Save button and form share the
  // ELN view id (save-btn-project-<id>, project-identification-info-<id>).
  // Only takes over when that form has a template selected.
  document.addEventListener("click", function (event) {
    var button = event.target.closest && event.target.closest('[id^="save-btn-project-"]');
    if (!button) {
      return;
    }
    var viewId = button.id.slice("save-btn-project-".length);
    var section = document.getElementById("project-identification-info-" + viewId);
    var state = section && states[viewId];
    if (!state || !state.templateCode) {
      return;
    }
    event.preventDefault();
    event.stopImmediatePropagation();
    createFromTemplate(state);
  }, true);

  function BamProjectTemplatesPlugin() {
    this.init();
  }

  $.extend(BamProjectTemplatesPlugin.prototype, ELNLIMSPlugin.prototype, {
    init: function () {},
    afterViewPaint: function (viewType, model, $container) {
      if (viewType === ViewType.PROJECT_FORM && model.mode === FormMode.CREATE) {
        attach(model, $container);
      }
    }
  });

  profile.plugins.push(new BamProjectTemplatesPlugin());
}());
