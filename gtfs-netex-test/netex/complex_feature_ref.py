from dataclasses import dataclass
from .complex_feature_ref_structure import ComplexFeatureRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureRef(ComplexFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"