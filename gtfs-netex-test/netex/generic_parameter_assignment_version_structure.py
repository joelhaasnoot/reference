from dataclasses import dataclass, field
from typing import List, Optional, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .logical_operation_enumeration import LogicalOperationEnumeration
from .validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    class Meta:
        name = "GenericParameterAssignment_VersionStructure"

    includes_grouping_type: Optional[LogicalOperationEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: Optional["GenericParameterAssignmentsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class GenericParameterAssignment(GenericParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericParameterAssignmentInContext(
    GenericParameterAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "genericParameterAssignments_RelStructure"

    generic_parameter_assignment_or_generic_parameter_assignment_in_context: List[
        Union[GenericParameterAssignment, GenericParameterAssignmentInContext]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )