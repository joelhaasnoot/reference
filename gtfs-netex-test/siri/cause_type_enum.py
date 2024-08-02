from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class CauseTypeEnum(Enum):
    ACCIDENT = "accident"
    CONGESTION = "congestion"
    EARLIER_ACCIDENT = "earlierAccident"
    EARLIER_EVENT = "earlierEvent"
    EARLIER_INCIDENT = "earlierIncident"
    EQUIPMENT_FAILURE = "equipmentFailure"
    EXCESSIVE_HEAT = "excessiveHeat"
    FROST = "frost"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    INFRASTRUCTURE_FAILURE = "infrastructureFailure"
    LARGE_NUMBERS_OF_VISITORS = "largeNumbersOfVisitors"
    OBSTRUCTION = "obstruction"
    POLLUTION_ALERT = "pollutionAlert"
    POOR_WEATHER = "poorWeather"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOM_POST = "problemsAtCustomPost"
    PROBLEMS_ON_LOCAL_ROADS = "problemsOnLocalRoads"
    RADIOACTIVE_LEAK_ALERT = "radioactiveLeakAlert"
    ROADSIDE_EVENT = "roadsideEvent"
    RUBBER_NECKING = "rubberNecking"
    SECURITY_INCIDENT = "securityIncident"
    SHEAR_WEIGHT_OF_TRAFFIC = "shearWeightOfTraffic"
    TECHNICAL_PROBLEMS = "technicalProblems"
    TERRORISM = "terrorism"
    TOXIC_CLOUD_ALERT = "toxicCloudAlert"
    VANDALISM = "vandalism"
    OTHER = "other"
