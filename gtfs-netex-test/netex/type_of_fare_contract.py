from dataclasses import dataclass
from .type_of_fare_contract_version_structure import (
    TypeOfFareContractVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareContract(TypeOfFareContractVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"