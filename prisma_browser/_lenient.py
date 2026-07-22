"""Forward-compatible string/int enum base (injected by phantasos).

Generated enums are rebased onto these so values the live API returns that the spec
does not declare are accepted (as pseudo-members) instead of failing validation.
Pydantic v2 invokes Enum._missing_, so this works for model fields typed as the enum.
"""

import warnings
from enum import Enum

UNKNOWN_ENUM_VALUES: dict[str, set] = {}


def _record(cls, value):
    UNKNOWN_ENUM_VALUES.setdefault(cls.__name__, set()).add(value)
    warnings.warn(
        f"{cls.__name__}: value {value!r} is not defined in the OpenAPI spec; "
        f"passing it through (the SDK may be out of date)",
        stacklevel=4,
    )


class LenientStrEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            _record(cls, value)
            pseudo = str.__new__(cls, value)
            pseudo._name_ = value
            pseudo._value_ = value
            return pseudo
        return None


class LenientIntEnum(int, Enum):
    @classmethod
    def _missing_(cls, value):
        if isinstance(value, int) and not isinstance(value, bool):
            _record(cls, value)
            pseudo = int.__new__(cls, value)
            pseudo._name_ = str(value)
            pseudo._value_ = value
            return pseudo
        return None
