from dataclasses import dataclass
from .onward_service_link_derived_view_structure import (
    OnwardServiceLinkDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardServiceLinkView(OnwardServiceLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
