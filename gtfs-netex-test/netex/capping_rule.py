from dataclasses import dataclass
from .capping_rule_versioned_child_structure import (
    CappingRuleVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRule(CappingRuleVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
