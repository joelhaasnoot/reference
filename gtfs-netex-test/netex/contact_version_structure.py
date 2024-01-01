from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .contact_details_structure import ContactDetailsStructure
from .contact_type_enumeration import ContactTypeEnumeration
from .multilingual_string import MultilingualString


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContactVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Contact_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_details: Optional[ContactDetailsStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_type: Optional[ContactTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ContactType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )