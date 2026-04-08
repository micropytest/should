from ._assert import AssertValue
from ._throw import AssertThrowContext

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any


class Should:
  def throw(self, E: type[Exception] = Exception, match: str | None = None) -> AssertThrowContext:
    return AssertThrowContext(E, match)

  def __call__(self, value: Any) -> "AssertValue":
    return AssertValue(value)
