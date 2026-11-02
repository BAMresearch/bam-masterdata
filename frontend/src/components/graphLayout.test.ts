import { describe, expect, it } from "vitest";

import type { SchemaEdge, SchemaNode } from "../types/schema";
import { calculateForestLayout } from "./graphLayout";

// Minimal fixtures: the layout only uses node IDs and edge relationships.
function node(id: string): SchemaNode {
  return {
    id,
    name: id,
    description: "",
    iri: [],
    properties: [],
  };
}

function inheritance(parent: string, child: string): SchemaEdge {
  return {
    source: parent,
    target: child,
    type: "inheritance",
    property_code: null,
    mandatory: null,
    multivalued: null,
  };
}

function objectReference(source: string, target: string): SchemaEdge {
  return {
    ...inheritance(source, target),
    type: "object_reference",
  };
}

describe("calculateForestLayout", () => {
  it("returns an empty layout for an empty schema", () => {
    const positions = calculateForestLayout([], []);

    expect(positions.size).toBe(0);
  });

  it("assigns a position to every object type", () => {
    const nodes = [node("ROOT"), node("ACTIVITY"), node("ENTITY")];
    const edges = [
      inheritance("ROOT", "ACTIVITY"),
      inheritance("ROOT", "ENTITY"),
    ];

    const positions = calculateForestLayout(nodes, edges);

    expect(positions.size).toBe(nodes.length);

    for (const item of nodes) {
      const position = positions.get(item.id);

      expect(position).toBeDefined();
      expect(Number.isFinite(position!.x)).toBe(true);
      expect(Number.isFinite(position!.y)).toBe(true);
    }
  });

  it("places children below their parents", () => {
    const nodes = [
      node("ROOT"),
      node("ACTIVITY"),
      node("EXPERIMENT"),
    ];

    const edges = [
      inheritance("ROOT", "ACTIVITY"),
      inheritance("ACTIVITY", "EXPERIMENT"),
    ];

    const positions = calculateForestLayout(nodes, edges);

    const root = positions.get("ROOT")!;
    const activity = positions.get("ACTIVITY")!;
    const experiment = positions.get("EXPERIMENT")!;

    expect(root.y).toBeLessThan(activity.y);
    expect(activity.y).toBeLessThan(experiment.y);
  });

  it("places independent trees in separate positions", () => {
    const nodes = [
      node("ROOT_A"),
      node("CHILD_A"),
      node("ROOT_B"),
      node("CHILD_B"),
    ];

    const edges = [
      inheritance("ROOT_A", "CHILD_A"),
      inheritance("ROOT_B", "CHILD_B"),
    ];

    const positions = calculateForestLayout(nodes, edges);

    const a = positions.get("ROOT_A")!;
    const b = positions.get("ROOT_B")!;

    expect(a.x === b.x && a.y === b.y).toBe(false);
  });

  it("ignores OBJECT references when calculating positions", () => {
    const nodes = [
      node("ROOT"),
      node("CHILD"),
      node("OTHER"),
    ];

    const inheritanceEdges = [
      inheritance("ROOT", "CHILD"),
    ];

    const withoutReferences = calculateForestLayout(
      nodes,
      inheritanceEdges,
    );

    const withReferences = calculateForestLayout(
      nodes,
      [
        ...inheritanceEdges,
        objectReference("CHILD", "OTHER"),
      ],
    );

    expect(withReferences).toEqual(withoutReferences);
  });

  it("handles cyclic inheritance without crashing", () => {
    const nodes = [node("A"), node("B")];

    const edges = [
      inheritance("A", "B"),
      inheritance("B", "A"),
    ];

    const positions = calculateForestLayout(nodes, edges);

    expect(positions.size).toBe(2);
    expect(positions.has("A")).toBe(true);
    expect(positions.has("B")).toBe(true);
  });

  it("places isolated object types", () => {
    const nodes = [
      node("ROOT"),
      node("CHILD"),
      node("ISOLATED"),
    ];

    const edges = [inheritance("ROOT", "CHILD")];

    const positions = calculateForestLayout(nodes, edges);

    expect(positions.size).toBe(3);
    expect(positions.has("ISOLATED")).toBe(true);
  });
});
