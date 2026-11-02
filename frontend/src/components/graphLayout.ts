import type { SchemaEdge, SchemaNode } from "../types/schema";

interface Position {
  x: number;
  y: number;
}

export function calculateForestLayout(
  nodes: SchemaNode[],
  edges: SchemaEdge[],
): Map<string, Position> {
  const positions = new Map<string, Position>();

  if (nodes.length === 0) return positions;

  const nodeIds = new Set(nodes.map((node) => node.id));
  const children = new Map<string, string[]>();
  const hasParent = new Set<string>();

  for (const node of nodes) {
    children.set(node.id, []);
  }

  for (const edge of edges) {
    if (
      edge.type !== "inheritance" ||
      !nodeIds.has(edge.source) ||
      !nodeIds.has(edge.target)
    ) {
      continue;
    }

    children.get(edge.source)!.push(edge.target);
    hasParent.add(edge.target);
  }

  for (const descendants of children.values()) {
    descendants.sort();
  }

  const roots = nodes
    .filter((node) => !hasParent.has(node.id))
    .map((node) => node.id)
    .sort();

  const NODE_SPACING_X = 190;
  const NODE_SPACING_Y = 105;
  const TREE_GAP = 100;
  const MAX_ROW_WIDTH = 1400;

  let cursorX = 0;
  let cursorY = 0;
  let rowHeight = 0;

  const visited = new Set<string>();

  for (const root of roots) {
    const levels: string[][] = [];
    const queue = [{ id: root, depth: 0 }];

    for (let index = 0; index < queue.length; index++) {
      const { id, depth } = queue[index];

      if (visited.has(id)) continue;
      visited.add(id);

      levels[depth] ??= [];
      levels[depth].push(id);

      for (const child of children.get(id) ?? []) {
        queue.push({ id: child, depth: depth + 1 });
      }
    }

    const maxWidth = Math.max(...levels.map((level) => level.length));
    const treeWidth = Math.max(1, maxWidth) * NODE_SPACING_X;
    const treeHeight = levels.length * NODE_SPACING_Y;

    if (cursorX > 0 && cursorX + treeWidth > MAX_ROW_WIDTH) {
      cursorX = 0;
      cursorY += rowHeight + TREE_GAP;
      rowHeight = 0;
    }

    levels.forEach((level, depth) => {
      const offsetX =
        (treeWidth - level.length * NODE_SPACING_X) / 2;

      level.forEach((id, index) => {
        positions.set(id, {
          x: cursorX + offsetX + index * NODE_SPACING_X,
          y: cursorY + depth * NODE_SPACING_Y,
        });
      });
    });

    cursorX += treeWidth + TREE_GAP;
    rowHeight = Math.max(rowHeight, treeHeight);
  }

  // Fallback for nodes not reached from any root.
  for (const node of nodes) {
    if (!positions.has(node.id)) {
      positions.set(node.id, {
        x: cursorX,
        y: cursorY + rowHeight + TREE_GAP,
      });

      cursorX += NODE_SPACING_X;
    }
  }

  return positions;
}
