from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.metadata.definitions import ObjectTypeDef

# Hierarchy of the Entity branch of datamodel/v1:

#   Entity                          (see `base_objects.py`)
#   ├── Context
#   │   ├── Software
#   │   ├── WorkflowDefinition
#   │   ├── Pseudopotential
#   │   ├── SimulatedSystem
#   │   └── ComputationalMethod
#   └── MaterialEntity
#       └── HPC


class Context(Entity):
    defs = ObjectTypeDef(
        code="CONTEXT",
        description="A Context is an entity that carries information about other entities or activities, "
        "such as specifications, parameters, or results.",
        generated_code_prefix="CTX",
        iri=["http://purl.obolibrary.org/obo/IAO_0000030"],
    )


class MaterialEntity(Entity):
    defs = ObjectTypeDef(
        code="MATERIAL_ENTITY",
        description="A MaterialEntity is an entity that has some portion of matter as part, such as a "
        "material, a sample, or a device.",
        generated_code_prefix="MAT_ENT",
        iri=["http://purl.obolibrary.org/obo/BFO_0000040"],
    )
