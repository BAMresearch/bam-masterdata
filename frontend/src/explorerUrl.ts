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
    ? `#/${view}/${version}/${encodeURIComponent(entityId)}`
    : `#/${view}/${version}`;
}

export function parseExplorerHash(hash: string): ExplorerLocation | null {
  const parts = hash.replace(/^#\/?/, "").split("/");

  if (parts.length !== 2 && parts.length !== 3) return null;

  const [view, version, encodedEntityId] = parts;

  if (view !== "graph" && view !== "browser") return null;
  if (version !== "v0" && version !== "v1") return null;

  if (parts.length === 2) {
    return { version, view, entityId: null };
  }

  try {
    const entityId = decodeURIComponent(encodedEntityId);
    if (!entityId || entityId.includes("/")) return null;

    return { version, view, entityId };
  } catch {
    return null;
  }
}

export function resolveExplorerEntity(
  location: ExplorerLocation,
  knownIds: readonly string[],
): ExplorerLocation {
  if (location.entityId && !knownIds.includes(location.entityId)) {
    return { ...location, entityId: null };
  }

  return location;
}

export function updateExplorerHistory(
  location: ExplorerLocation,
  replace = false,
): void {
  const hash = formatExplorerHash(location);

  if (window.location.hash === hash) return;

  if (replace) {
    window.history.replaceState(null, "", hash);
  } else {
    window.history.pushState(null, "", hash);
  }
}
