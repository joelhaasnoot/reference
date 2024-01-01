from dataclasses import dataclass
from .common_section_ref_structure import CommonSectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonSectionRef(CommonSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
