from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .service_request_context_structure import ServiceRequestContextStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ContextualisedRequestStructure:
    service_request_context: Optional[ServiceRequestContextStructure] = field(
        default=None,
        metadata={
            "name": "ServiceRequestContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_timestamp: XmlDateTime = field(
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    account_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountId",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    account_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountKey",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: str = field(
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
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
