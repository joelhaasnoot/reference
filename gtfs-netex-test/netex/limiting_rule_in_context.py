from dataclasses import dataclass
from .limiting_rule_versioned_structure import LimitingRuleVersionedStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRuleInContext(LimitingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
