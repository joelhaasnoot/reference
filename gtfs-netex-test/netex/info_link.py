from dataclasses import dataclass
from .info_link_structure import InfoLinkStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfoLink(InfoLinkStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
