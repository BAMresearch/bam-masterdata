export type SchemaVersion = "v0" | "v1";

export interface SchemaProperty {
  code: string;
  property_label: string;
  description: string;
  data_type: string;
  mandatory: boolean;
  multivalued: boolean;
  object_code: string | null;
  vocabulary_code: string | null;
  units: string | null;
  section: string;
}

export interface SchemaNode {
  id: string;
  name: string;
  description: string;
  iri: string[];
  properties: SchemaProperty[];
}

export interface SchemaEdge {
  source: string;
  target: string;
  type: "inheritance" | "object_reference";
  property_code: string | null;
  multivalued: boolean | null;
  mandatory: boolean | null;
}

export interface SchemaExport {
  version: SchemaVersion;
  nodes: SchemaNode[];
  edges: SchemaEdge[];
}
