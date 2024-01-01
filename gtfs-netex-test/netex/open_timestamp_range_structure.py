from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OpenTimestampRangeStructure:
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
