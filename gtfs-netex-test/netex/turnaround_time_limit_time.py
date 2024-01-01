from dataclasses import dataclass
from .turnaround_time_limit_time_versioned_child_structure import (
    TurnaroundTimeLimitTimeVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TurnaroundTimeLimitTime(TurnaroundTimeLimitTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
