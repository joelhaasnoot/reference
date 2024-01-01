from dataclasses import dataclass, field
from typing import List
from .delta_value import DeltaValue


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeltaValuesRelStructure:
    class Meta:
        name = "deltaValues_RelStructure"

    delta_value: List[DeltaValue] = field(
        default_factory=list,
        metadata={
            "name": "DeltaValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
