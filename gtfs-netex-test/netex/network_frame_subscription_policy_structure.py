from dataclasses import dataclass, field
from typing import Optional


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkFrameSubscriptionPolicyStructure:
    incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
