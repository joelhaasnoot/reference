from dataclasses import dataclass, field
from typing import Optional
from .department_ref import DepartmentRef
from .organisation_part_version_structure import (
    OrganisationPartVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnitVersionStructure(OrganisationPartVersionStructure):
    class Meta:
        name = "OrganisationalUnit_VersionStructure"

    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
