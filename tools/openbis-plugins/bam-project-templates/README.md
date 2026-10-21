# Project template webapp (proposal)

An openBIS webapp that creates a new project together with an agreed starting
structure in one step. It was built for FB 8.2, but the template catalog is
generic, so other departments could add their own templates.

**Status:** proposal, tested only on a local openBIS 20.10.12 instance. Not
deployed anywhere.

## What it does

The user picks a space, project code, title, description and a template. The
webapp then creates, in a single transaction:

- the project (description stored on the native project),
- the template's collections (FB 8.2: `MEASUREMENTS`),
- the template's objects (FB 8.2: a `DOCUMENT` for the project documentation
  and an initial `MEASUREMENT`).

If any part fails, nothing is created.

## Security model

- **Client-side only.** The plugin registers a static webapp folder
  (`webapp-folder = html`). There is no custom AS service, no Jython and no
  server-side code.
- **User's own session.** It uses the embedded webapp context and the logged-in
  user's session. openBIS checks every operation; the webapp cannot do anything
  the user could not already do through the V3 API.
- **Create operations only.** The adapter builds only `CreateProjectsOperation`,
  `CreateExperimentsOperation` and `CreateSamplesOperation` and sends them in one
  synchronous `executeOperations()` call.
- **Templates are data, not commands.** `templates.json` is validated against an
  allowlist of types, property codes and placeholders defined in
  `template-catalog.js`. Extending what templates may create requires a reviewed
  code change, not just a JSON edit. Values are inserted as text only.
- **No dependencies.** No npm/CDN packages; the page uses the instance's own
  `openbis.var.js` and a strict Content Security Policy.

Remaining risks: a malicious change to the deployed JavaScript could misuse the
user's session, so installation and updates need review and controlled write
access to `servers/core-plugins`. openBIS 20.10 passes the session ID in the
initial query string; the app removes it from the browser history, but proxy
logs should not keep query strings.

## Files

| File | Purpose |
| --- | --- |
| `plugin.properties` | registers the static webapp folder |
| `html/templates.json` | released templates |
| `html/js/template-catalog.js` | validation, allowlist, placeholders, creation plan |
| `html/js/openbis-adapter.js` | the only openBIS V3 integration point |
| `html/js/app.js` | form and user feedback |
| `verification/verify_embedded_webapp.js` | offline tests (injection payloads, allowlist, single transaction) |

## Installation

1. Copy `bam-project-templates` to `servers/core-plugins/`.
2. Add `bam-project-templates` to `enabled-modules` in `core-plugins.properties`.
3. Restart the application server.
4. Open it from the openBIS modules menu ("Projekt aus Template").

## Tests

```bash
node tools/openbis-plugins/bam-project-templates/verification/verify_embedded_webapp.js
```

A live test (create, read back, forced rollback, cleanup) was run against a
local openBIS 20.10.12 Docker instance; it is not included because it depends
on that local setup.
