import type { SchemaVersion } from "./types/schema";

export type ExplorerView = "graph" | "browser";

export interface ExplorerLocation {
  version: SchemaVersion;
  view: ExplorerView;
  entityId: string | null;
}

export const defaultExplorerLocation: ExplorerLocation = {
  version: "v1",
  view: "graph",
  entityId: null,
};

export function formatExplorerHash(location: ExplorerLocation): string {
  const { version, view, entityId } = location;

  return entityId
    ? `#/${version}/${encodeURIComponent(entityId)}/${view}`
    : `#/${version}/${view}`;
}

export function parseExplorerHash(hash: string): ExplorerLocation | null {
  const parts = hash.replace(/^#\/?/, "").split("/");

  if (parts.length !== 2 && parts.length !== 3) return null;

  const [version, second, third] = parts;
  if (version !== "v0" && version !== "v1") return null;

  const view = parts.length === 2 ? second : third;
  if (view !== "graph" && view !== "browser") return null;

  if (parts.length === 2) {
    return { version, view, entityId: null };
  }

  try {
    const entityId = decodeURIComponent(second);
    if (!entityId || entityId.includes("/")) return null;
    return { version, view, entityId };
  } catch {
    return null;
  }
}
