from dataclasses import dataclass, field
from typing import List, Optional


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class DirectPositionType:
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
