from dataclasses import dataclass
from .ordered_version_of_object_ref_structure import (
    OrderedVersionOfObjectRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentRefStructure(OrderedVersionOfObjectRefStructure):
    value: RestrictedVar
