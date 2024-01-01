from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_contract import FareContract
from .fare_contract_ref import FareContractRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareContracts_RelStructure"

    fare_contract_ref_or_fare_contract: List[
        Union[FareContractRef, FareContract]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareContractRef",
                    "type": FareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContract",
                    "type": FareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
