from dataclasses import dataclass
from .type_of_service_feature_value_structure import (
    TypeOfServiceFeatureValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfServiceFeature(TypeOfServiceFeatureValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
