from dataclasses import dataclass
from .subscription_request_structure import SubscriptionRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionRequest(SubscriptionRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
