from dataclasses import dataclass
from .estimated_passing_time_ref_structure import (
    EstimatedPassingTimeRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeRef(EstimatedPassingTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
