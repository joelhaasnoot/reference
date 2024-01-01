from dataclasses import dataclass, field
from typing import Optional
from .iana_country_tld_enumeration import IanaCountryTldEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CountryRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_principality: Optional[str] = field(
        default=None,
        metadata={
            "name": "refPrincipality",
            "type": "Attribute",
        },
    )
