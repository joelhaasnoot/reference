from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SharedUsageEnumeration(Enum):
    SINGLE_USER = "singleUser"
    CONCURRENT_USERS = "concurrentUsers"
    CONCURRENT_DESIGNATED_USERS = "concurrentDesignatedUsers"
