from dataclasses import dataclass
from .type_of_security_list_version_structure import (
    TypeOfSecurityListVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfSecurityList(TypeOfSecurityListVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
