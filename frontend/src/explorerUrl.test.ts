import { describe, expect, it } from "vitest";
import {
  formatExplorerHash,
  parseExplorerHash,
} from "./explorerUrl";

describe("Explorer URLs", () => {
  it.each([
    ["#/v1/graph", { version: "v1", view: "graph", entityId: null }],
    ["#/v1/ROOT/graph", { version: "v1", view: "graph", entityId: "ROOT" }],
    [
      "#/v0/EXPERIMENTAL_STEP/browser",
      { version: "v0", view: "browser", entityId: "EXPERIMENTAL_STEP" },
    ],
    [
      "#/v0/EXPERIMENTAL_STEP.DCPD/browser",
      {
        version: "v0",
        view: "browser",
        entityId: "EXPERIMENTAL_STEP.DCPD",
      },
    ],
  ] as const)("parses %s", (hash, expected) => {
    expect(parseExplorerHash(hash)).toEqual(expected);
    expect(formatExplorerHash(expected)).toBe(hash);
  });

  it.each([
    "#/v2/ROOT/graph",
    "#/v1/ROOT/unknown",
    "#/v1/ROOT/graph/extra",
    "#/v1/%ZZ/browser",
    "#/v1/%2F/browser",
    "#/v1//browser",
  ])("rejects an invalid fragment: %s", (hash) => {
    expect(parseExplorerHash(hash)).toBeNull();
  });
});
