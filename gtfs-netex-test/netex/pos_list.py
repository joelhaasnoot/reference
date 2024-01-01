from dataclasses import dataclass
from .direct_position_list_type import DirectPositionListType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"
