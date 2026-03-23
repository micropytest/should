TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any

from ._should import AssertValue

__all__ = [
  "should",
]


def should(v: Any = None) -> AssertValue:
  """Creates a wrapper for performing assertions.

  Args:
    v: Value to apply the assertions.
  """

  return AssertValue(v)
