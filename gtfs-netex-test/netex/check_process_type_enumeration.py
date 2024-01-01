from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckProcessTypeEnumeration(Enum):
    NONE = "none"
    UNKNOWN = "unknown"
    BOARDING = "boarding"
    ALIGHTING = "alighting"
    TICKET_PURCHASE = "ticketPurchase"
    TICKET_COLLECTION = "ticketCollection"
    TICKET_VALIDATION = "ticketValidation"
    BAGGAGE_CHECK_IN = "baggageCheckIn"
    CHECKOUT = "checkout"
    OVERSIZE_BAGGAGE_CHECK_IN = "oversizeBaggageCheckIn"
    OVERSIZE_BAGGAGE_RECLAIM = "oversizeBaggageReclaim"
    BAGGAGE_RECLAIM = "baggageReclaim"
    LEFT_LUGGAGE_DEPOSIT = "leftLuggageDeposit"
    LEFT_LUGGAGE_RECLAIM = "leftLuggageReclaim"
    FIRSTCLASS_CHECKIN = "firstclassCheckin"
    SPECIAL_NEEDS_CHECKIN = "specialNeedsCheckin"
    BAGGAGE_SECURITY_CHECK = "baggageSecurityCheck"
    SECURITY_CHECK = "securityCheck"
    OUTGOING_PASSPORT_CONTROL = "outgoingPassportControl"
    INCOMING_PASSPORT_CONTROL = "incomingPassportControl"
    FASTTRACK_DEPARTURES = "fasttrackDepartures"
    FASTTRACK_ARRIVALS = "fasttrackArrivals"
    INCOMING_DUTY_FREE = "incomingDutyFree"
    OUTGOING_DUTY_FREE = "outgoingDutyFree"
    TAX_REFUNDS = "taxRefunds"
    OUTGOING_CUSTOMS = "outgoingCustoms"
    INCOMING_CUSTOMS = "incomingCustoms"
    WAIT_FOR_LIFT = "waitForLift"
    INGRESS = "ingress"
    EGRESS = "egress"
    QUEUE = "queue"
    VEHICLE_LOADING = "vehicleLoading"
    VEHICLE_UNLOADING = "vehicleUnloading"
    OTHER = "other"
