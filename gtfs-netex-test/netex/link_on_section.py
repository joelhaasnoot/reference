from dataclasses import dataclass
from .link_on_section_versioned_child_structure import (
    LinkOnSectionVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkOnSection(LinkOnSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
