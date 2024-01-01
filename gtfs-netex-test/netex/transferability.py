from dataclasses import dataclass
from .transferability_version_structure import TransferabilityVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Transferability(TransferabilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
