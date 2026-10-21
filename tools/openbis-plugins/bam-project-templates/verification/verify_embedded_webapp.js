"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const pluginRoot = path.resolve(__dirname, "../1/as/webapps/bam-project-template-create");
const htmlRoot = path.join(pluginRoot, "html");
const catalogModule = require(path.join(htmlRoot, "js/template-catalog.js"));
const adapterModule = require(path.join(htmlRoot, "js/openbis-adapter.js"));
const catalogDocument = JSON.parse(
  fs.readFileSync(path.join(htmlRoot, "templates.json"), "utf8")
);

function expectCatalogFailure(document, pattern) {
  assert.throws(() => catalogModule.create(document), pattern);
}

function copy(value) {
  return JSON.parse(JSON.stringify(value));
}

function dtoClass() {
  return class Dto {
    constructor(value) {
      this.value = value;
      this.properties = Object.create(null);
    }
    setCreationId(value) { this.creationId = value; }
    setCode(value) { this.code = value; }
    setSpaceId(value) { this.spaceId = value; }
    setDescription(value) { this.description = value; }
    setTypeId(value) { this.typeId = value; }
    setProjectId(value) { this.projectId = value; }
    setExperimentId(value) { this.experimentId = value; }
    setProperty(code, value) { this.properties[code] = value; }
  };
}

const Dto = dtoClass();
class SearchResult {
  constructor(objects) { this.objects = objects; }
  getObjects() { return this.objects; }
}
class Space {
  constructor(code, description) {
    this.code = code;
    this.description = description;
  }
  getCode() { return this.code; }
  getDescription() { return this.description; }
}
class Operation {
  constructor(creations) { this.creations = creations; }
}
class SynchronousOptions {}

const sdk = {
  CreationId: Dto,
  EntityTypePermId: Dto,
  ExperimentCreation: Dto,
  ProjectCreation: Dto,
  SampleCreation: Dto,
  SpacePermId: Dto,
  SpaceSearchCriteria: Dto,
  SpaceFetchOptions: Dto,
  CreateProjectsOperation: Operation,
  CreateExperimentsOperation: Operation,
  CreateSamplesOperation: Operation,
  SynchronousOperationExecutionOptions: SynchronousOptions
};

async function run() {
  const catalog = catalogModule.create(catalogDocument);
  assert.equal(catalog.getDefaultTemplateCode(), "");
  assert.equal(catalog.listTemplates().length, 1);
  assert.equal(catalog.listTemplates()[0].code, "FB82_STANDARD");

  const emptyPlan = catalog.buildPlan({
    spaceCode: "my_space",
    projectCode: "manual_001",
    projectTitle: "Manuelles Projekt",
    projectDescription: "",
    templateCode: ""
  });
  assert.equal(emptyPlan.project.spaceCode, "MY_SPACE");
  assert.equal(emptyPlan.project.code, "MANUAL_001");
  assert.equal(emptyPlan.templateCode, "");
  assert.deepEqual(emptyPlan.collections, []);
  assert.deepEqual(emptyPlan.objects, []);

  const plan = catalog.buildPlan({
    spaceCode: "MY_SPACE",
    projectCode: "WEBAPP_001",
    projectTitle: "Sicheres Projekt",
    projectDescription: "Fachlicher Kontext",
    templateCode: "FB82_STANDARD"
  });
  assert.equal(plan.collections.length, 1);
  assert.equal(plan.objects.length, 2);
  assert.equal(plan.objects[0].type, "DOCUMENT");
  assert.equal(plan.objects[0].properties.$NAME, "Sicheres Projekt | Project Documentation");
  assert.equal(plan.objects[0].properties.DOCUMENT_TYPE, "TECHNICAL_DOCUMENT");
  assert.equal(plan.objects[1].collectionCreationKey, "collection:MEASUREMENTS");
  assert.ok(Object.isFrozen(plan));
  assert.ok(Object.isFrozen(plan.objects[0].properties));

  // Code-looking strings remain inert data. No global state is touched.
  globalThis.__bamInjectionProbe = "unchanged";
  const inertDocument = copy(catalogDocument);
  inertDocument.templates[0].objects[0].properties.NOTES =
    "__import__('os').system('touch /tmp/should-not-exist')";
  const inertCatalog = catalogModule.create(inertDocument);
  const inertPlan = inertCatalog.buildPlan({
    spaceCode: "MY_SPACE",
    projectCode: "INERT_001",
    projectTitle: "Inert",
    projectDescription: "",
    templateCode: "FB82_STANDARD"
  });
  assert.equal(
    inertPlan.objects[0].properties.NOTES,
    "__import__('os').system('touch /tmp/should-not-exist')"
  );
  assert.equal(globalThis.__bamInjectionProbe, "unchanged");

  const scriptDocument = copy(catalogDocument);
  scriptDocument.templates[0].objects[0].properties.NOTES =
    "</script><script>globalThis.__bamInjectionProbe='changed'</script>";
  const scriptPlan = catalogModule.create(scriptDocument).buildPlan({
    spaceCode: "MY_SPACE",
    projectCode: "TEXT_001",
    projectTitle: "Text",
    projectDescription: "",
    templateCode: "FB82_STANDARD"
  });
  assert.match(scriptPlan.objects[0].properties.NOTES, /<script>/);
  assert.equal(globalThis.__bamInjectionProbe, "unchanged");

  const unknownField = copy(catalogDocument);
  unknownField.templates[0].execute = "deleteEverything";
  expectCatalogFailure(unknownField, /nicht erlaubtes Feld/);

  const unknownType = copy(catalogDocument);
  unknownType.templates[0].objects[0].type = "ARBITRARY_SERVER_TYPE";
  expectCatalogFailure(unknownType, /Nicht freigegebener Object-Typ/);

  const unknownProperty = copy(catalogDocument);
  unknownProperty.templates[0].objects[0].properties.SQL = "DROP DATABASE";
  expectCatalogFailure(unknownProperty, /nicht freigegebenen Property-Code/);

  const unknownPlaceholder = copy(catalogDocument);
  unknownPlaceholder.templates[0].objects[0].properties.$NAME = "{{PYTHON_CODE}}";
  expectCatalogFailure(unknownPlaceholder, /nicht freigegebenen Platzhalter/);

  const draft = copy(catalogDocument);
  draft.templates[0].status = "draft";
  expectCatalogFailure(draft, /Nur freigegebene Templates/);

  const polluted = JSON.parse(JSON.stringify(catalogDocument));
  polluted.templates[0].objects[0].properties["__proto__"] = { polluted: true };
  // Assignment above changes the temporary object's prototype. It therefore
  // ceases to be a plain JSON object and must be rejected.
  expectCatalogFailure(polluted, /properties muss ein JSON-Objekt/);
  assert.equal({}.polluted, undefined);

  const jsonPolluted = JSON.parse(
    JSON.stringify(catalogDocument).replace(
      '"schemaVersion":1', '"__proto__":{"polluted":true},"schemaVersion":1'
    )
  );
  expectCatalogFailure(jsonPolluted, /nicht erlaubtes Feld: __proto__/);
  assert.equal({}.polluted, undefined);

  const calls = [];
  const client = {
    async searchSpaces(criteria, options) {
      calls.push({ method: "searchSpaces", criteria, options });
      return new SearchResult([
        new Space("ZETA", "Z"),
        new Space("ALPHA", "A")
      ]);
    },
    async executeOperations(operations, options) {
      calls.push({ method: "executeOperations", operations, options });
      return {};
    }
  };
  const adapter = adapterModule.create(client, sdk);
  const spaces = await adapter.listVisibleSpaces();
  assert.deepEqual(spaces.map((item) => item.code), ["ALPHA", "ZETA"]);

  const result = await adapter.createProject(plan);
  assert.equal(result.projectIdentifier, "/MY_SPACE/WEBAPP_001");
  const execution = calls.find((call) => call.method === "executeOperations");
  assert.ok(execution);
  assert.equal(execution.operations.length, 3);
  assert.ok(execution.operations[0] instanceof sdk.CreateProjectsOperation);
  assert.ok(execution.operations[1] instanceof sdk.CreateExperimentsOperation);
  assert.ok(execution.operations[2] instanceof sdk.CreateSamplesOperation);
  assert.ok(execution.options instanceof sdk.SynchronousOperationExecutionOptions);
  const project = execution.operations[0].creations[0];
  const collection = execution.operations[1].creations[0];
  const measurement = execution.operations[2].creations[1];
  assert.equal(project.description, "Sicheres Projekt");
  assert.equal(project.creationId.value, "project");
  assert.equal(collection.projectId.value, "project");
  assert.equal(measurement.projectId.value, "project");
  assert.equal(measurement.experimentId.value, "collection:MEASUREMENTS");

  const manualCalls = [];
  const manualAdapter = adapterModule.create({
    async searchSpaces() { return new SearchResult([]); },
    async executeOperations(operations, options) {
      manualCalls.push({ operations, options });
    }
  }, sdk);
  await manualAdapter.createProject(emptyPlan);
  assert.equal(manualCalls[0].operations.length, 1);
  assert.ok(manualCalls[0].operations[0] instanceof sdk.CreateProjectsOperation);

  await assert.rejects(
    adapterModule.create({
      async searchSpaces() { return new SearchResult([]); },
      async executeOperations() { throw new Error("denied"); }
    }, sdk).createProject(plan),
    /Projekt konnte nicht angelegt werden: denied/
  );

  const html = fs.readFileSync(path.join(htmlRoot, "index.html"), "utf8");
  const appSource = fs.readFileSync(path.join(htmlRoot, "js/app.js"), "utf8");
  const catalogSource = fs.readFileSync(
    path.join(htmlRoot, "js/template-catalog.js"), "utf8"
  );
  const adapterSource = fs.readFileSync(
    path.join(htmlRoot, "js/openbis-adapter.js"), "utf8"
  );
  const productionSource = [html, appSource, catalogSource, adapterSource].join("\n");
  [
    /\beval\s*\(/,
    /new\s+Function\s*\(/,
    /\.innerHTML\s*=/,
    /document\.write\s*\(/,
    /localStorage/,
    /sessionStorage/,
    /Create.*Delete|Delete.*Operation/,
    /executeCustomASService/
  ].forEach((pattern) => {
    assert.doesNotMatch(productionSource, pattern);
  });
  assert.match(html, /Content-Security-Policy/);
  assert.match(html, /openbis\.var\.js/);
  assert.doesNotMatch(html, /config\.bundle\.js|require\.js/);

  const properties = fs.readFileSync(path.join(pluginRoot, "plugin.properties"), "utf8");
  assert.match(properties, /^webapp-folder = html$/m);
  assert.doesNotMatch(properties, /Jython|script-path|class\s*=/);

  console.log("EMBEDDED WEBAPP VERIFICATION OK");
}

run().catch((error) => {
  console.error(error.stack || error);
  process.exitCode = 1;
});
