from dataclasses import dataclass
from .department_ref_structure import DepartmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DepartmentRef(DepartmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
