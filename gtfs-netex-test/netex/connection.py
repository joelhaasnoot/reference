from dataclasses import dataclass
from .connection_version_structure import ConnectionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Connection(ConnectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"