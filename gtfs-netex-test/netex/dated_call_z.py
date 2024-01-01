from dataclasses import dataclass
from .dated_call_versioned_child_structure import (
    DatedCallVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedCallZ(DatedCallVersionedChildStructure):
    class Meta:
        name = "DatedCall-Z"
        namespace = "http://www.netex.org.uk/netex"