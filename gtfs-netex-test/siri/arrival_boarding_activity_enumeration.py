from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ArrivalBoardingActivityEnumeration(Enum):
    ALIGHTING = "alighting"
    NO_ALIGHTING = "noAlighting"
    PASS_THRU = "passThru"
