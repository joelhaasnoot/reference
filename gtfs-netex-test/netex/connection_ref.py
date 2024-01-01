from dataclasses import dataclass
from .connection_ref_structure import ConnectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionRef(ConnectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"