from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .child_seat_enumeration import ChildSeatEnumeration
from .multilingual_string import MultilingualString


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModelProfileVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleModelProfile_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_gears: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfGears",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    child_seat: Optional[ChildSeatEnumeration] = field(
        default=None,
        metadata={
            "name": "ChildSeat",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    range_between_refuelling: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RangeBetweenRefuelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_portable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPortable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
