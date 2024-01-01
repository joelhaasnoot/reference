from dataclasses import dataclass
from .contextualised_request_structure import ContextualisedRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceRequestStructure(ContextualisedRequestStructure):
    pass
