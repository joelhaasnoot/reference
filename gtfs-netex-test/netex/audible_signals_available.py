from dataclasses import dataclass, field
from .limitation_status_enumeration import LimitationStatusEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AudibleSignalsAvailable:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LimitationStatusEnumeration = field(
        default=LimitationStatusEnumeration.FALSE,
        metadata={
            "required": True,
        },
    )
