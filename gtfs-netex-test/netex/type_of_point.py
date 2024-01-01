from dataclasses import dataclass, field
from .type_of_point_value_structure import TypeOfPointValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPoint(TypeOfPointValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="Point",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
