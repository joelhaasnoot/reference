from dataclasses import dataclass
from .scheduled_mode_of_operation_ref_structure import (
    ScheduledModeOfOperationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledModeOfOperationRef(ScheduledModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
