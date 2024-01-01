from dataclasses import dataclass, field
from typing import List, Union
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .quay_ref import QuayRef
from .taxi_stand_ref import TaxiStandRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "quayRefs_RelStructure"

    quay_ref: List[Union[TaxiStandRef, QuayRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
