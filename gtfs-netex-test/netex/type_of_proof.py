from dataclasses import dataclass
from .type_of_proof_value_structure import TypeOfProofValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProof(TypeOfProofValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
