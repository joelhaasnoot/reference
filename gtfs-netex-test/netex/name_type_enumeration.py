from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NameTypeEnumeration(Enum):
    ALIAS = "alias"
    TRANSLATION = "translation"
    COPY = "copy"
    LABEL = "label"
    OTHER = "other"