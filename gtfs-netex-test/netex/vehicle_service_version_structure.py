from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .vehicle_service_parts_rel_structure import (
    VehicleServicePartsRelStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServiceVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleService_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_service_parts: Optional[VehicleServicePartsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleServiceParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
