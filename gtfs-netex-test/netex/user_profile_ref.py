from dataclasses import dataclass
from .user_profile_ref_structure import UserProfileRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileRef(UserProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
