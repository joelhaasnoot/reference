from dataclasses import dataclass
from .repeated_trip_fare_request_ref_structure import (
    RepeatedTripFareRequestRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RepeatedTripFareRequestRef(RepeatedTripFareRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
