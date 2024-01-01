from dataclasses import dataclass, field
from typing import Optional
from .abstract_gmltype import AbstractGmltype


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractGeometryType(AbstractGmltype):
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
