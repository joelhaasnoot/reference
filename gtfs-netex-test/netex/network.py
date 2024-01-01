from dataclasses import dataclass
from .network_version_structure import NetworkVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Network(NetworkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"