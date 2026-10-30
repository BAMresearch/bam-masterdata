import { useEffect, useMemo, useRef, useState } from "react";
import type {
  SchemaEdge,
  SchemaExport,
  SchemaNode,
  SchemaVersion,
} from "./types/schema";
import "./App.css";
import { SchemaGraph } from "./components/SchemaGraph";

const versions: SchemaVersion[] = ["v0", "v1"];

type ExplorerView = "graph" | "browser";

function RelationshipHelp() {
  const detailsRef = useRef<HTMLDetailsElement>(null);

  useEffect(() => {
    function handleClickOutside(event: PointerEvent) {
      if (
        detailsRef.current &&
        !detailsRef.current.contains(event.target as Node)
      ) {
        detailsRef.current.open = false;
      }
    }

    function handleEscape(event: KeyboardEvent) {
      if (event.key === "Escape" && detailsRef.current) {
        detailsRef.current.open = false;
      }
    }

    document.addEventListener("pointerdown", handleClickOutside);
    document.addEventListener("keydown", handleEscape);

    return () => {
      document.removeEventListener("pointerdown", handleClickOutside);
      document.removeEventListener("keydown", handleEscape);
    };
  }, []);

  return (
    <details ref={detailsRef} className="relationship-help">
      <summary aria-label="Explain relationship cardinality">?</summary>

      <div className="relationship-help-content">
        <strong>Relationship cardinality</strong>

        <p>
          Cardinality indicates how many references an object can have
          through a property.
        </p>

        <dl>
          <dt>0..1</dt>
          <dd>Optional, at most one reference.</dd>

          <dt>1..1</dt>
          <dd>Required, exactly one reference.</dd>

          <dt>0..*</dt>
          <dd>Optional, multiple references allowed.</dd>

          <dt>1..*</dt>
          <dd>Required, at least one reference.</dd>
        </dl>

        <p>
          Cardinality applies to OBJECT references, not inheritance.
        </p>
      </div>
    </details>
  );
}

function App() {
  const [version, setVersion] = useState<SchemaVersion>("v1");
  const [view, setView] = useState<ExplorerView>("graph");
  const [schema, setSchema] = useState<SchemaExport | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [search, setSearch] = useState("");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadSchema() {
      setSchema(null);
      setSelectedId(null);
      setSearch("");
      setError(null);

      try {
        const response = await fetch(
          `${import.meta.env.BASE_URL}data/schema-${version}.json`,
          { signal: controller.signal },
        );

        if (!response.ok) {
          throw new Error(`Failed to load ${version}: HTTP ${response.status}`);
        }

        const data: SchemaExport = await response.json();

        if (data.version !== version) {
          throw new Error(`Expected ${version}, received ${data.version}`);
        }

        if (!Array.isArray(data.nodes) || !Array.isArray(data.edges)) {
          throw new Error("Invalid schema data");
        }

        if (!controller.signal.aborted) {
          setSchema(data);
          setSelectedId(data.nodes[0]?.id ?? null);
        }
      } catch (err) {
        if (!controller.signal.aborted) {
          setError(err instanceof Error ? err.message : "Unknown error");
        }
      }
    }

    void loadSchema();

    return () => controller.abort();
  }, [version]);

  const filteredNodes = useMemo(() => {
    if (!schema) return [];

    const query = search.trim().toLowerCase();

    return schema.nodes.filter(
      (node) =>
        node.name.toLowerCase().includes(query) ||
        node.id.toLowerCase().includes(query) ||
        node.description.toLowerCase().includes(query),
    );
  }, [schema, search]);

  const selectedNode = useMemo(
    () => schema?.nodes.find((node) => node.id === selectedId) ?? null,
    [schema, selectedId],
  );

  const relationships = useMemo(() => {
    if (!schema || !selectedNode) return [];

    return schema.edges.filter(
      (edge) =>
        edge.source === selectedNode.id ||
        edge.target === selectedNode.id,
    );
  }, [schema, selectedNode]);

  const inheritanceCount =
    schema?.edges.filter((edge) => edge.type === "inheritance").length ?? 0;

  const referenceCount =
    schema?.edges.filter((edge) => edge.type === "object_reference").length ?? 0;

  return (
    <div className="app-shell">
      <header className="site-header">
        <div className="header-inner">
          <div className="brand">
            <img
              src={`${import.meta.env.BASE_URL}assets/bammasterdata_blue_transparent.png`}
              alt="BAM Masterdata"
              className="brand-logo"
            />

            <span className="brand-divider" />

            <span className="brand-title">Schema Explorer</span>
          </div>

          <nav className="header-links" aria-label="Main navigation">
            <a
              href="https://bamresearch.github.io/bam-masterdata/"
              target="_blank"
              rel="noopener noreferrer"
            >
              Documentation
            </a>

            <a
              href="https://github.com/BAMresearch/bam-masterdata"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>
          </nav>
        </div>
      </header>

      <main className="main-content">
        <section className="page-intro">
          <div>
            <div className="eyebrow">BAM MASTERDATA</div>
            <h1>Explore the datamodel</h1>
            <p>
              Browse object types, inspect their properties, and discover
              relationships within the scientific data model.
            </p>
          </div>

          <div className="version-control">
            <label htmlFor="schema-version">Datamodel version</label>

            <select
              id="schema-version"
              value={version}
              onChange={(event) =>
                setVersion(event.target.value as SchemaVersion)
              }
            >
              {versions.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>

            {schema && (
              <div className="schema-stats" aria-label="Schema statistics">
                <span>{schema.nodes.length} types</span>
                <span>{inheritanceCount} inheritance</span>
                <span>{referenceCount} references</span>
              </div>
            )}
          </div>
        </section>

        {error && (
          <div className="error-message" role="alert">
            {error}
          </div>
        )}

        {!schema && !error && (
          <div className="loading-message" role="status">
            Loading {version} schema...
          </div>
        )}

        {schema && (
          <>
            <nav className="view-selector" aria-label="Explorer views">
              <button
                type="button"
                className={view === "graph" ? "active" : ""}
                onClick={() => setView("graph")}
                aria-current={view === "graph" ? "page" : undefined}
              >
                Graph
              </button>

              <button
                type="button"
                className={view === "browser" ? "active" : ""}
                onClick={() => setView("browser")}
                aria-current={view === "browser" ? "page" : undefined}
              >
                Object browser
              </button>
            </nav>

            {view === "graph" && (
              <section className="graph-view">
                <div className="graph-view-header">
                  <div>
                    <h2>Datamodel relationships</h2>
                    <p>
                      Complete inheritance hierarchy for {version}.
                    </p>
                  </div>
                </div>

                <SchemaGraph
                  key={version}
                  schema={schema}
                  onSelectNode={(id) => {
                    setSelectedId(id);
                    setView("browser");
                  }}
                />
              </section>
            )}

            {view === "browser" && (
              <section className="explorer-layout">
                <aside className="browser-panel">
                  <div className="panel-heading">
                    <h2>Object types</h2>
                    <span className="count-badge">{filteredNodes.length}</span>
                  </div>

                  <div className="search-container">
                    <input
                      type="search"
                      placeholder="Search object types..."
                      aria-label="Search object types"
                      value={search}
                      onChange={(event) => setSearch(event.target.value)}
                    />
                  </div>

                  <div className="object-list">
                    {filteredNodes.map((node) => (
                      <button
                        key={node.id}
                        type="button"
                        className={`object-item ${
                          selectedId === node.id ? "selected" : ""
                        }`}
                        onClick={() => setSelectedId(node.id)}
                        aria-pressed={selectedId === node.id}
                      >
                        <span className="object-icon" />
                        <span className="object-label">
                          <strong>{node.name}</strong>
                          <small>{node.id}</small>
                        </span>
                      </button>
                    ))}

                    {filteredNodes.length === 0 && (
                      <div className="empty-list">
                        No object types match your search.
                      </div>
                    )}
                  </div>
                </aside>

                <div className="details-panel">
                  {selectedNode ? (
                    <ObjectDetails
                      node={selectedNode}
                      relationships={relationships}
                      onSelectNode={setSelectedId}
                      knownIds={new Set(schema.nodes.map((node) => node.id))}
                    />
                  ) : (
                    <div className="empty-state">
                      Select an object type to inspect its definition.
                    </div>
                  )}
                </div>
              </section>
            )}
          </>
        )}
      </main>
    </div>
  );
}

function ObjectDetails({
  node,
  relationships,
  onSelectNode,
  knownIds,
}: {
  node: SchemaNode;
  relationships: SchemaEdge[];
  onSelectNode: (id: string) => void;
  knownIds: Set<string>;
}) {
  const inheritance = relationships.filter(
    (edge) => edge.type === "inheritance",
  );

  const references = relationships.filter(
    (edge) => edge.type === "object_reference",
  );

  return (
    <div className="object-details">
      <div className="details-header">
        <div className="eyebrow">OBJECT TYPE</div>
        <h2>{node.name}</h2>
        <code className="code-badge">{node.id}</code>
      </div>

      <section className="detail-section">
        <h3>Description</h3>
        <p>{node.description || "No description available."}</p>
      </section>

      {node.iri.length > 0 && (
        <section className="detail-section">
          <h3>Ontology references</h3>
          <div className="iri-list">
            {node.iri.map((iri) =>
              /^https?:\/\//.test(iri) ? (
                <a
                  key={iri}
                  href={iri}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {iri}
                </a>
              ) : (
                <code key={iri}>{iri}</code>
              ),
            )}
          </div>
        </section>
      )}

      <section className="detail-section">
        <div className="section-title">
          <h3>Properties</h3>
          <span className="count-badge">{node.properties.length}</span>
        </div>

        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Property</th>
                <th>Description</th>
                <th>Data type</th>
                <th>Reference</th>
                <th>Required</th>
                <th>Multiple</th>
              </tr>
            </thead>
            <tbody>
              {node.properties.map((property) => (
                <tr key={property.code}>
                  <td>
                    <strong>{property.property_label || property.code}</strong>
                    <small>{property.code}</small>
                    {property.units && <small>Units: {property.units}</small>}
                  </td>

                  <td className="property-description">
                    {property.description || "—"}
                  </td>

                  <td>
                    <span className="datatype-badge">
                      {property.data_type}
                    </span>
                  </td>

                  <td>
                    {property.object_code || property.vocabulary_code || "—"}
                  </td>

                  <td>{property.mandatory ? "Yes" : "No"}</td>

                  <td>{property.multivalued ? "Yes" : "No"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="detail-section">
        <div className="section-title">
          <h3>
            Relationships
           <RelationshipHelp />
          </h3>

          <span className="count-badge">{relationships.length}</span>
        </div>

        {inheritance.length > 0 && (
          <RelationshipGroup
            title="Inheritance"
            edges={inheritance}
            nodeId={node.id}
            knownIds={knownIds}
            onSelectNode={onSelectNode}
          />
        )}

        {references.length > 0 && (
          <RelationshipGroup
            title="OBJECT references"
            edges={references}
            nodeId={node.id}
            knownIds={knownIds}
            onSelectNode={onSelectNode}
          />
        )}

        {relationships.length === 0 && (
          <p className="muted">No relationships found.</p>
        )}
      </section>
    </div>
  );
}

function RelationshipGroup({
  title,
  edges,
  nodeId,
  knownIds,
  onSelectNode,
}: {
  title: string;
  edges: SchemaEdge[];
  nodeId: string;
  knownIds: Set<string>;
  onSelectNode: (id: string) => void;
}) {
  return (
    <div className="relationship-group">
      <h4>{title}</h4>

      {edges.map((edge, index) => {
        const outgoing = edge.source === nodeId;
        const relatedId = outgoing ? edge.target : edge.source;
        const resolved = knownIds.has(relatedId);

        const cardinality =
          edge.type === "object_reference"
            ? `${edge.mandatory ? "1" : "0"}..${
                edge.multivalued ? "*" : "1"
              }`
            : null;

        return (
          <div
            className="relationship-item"
            key={`${edge.source}-${edge.target}-${edge.property_code}-${index}`}
          >
            <span className="relationship-direction">
              {outgoing ? "→" : "←"}
            </span>

            {resolved ? (
              <button
                type="button"
                className="relationship-link"
                onClick={() => onSelectNode(relatedId)}
              >
                {relatedId}
              </button>
            ) : (
              <span className="unresolved-reference">
                {relatedId} (not defined)
              </span>
            )}

            {edge.property_code && (
              <code className="relationship-property">
                {edge.property_code}
              </code>
            )}

            {cardinality && (
              <span className="cardinality-badge">
                {cardinality}
              </span>
            )}
          </div>
        );
      })}
    </div>
  );
}

export default App;
