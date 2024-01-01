from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_facility_set import ServiceFacilitySet
from .service_facility_set_ref import ServiceFacilitySetRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceFacilitySets_RelStructure"

    service_facility_set_ref_or_service_facility_set: List[
        Union[ServiceFacilitySetRef, ServiceFacilitySet]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFacilitySet",
                    "type": ServiceFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
