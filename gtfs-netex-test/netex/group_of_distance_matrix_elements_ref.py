from dataclasses import dataclass
from .group_of_distance_matrix_elements_ref_structure_element import (
    GroupOfDistanceMatrixElementsRefStructureElement,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfDistanceMatrixElementsRef(
    GroupOfDistanceMatrixElementsRefStructureElement
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
