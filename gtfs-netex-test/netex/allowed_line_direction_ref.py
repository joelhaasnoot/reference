from dataclasses import dataclass
from .allowed_line_direction_ref_structure import (
    AllowedLineDirectionRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllowedLineDirectionRef(AllowedLineDirectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
