from dataclasses import dataclass, field
from typing import Optional
from .direction_ref_structure import DirectionRefStructure
from .direction_type_enumeration import DirectionTypeEnumeration
from .external_object_ref_structure import ExternalObjectRefStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DirectionValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "Direction_ValueStructure"

    external_direction_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    opposite_direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "OppositeDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
