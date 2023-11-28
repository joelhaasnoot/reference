from dataclasses import dataclass, field
from typing import Optional
from netex.access_zone_ref import AccessZoneRef
from netex.administrative_zone_ref import AdministrativeZoneRef
from netex.fare_zone_ref import FareZoneRef
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.stop_area_ref import StopAreaRef
from netex.tariff_zone_ref import TariffZoneRef
from netex.transport_administrative_zone_ref import TransportAdministrativeZoneRef
from netex.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "zoneRefs_RelStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
