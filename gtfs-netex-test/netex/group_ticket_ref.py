from dataclasses import dataclass
from .group_ticket_ref_structure import GroupTicketRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupTicketRef(GroupTicketRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
