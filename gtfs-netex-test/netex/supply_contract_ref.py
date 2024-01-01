from dataclasses import dataclass
from .supply_contract_ref_structure import SupplyContractRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplyContractRef(SupplyContractRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
