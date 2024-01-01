from dataclasses import dataclass
from .unapproved_key_access_structure import UnapprovedKeyAccessStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnapprovedKeyAccessError(UnapprovedKeyAccessStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
