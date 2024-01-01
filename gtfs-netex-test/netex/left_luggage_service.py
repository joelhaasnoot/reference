from dataclasses import dataclass
from .left_luggage_service_version_structure import (
    LeftLuggageServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LeftLuggageService(LeftLuggageServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
