from dataclasses import dataclass
from .type_of_customer_account_version_structure import (
    TypeOfCustomerAccountVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCustomerAccount(TypeOfCustomerAccountVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
