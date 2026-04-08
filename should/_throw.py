from ._util import assert_caught_error


class AssertThrowContext:
  """Context for throw().

  Attributes:
    E: Exception class expected to be raised.
    match: Message match to assert.
    e: Exception raised and caught.
  """

  @property
  def exception(self) -> Exception | None:
    """Alias for self.e."""

    return self.e

  def __init__(self, E: type[Exception], match: str | None = None):
    self.E = E
    self.match = match
    self.e = None

  def __enter__(self):
    return self

  def __exit__(self, cls, value, tb):
    # (1) pre: something raised?
    if cls is None:
      assert False, f"Expected {self.E} to be raised."

    # (2) assert
    self.e = value
    return assert_caught_error(self.e, self.E, self.match)
