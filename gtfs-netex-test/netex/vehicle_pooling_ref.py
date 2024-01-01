from dataclasses import dataclass
from .vehicle_pooling_mode_of_operation_ref_structure import (
    VehiclePoolingModeOfOperationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingRef(VehiclePoolingModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
