from dataclasses import dataclass
from .compound_train_ref_structure import CompoundTrainRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrainRef(CompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
