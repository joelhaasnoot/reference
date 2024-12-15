import warnings
from typing import T, Generator
from xsdata.models.datatype import XmlDateTime, XmlDuration

def get_object_name(clazz: T) -> str:
    return getattr(clazz.Meta, 'name', clazz.__name__)

def get_element_name_with_ns(clazz):
    name = get_object_name(clazz)
    return "{" + clazz.Meta.namespace + "}" + name

def project(obj, clazz: T) -> T:
    # if issubclass(obj.__class__, clazz_intermediate):
    attributes = {x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())}
    if 'id' in attributes:
        attributes['id'] = attributes['id'].replace(f":{get_object_name(obj.__class__)}:", f":{get_object_name(clazz)}:")
    # return clazz({x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())})
    return clazz(**attributes)

def to_seconds(xml_duration: XmlDuration):
    if xml_duration.months is not None and xml_duration.months > 0:
        warnings.warn("Duration is bigger than a month!")
    return (((xml_duration.days or 0) * 24 + (xml_duration.hours or 0)) * 3600) + ((xml_duration.minutes or 0) * 60) + (xml_duration.seconds or 0)

def dontsetifnone(clazz, attr, value):
    if value is None:
        return None

    try:
        first = value.__next__()
    except StopIteration:
        return None
    else:
        return clazz(**{attr: chain([first],value)})

def chain(*iterables) -> Generator:
    for it in iterables:
        for element in it:
            yield element

class GeneratorTester:
    def __init__(self, value):
        self._has_value = None
        self.value = value

    def has_value(self) -> bool:
        if self._has_value is not None:
            return self._has_value

        try:
            self.first = self.value.__next__()
            self._has_value = True
        except StopIteration:
            self._has_value = False
            pass

        return self._has_value

    def generator(self) -> Generator | None:
        if self._has_value is None:
            return self.value

        elif self._has_value:
            return chain([self.first], self.value)

        return None
