import re

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any


def assert_caught_error(e: Any, E: type[Exception], match: str | None = None) -> bool:
  """Asserts a caught error with the given info.

  Args:
    e: Exception instance caught.
    E: Exception type should be raised.
    match: Regular expression to assert.

  Returns:
    True if ok, only used by context manager.

  Raises:
    AssertionError: if assertion not complied.
  """

  # (1) assert
  assert issubclass(type(e), E), f"Expected error ({type(e)}) to be instance of {E}."

  if isinstance(match, str):
    assert re.search(match, str(e)) is not None, (
      f"Expected error message '{e}' to be like '{match}'."
    )

  # (2) return true for its usage in a context manager
  return True
