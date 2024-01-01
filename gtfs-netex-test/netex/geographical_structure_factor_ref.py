from dataclasses import dataclass
from .geographical_structure_factor_ref_structure import (
    GeographicalStructureFactorRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalStructureFactorRef(GeographicalStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"