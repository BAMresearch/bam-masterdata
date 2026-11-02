from bam_masterdata.datamodel.v1.base_objects import Entity
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment

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


class Software(Context):
    defs = ObjectTypeDef(
        code="SOFTWARE",
        description="A Software is a context that specifies a computer program or library, in a given version, which "
        "can be executed to carry out a computation.",
        generated_code_prefix="SW",
        iri=["http://purl.obolibrary.org/obo/IAO_0000010"],
        prev_versions=["SOFTWARE_CODE:v0"],
    )

    version = PropertyTypeAssignment(
        code="VERSION",
        data_type="VARCHAR",
        property_label="Version",
        description="Version identifier of the entity, such as a release number or a date.",
        mandatory=False,
        section="Software Details",
        prev_versions=["VERSION:v0"],
    )

    license = PropertyTypeAssignment(
        code="LICENSE",
        data_type="VARCHAR",
        property_label="License",
        description="License under which the entity is distributed.",
        mandatory=False,
        section="Software Details",
        prev_versions=["LICENSE:v0"],
    )

    link = PropertyTypeAssignment(
        code="LINK",
        data_type="HYPERLINK",
        property_label="Link",
        description="Website or download location of the entity, such as the project page or a repository.",
        mandatory=False,
        section="Software Details",
        prev_versions=["SOURCE_LINK:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from SOFTWARE_CODE:v0):
    # SOFTWARE_NAME
    # REFERENCE


class WorkflowDefinition(Context):
    defs = ObjectTypeDef(
        code="WORKFLOW_DEFINITION",
        description="A WorkflowDefinition is a context that specifies the steps of a computational "
        "workflow and the order in which they are executed.",
        generated_code_prefix="WF_DEF",
        iri=["https://w3id.org/pmd/co/PMD_0000012"],
        prev_versions=["WORKFLOW_REFERENCE:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from WORKFLOW_REFERENCE:v0):
    # REFERENCE


class HPC(MaterialEntity):
    defs = ObjectTypeDef(
        code="HPC",
        description="An HPC is a material entity consisting of a high-performance computing cluster "
        "used to execute computations.",
        generated_code_prefix="HPC",
        iri=["https://w3id.org/pmd/co/PMD_0000582"],
        prev_versions=["HPC:v0"],
    )

    alias = PropertyTypeAssignment(
        code="ALIAS",
        data_type="VARCHAR",
        property_label="Alias",
        description="Alternative name of the entity, such as an abbreviation or nickname.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["ALIAS:v0"],
    )

    cpu_nodes_config = PropertyTypeAssignment(
        code="CPU_NODES_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="CPU node configuration",
        description="Configuration of the CPU nodes of the cluster, such as processor type, cores and memory per node.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["CPU_NODES_CONFIG:v0"],
    )

    gpu_nodes_config = PropertyTypeAssignment(
        code="GPU_NODES_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="GPU node configuration",
        description="Configuration of the GPU nodes of the cluster, such as GPU type and number of GPUs per node.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["GPU_NODES_CONFIG:v0"],
    )

    file_system_config = PropertyTypeAssignment(
        code="FILE_SYSTEM_CONFIG",
        data_type="MULTILINE_VARCHAR",
        property_label="File system configuration",
        description="Configuration of the file systems available on the cluster.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["FILE_SYSTEM_CONFIG:v0"],
    )

    external_address = PropertyTypeAssignment(
        code="HPC_EXT_PHYS_ADDRESS",
        data_type="VARCHAR",
        property_label="External HPC address",
        description="Physical address of the cluster when it is operated by an external institution.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["HPC_EXT_PHYS_ADDRESS:v0"],
    )

    external_contact = PropertyTypeAssignment(
        code="HPC_EXT_EMAIL_ADDRESS",
        data_type="VARCHAR",
        property_label="External HPC contact",
        description="Email address or point of contact of the cluster when it is operated by an external institution.",
        mandatory=False,
        section="HPC Details",
        prev_versions=["HPC_EXT_EMAIL_ADDRESS:v0"],
    )

    # Properties from v0 that need to be migrated to v1 (from HPC:v0):
    # OPERATING_SYSTEM
    # QUEUING_SYSTEM
    # RESPONSIBLE_PERSON
    # CO_RESPONSIBLE_PERSON
    # REFERENCE
