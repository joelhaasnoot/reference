from dataclasses import dataclass, field
from typing import Optional
from .authenticated_request_structure import AuthenticatedRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProducerRequestEndpointStructure(AuthenticatedRequestStructure):
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
