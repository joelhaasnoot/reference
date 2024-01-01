from dataclasses import dataclass
from .vehicle_pooling_service_ref_structure import (
    VehiclePoolingServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarPoolingServiceRefStructure(VehiclePoolingServiceRefStructure):
    value: RestrictedVar
