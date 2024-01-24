from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .abbringer_info_type import AbbringerInfoType
from .fahrt_idext_type import FahrtIdextType


@dataclass(kw_only=True)
class WartetBisType:
    asbid: str = field(
        metadata={
            "name": "ASBID",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    abbringer_info: AbbringerInfoType = field(
        metadata={
            "name": "AbbringerInfo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    fahrt_idext: List[FahrtIdextType] = field(
        default_factory=list,
        metadata={
            "name": "FahrtIDExt",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    abfahrtszeit_asbprognose: XmlDateTime = field(
        metadata={
            "name": "AbfahrtszeitASBPrognose",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    verlaesslichkeit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Verlaesslichkeit",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
            "max_inclusive": 5,
            "total_digits": 1,
        },
    )
    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
            "type": "Attribute",
            "required": True,
        }
    )