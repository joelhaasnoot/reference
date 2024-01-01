from dataclasses import dataclass
from .parameters_ignored_error_structure import ParametersIgnoredErrorStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ParametersIgnoredError(ParametersIgnoredErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
