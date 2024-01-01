from dataclasses import dataclass
from .fare_table_ref_structure import FareTableRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRefStructure(FareTableRefStructure):
    value: RestrictedVar
