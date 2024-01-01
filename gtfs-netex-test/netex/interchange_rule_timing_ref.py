from dataclasses import dataclass
from .interchange_rule_timing_ref_structure import (
    InterchangeRuleTimingRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleTimingRef(InterchangeRuleTimingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
