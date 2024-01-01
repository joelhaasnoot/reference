from dataclasses import dataclass, field


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class GmlProfileSchema:
    class Meta:
        name = "gmlProfileSchema"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
