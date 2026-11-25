import { afterEach, describe, expect, it, vi } from "vitest";

import {
  defaultExplorerLocation,
  formatExplorerHash,
  parseExplorerHash,
  resolveExplorerEntity,
  updateExplorerHistory,
} from "./explorerUrl";

describe("Explorer URLs", () => {
  it.each([
    ["#/graph/v1", { version: "v1", view: "graph", entityId: null }],
    ["#/graph/v1/ROOT", { version: "v1", view: "graph", entityId: "ROOT" }],
    [
      "#/browser/v0/EXPERIMENTAL_STEP",
      { version: "v0", view: "browser", entityId: "EXPERIMENTAL_STEP" },
    ],
    [
      "#/browser/v0/EXPERIMENTAL_STEP.DCPD",
      {
        version: "v0",
        view: "browser",
        entityId: "EXPERIMENTAL_STEP.DCPD",
      },
    ],
  ] as const)("parses and formats %s", (hash, expected) => {
    expect(parseExplorerHash(hash)).toEqual(expected);
    expect(formatExplorerHash(expected)).toBe(hash);
  });

  it.each([
    "#/graph/v2",
    "#/unknown/v1",
    "#/browser/v1/ROOT/extra",
    "#/browser/v1/%ZZ",
    "#/browser/v1/%2F",
    "#/browser/v1/",
    "#/v1/ROOT/graph", // Previous route order
    "",
  ])("rejects an invalid or absent fragment: %s", (hash) => {
    expect(parseExplorerHash(hash)).toBeNull();
  });

  it("formats the default landing route", () => {
    expect(formatExplorerHash(defaultExplorerLocation)).toBe("#/graph/v1");
  });
});

describe("resolving an entity against the loaded schema", () => {
  it("preserves a known dotted entity code", () => {
    const location = {
      version: "v0" as const,
      view: "browser" as const,
      entityId: "EXPERIMENTAL_STEP.DCPD",
    };

    expect(
      resolveExplorerEntity(location, ["EXPERIMENTAL_STEP.DCPD"]),
    ).toBe(location);
  });

  it.each(["graph", "browser"] as const)(
    "clears an unknown entity in the %s view",
    (view) => {
      const location = {
        version: "v1" as const,
        view,
        entityId: "UNKNOWN",
      };

      expect(resolveExplorerEntity(location, ["ROOT"])).toEqual({
        version: "v1",
        view,
        entityId: null,
      });
    },
  );

  it("preserves a view with no selected entity", () => {
    const location = {
      version: "v1" as const,
      view: "graph" as const,
      entityId: null,
    };

    expect(resolveExplorerEntity(location, ["ROOT"])).toBe(location);
  });
});

describe("Explorer history updates", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("adds a history entry when selecting an entity", () => {
    const pushState = vi.fn();
    const replaceState = vi.fn();

    vi.stubGlobal("window", {
      location: { hash: "#/graph/v1" },
      history: { pushState, replaceState },
    });

    updateExplorerHistory({
      version: "v1",
      view: "graph",
      entityId: "ROOT",
    });

    expect(pushState).toHaveBeenCalledOnce();
    expect(pushState).toHaveBeenCalledWith(
      null,
      "",
      "#/graph/v1/ROOT",
    );
    expect(replaceState).not.toHaveBeenCalled();
  });

  it("replaces an invalid entity URL without adding history", () => {
    const pushState = vi.fn();
    const replaceState = vi.fn();

    vi.stubGlobal("window", {
      location: { hash: "#/browser/v1/UNKNOWN" },
      history: { pushState, replaceState },
    });

    updateExplorerHistory(
      { version: "v1", view: "browser", entityId: null },
      true,
    );

    expect(replaceState).toHaveBeenCalledWith(
      null,
      "",
      "#/browser/v1",
    );
    expect(pushState).not.toHaveBeenCalled();
  });

  it("does not add another entry for the current URL", () => {
    const pushState = vi.fn();
    const replaceState = vi.fn();

    vi.stubGlobal("window", {
      location: { hash: "#/graph/v1/ROOT" },
      history: { pushState, replaceState },
    });

    updateExplorerHistory({
      version: "v1",
      view: "graph",
      entityId: "ROOT",
    });

    expect(pushState).not.toHaveBeenCalled();
    expect(replaceState).not.toHaveBeenCalled();
  });
});
