from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfInfolinkEnumeration(Enum):
    CONTACT = "contact"
    RESOURCE = "resource"
    INFO = "info"
    IMAGE = "image"
    DOCUMENT = "document"
    TIMETABLE_DOCUMENT = "timetableDocument"
    FARE_SHEET = "fareSheet"
    DATA_LICENCE = "dataLicence"
    MOBILE_APP_DOWNLOAD = "mobileAppDownload"
    MOBILE_APP_INSTALL_CHECK = "mobileAppInstallCheck"
    MAP = "map"
    ICON = "icon"
    OTHER = "other"
