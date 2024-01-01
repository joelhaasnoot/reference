from dataclasses import dataclass, field
from typing import List
from .hire_service_enumeration import HireServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "HireService_VersionStructure"

    service_list: List[List[HireServiceEnumeration]] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "tokens": True,
        },
    )
