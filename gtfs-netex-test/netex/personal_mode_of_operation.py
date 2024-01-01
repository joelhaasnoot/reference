from dataclasses import dataclass
from .personal_mode_of_operation_value_structure import (
    PersonalModeOfOperationValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PersonalModeOfOperation(PersonalModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
