from dataclasses import dataclass
from .mode_restriction_assessment_version_structure import (
    ModeRestrictionAssessmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRestrictionAssessment(ModeRestrictionAssessmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
