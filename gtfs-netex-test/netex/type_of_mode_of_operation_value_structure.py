from dataclasses import dataclass
from .type_of_entity_version_structure import TypeOfEntityVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfModeOfOperationValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfModeOfOperation_ValueStructure"