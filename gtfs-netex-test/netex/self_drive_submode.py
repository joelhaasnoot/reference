from dataclasses import dataclass, field
from .self_drive_submode_enumeration import SelfDriveSubmodeEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SelfDriveSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SelfDriveSubmodeEnumeration = field(
        default=SelfDriveSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
