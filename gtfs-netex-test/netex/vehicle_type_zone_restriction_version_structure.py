from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from .alternative_texts_rel_structure import VersionedChildStructure
from .compound_train_ref import CompoundTrainRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .transport_zone_use_enumeration import TransportZoneUseEnumeration
from .vehicle_type_ref import VehicleTypeRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeZoneRestrictionVersionStructure(VersionedChildStructure):
    class Meta:
        name = "VehicleTypeZoneRestriction_VersionStructure"

    zone_use: Optional[TransportZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_speed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumSpeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_type_ref_or_vehicle_type_ref: Optional[
        Union[
            SimpleVehicleTypeRef,
            CompoundTrainRef,
            TrainRef,
            VehicleTypeRef,
            TransportTypeRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
