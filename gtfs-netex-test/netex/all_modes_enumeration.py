from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AllModesEnumeration(Enum):
    ALL = "all"
    ANY_MODE = "anyMode"
    UNKNOWN = "unknown"
    AIR = "air"
    BUS = "bus"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    COACH = "coach"
    RAIL = "rail"
    INTERCITY_RAIL = "intercityRail"
    URBAN_RAIL = "urbanRail"
    METRO = "metro"
    WATER = "water"
    FERRY = "ferry"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    LIFT = "lift"
    SNOW_AND_ICE = "snowAndIce"
    TAXI = "taxi"
    SELF_DRIVE = "selfDrive"
    FOOT = "foot"
    BICYCLE = "bicycle"
    MOTORCYCLE = "motorcycle"
    SCOOTER = "scooter"
    CAR = "car"
    SHUTTLE = "shuttle"
