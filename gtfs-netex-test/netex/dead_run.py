from dataclasses import dataclass
from .dead_run_with_calls_version_structure import (
    DeadRunWithCallsVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRun(DeadRunWithCallsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
