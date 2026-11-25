# AUTO-GENERATED CLASS HIERARCHY — DO NOT EDIT
#
# Synthesis*
# ├── ResinSynthesis
# └── NanoParticleSynthesis
#
# END AUTO-GENERATED CLASS HIERARCHY


from bam_masterdata.datamodel.v1.activities import Synthesis
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment


class ResinSynthesis(Synthesis):
    defs = ObjectTypeDef(
        code="RESIN_SYNTHESIS",
        description="A ResinSynthesis is a synthesis that produces a resin from "
        "monomers or prepolymers.",
        generated_code_prefix="RESIN_SYNTH",
    )


class NanoParticleSynthesis(Synthesis):
    defs = ObjectTypeDef(
        code="NANO_PARTICLE_SYNTHESIS",
        description="A NanoParticleSynthesis is a synthesis that produces particles "
        "with dimensions in the nanometre range.",
        generated_code_prefix="NP_SYNTH",
    )
