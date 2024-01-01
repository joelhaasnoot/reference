from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PyschosensoryNeedEnumeration(Enum):
    VISUAL_IMPAIRMENT = "visualImpairment"
    AUDITORY_IMPAIRMENT = "auditoryImpairment"
    COGNITIVE_INPUT_IMPAIRMENT = "cognitiveInputImpairment"
    AVERSE_TO_LIFTS = "averseToLifts"
    AVERSE_TO_ESCALATORS = "averseToEscalators"
    AVERSE_TO_CONFINED_SPACES = "averseToConfinedSpaces"
    AVERSE_TO_CROWDS = "averseToCrowds"
    OTHER_PSYCHOSENSORY_NEED = "otherPsychosensoryNeed"
