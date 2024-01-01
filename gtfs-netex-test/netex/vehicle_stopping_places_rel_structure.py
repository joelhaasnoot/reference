from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleStoppingPlaces_RelStructure"

    vehicle_stopping_place_ref_or_vehicle_stopping_place: List[
        Union[VehicleStoppingPlaceRef, VehicleStoppingPlace]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleStoppingPlaceRef",
                    "type": VehicleStoppingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlace",
                    "type": VehicleStoppingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
