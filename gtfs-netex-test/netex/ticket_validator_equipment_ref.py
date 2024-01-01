from dataclasses import dataclass
from .ticket_validator_equipment_ref_structure import (
    TicketValidatorEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketValidatorEquipmentRef(TicketValidatorEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
