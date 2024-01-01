from dataclasses import dataclass
from .conventional_mode_of_operation_ref_structure import (
    ConventionalModeOfOperationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleModeOfOperationRefStructure(
    ConventionalModeOfOperationRefStructure
):
    value: RestrictedVar
