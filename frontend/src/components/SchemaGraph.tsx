import { useEffect, useMemo, useRef, useState } from "react";
import cytoscape, { type ElementDefinition } from "cytoscape";

import type { SchemaExport } from "../types/schema";
import { calculateForestLayout } from "./graphLayout";

interface SchemaGraphProps {
  schema: SchemaExport;
  onSelectNode: (id: string) => void;
}

function truncateLabel(label: string, maxLength = 24): string {
  return label.length > maxLength
    ? `${label.slice(0, maxLength - 1)}…`
    : label;
}

/**
 * Calculate hierarchy levels from inheritance edges.
 *
 * Independent roots start at level 0.
 * Object references are deliberately ignored.
 */
function calculateDepths(schema: SchemaExport): Map<string, number> {
  const depths = new Map<string, number>();
  const children = new Map<string, string[]>();
  const hasParent = new Set<string>();

  for (const node of schema.nodes) {
    children.set(node.id, []);
  }

  for (const edge of schema.edges) {
    if (edge.type !== "inheritance") continue;

    if (!children.has(edge.source) || !children.has(edge.target)) {
      continue;
    }

    children.get(edge.source)!.push(edge.target);
    hasParent.add(edge.target);
  }

  const roots = schema.nodes
    .filter((node) => !hasParent.has(node.id))
    .map((node) => node.id);

  const queue = [...roots];

  for (const root of roots) {
    depths.set(root, 0);
  }

  for (let index = 0; index < queue.length; index++) {
    const parent = queue[index];
    const parentDepth = depths.get(parent)!;

    for (const child of children.get(parent) ?? []) {
      if (depths.has(child)) continue;

      depths.set(child, parentDepth + 1);
      queue.push(child);
    }
  }

  // Defensive fallback for malformed or cyclic hierarchies.
  for (const node of schema.nodes) {
    if (!depths.has(node.id)) {
      depths.set(node.id, 0);
    }
  }

  return depths;
}

export function SchemaGraph({
  schema,
  onSelectNode,
}: SchemaGraphProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const onSelectNodeRef = useRef(onSelectNode);

  const [query, setQuery] = useState("");
  const [focusedId, setFocusedId] = useState<string | null>(null);

  const depths = useMemo(() => calculateDepths(schema), [schema]);

  const searchResults = useMemo(() => {
    const term = query.trim().toLowerCase();

    if (!term) return [];

    return schema.nodes
      .filter(
        (node) =>
          node.name.toLowerCase().includes(term) ||
          node.id.toLowerCase().includes(term),
      )
      .slice(0, 8);
  }, [schema.nodes, query]);

  const focusedNode = useMemo(
    () => schema.nodes.find((node) => node.id === focusedId) ?? null,
    [schema.nodes, focusedId],
  );

  function focusNode(id: string) {
    setFocusedId(id);
    setQuery("");
    setDepth(1);
  }

  function resetFocus() {
    setFocusedId(null);
    setQuery("");
    setDepth(Math.min(2, maxDepth));
  }

  const maxDepth = useMemo(
    () => Math.max(0, ...depths.values()),
    [depths],
  );

  const [depth, setDepth] = useState(() => Math.min(2, maxDepth));

  useEffect(() => {
    setDepth(Math.min(2, maxDepth));
  }, [schema.version, maxDepth]);

  useEffect(() => {
    onSelectNodeRef.current = onSelectNode;
  }, [onSelectNode]);

  const visibleNodes = useMemo(() => {
    // Overview: depth measured from inheritance roots.
    if (!focusedId) {
      return schema.nodes.filter(
        (node) => (depths.get(node.id) ?? 0) <= depth,
      );
    }

    // Focused mode: depth measured from the selected class.
    const adjacency = new Map<string, Set<string>>();

    for (const node of schema.nodes) {
      adjacency.set(node.id, new Set());
    }

    for (const edge of schema.edges) {
      if (edge.type !== "inheritance") continue;

      adjacency.get(edge.source)?.add(edge.target);
      adjacency.get(edge.target)?.add(edge.source);
    }

    const distances = new Map<string, number>([[focusedId, 0]]);
    const queue = [focusedId];

    for (let index = 0; index < queue.length; index++) {
      const currentId = queue[index];
      const distance = distances.get(currentId)!;

      if (distance >= depth) continue;

      for (const neighbor of adjacency.get(currentId) ?? []) {
        if (distances.has(neighbor)) continue;

        distances.set(neighbor, distance + 1);
        queue.push(neighbor);
      }
    }

    return schema.nodes.filter((node) => distances.has(node.id));
  }, [schema.nodes, schema.edges, depths, depth, focusedId]);

  const visibleEdges = useMemo(() => {
    const visibleIds = new Set(visibleNodes.map((node) => node.id));

    return schema.edges.filter(
      (edge) =>
        edge.type === "inheritance" &&
        visibleIds.has(edge.source) &&
        visibleIds.has(edge.target),
    );
  }, [schema.edges, visibleNodes]);

  useEffect(() => {
    if (!containerRef.current) return;

    const positions = calculateForestLayout(
        visibleNodes,
        visibleEdges,
    );

    const elements: ElementDefinition[] = [
      ...visibleNodes.map((node) => ({
        data: {
          id: node.id,
          label: truncateLabel(node.name),
          fullName: node.name,
          depth: depths.get(node.id) ?? 0,
        },
        position: positions.get(node.id),
        classes: node.id === focusedId ? "focused-node" : "",
      })),

      ...visibleEdges.map((edge) => ({
        data: {
            id: `inheritance:${edge.source}:${edge.target}`,
            source: edge.target, // Child
            target: edge.source, // Parent
        },
      })),
    ];

    const cy = cytoscape({
      container: containerRef.current,
      elements,

      layout: {
        name: "preset",
        fit: true,
        padding: 60,
        animate: false,
      },

      minZoom: 0.05,
      maxZoom: 5,

      wheelSensitivity: 5,
      motionBlur: false,
      pixelRatio: 1,

      style: [
        {
          selector: "node",
          style: {
            shape: "round-rectangle",
            width: 150,
            height: 44,

            "background-color": "#007599",
            "border-color": "#00556e",
            "border-width": 1.5,

            label: "data(label)",
            color: "#ffffff",
            "font-size": 14,
            "font-weight": 500,
            "text-valign": "center",
            "text-halign": "center",

            "text-wrap": "ellipsis",
            "text-max-width": "130px",
          },
        },
        {
          selector: ".focused-node",
          style: {
            "background-color": "#dcebbb",
            "border-color": "#6d9410",
            "border-width": 2.5,
            "font-weight": 700,
          },
        },
        {
          selector: "node:active",
          style: {
            "overlay-opacity": 0.08,
          },
        },
        {
        selector: "edge",
        style: {
            width: 2,
            "line-color": "#8299a5",
            "target-arrow-color": "#8299a5",
            "target-arrow-shape": "triangle",
            "target-arrow-fill": "hollow",
            "arrow-scale": 1,
            "curve-style": "bezier",
        },
        },
      ],
    });

    cy.on("tap", "node", (event) => {
      setFocusedId(event.target.id());
      setQuery("");
      setDepth(1);
    });

    return () => {
      cy.destroy();
    };
  }, [visibleNodes, visibleEdges, depths, focusedId]);

  return (
    <div className="schema-graph">
        <div className="graph-toolbar">
            <div className="graph-search">
              <input
                type="search"
                aria-label="Find an object type"
                placeholder="Search object type..."
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter" && searchResults.length > 0) {
                    focusNode(searchResults[0].id);
                  }

                  if (event.key === "Escape") {
                    setQuery("");
                  }
                }}
              />
            </div>

            <div className="depth-control">
              <label htmlFor="graph-depth">
                  Hierarchy depth
              </label>

                {searchResults.length > 0 && (
                  <div className="graph-search-results">
                    {searchResults.map((node) => (
                      <button
                        key={node.id}
                        type="button"
                        onClick={() => focusNode(node.id)}
                      >
                        <strong>{node.name}</strong>
                        <small>{node.id}</small>
                      </button>
                    ))}
                  </div>
                )}

              <input
                  id="graph-depth"
                  type="range"
                  min={0}
                  max={focusedId ? Math.max(1, maxDepth) : maxDepth}
                  value={depth}
                  disabled={!focusedId && maxDepth === 0}
                  onChange={(event) =>
                  setDepth(Number(event.target.value))
                  }
              />

              <span className="depth-value">
                  {depth} / {focusedId ? Math.max(1, maxDepth) : maxDepth}
              </span>
            </div>
        </div>

        {focusedNode && (
          <div className="graph-focus-toolbar">
            <button
              type="button"
              className="graph-back-button"
              onClick={resetFocus}
            >
              ← All classes
            </button>

            <span className="graph-focus-title">
              {focusedNode.name}
            </span>

            <button
              type="button"
              className="graph-details-button"
              onClick={() => onSelectNodeRef.current(focusedNode.id)}
            >
              View details →
            </button>
          </div>
        )}

        <div className="graph-stage">
          <div
            ref={containerRef}
            className="graph-canvas"
            aria-label="Inheritance graph"
          />

          <div className="graph-legend">
            <span className="graph-legend-arrow" aria-hidden="true">
            ───▷
            </span>
            <span>Inherits from</span>
          </div>
        </div>
    </div>
  );
}
