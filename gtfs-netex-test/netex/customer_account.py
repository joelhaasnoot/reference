from dataclasses import dataclass
from .customer_account_version_structure import CustomerAccountVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccount(CustomerAccountVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
