from dataclasses import dataclass
from .distance_matrix_element_ref_structure import (
    DistanceMatrixElementRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementInverseRef(DistanceMatrixElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
