from dataclasses import dataclass
from .restricted_manoeuvre_version_structure import (
    RestrictedManoeuvreVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedManoeuvre(RestrictedManoeuvreVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
