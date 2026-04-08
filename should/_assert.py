import re

from ._util import assert_caught_error

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any, Iterable


class AssertValue:
  """A wrapper for the value to check.

  Attributes:
    value: Value to check.
  """

  def __init__(self, value: Any):
    self._value = value

  def be_like(self, pat: str | re.Pattern) -> "AssertValue":
    """Checks whether the value complies with a given pattern."""

    assert re.search(pat, v := self._value) is not None, f"'{v}' expected to be like '{pat}'."
    return self

  def not_be_like(self, pat: str | re.Pattern) -> "AssertValue":
    """Checks whether the value doesn't comply with a given pattern."""

    assert re.search(pat, v := self._value) is None, f"'{v}' expected not to be like '{pat}'."
    return self

  def be_instance_of(self, cls: type) -> "AssertValue":
    """Checks whether the value is an instance of the given type."""

    assert isinstance(v := self._value, cls), f"{v} expected to be instance of {cls}."
    return self

  def not_be_instance_of(self, cls: type) -> "AssertValue":
    """Checks whether the value is not an instance of the given type."""

    assert not isinstance(v := self._value, cls), f"{v} expected not to be instance of {cls}."
    return self

  def be_callable(self) -> "AssertValue":
    """Checks whether the value is callable."""

    assert callable(v := self._value), f"{v} expected to be callable."
    return self

  def not_be_callable(self) -> "AssertValue":
    """Checks whether the value is not callable."""

    assert not callable(v := self._value), f"{v} expected not to be callable."
    return self

  def be_true(self) -> "AssertValue":
    """Checks whether the value is true."""

    assert (v := self._value), f"{v} expected to be True."
    return self

  def be_false(self) -> "AssertValue":
    """Checks whether the value is true."""

    assert not (v := self._value), f"{v} expected to be False."
    return self

  def be_none(self) -> "AssertValue":
    """Checks whether the value is None."""

    assert (v := self._value) is None, f"{v} expected to be None."
    return self

  def not_be_none(self) -> "AssertValue":
    """Checks whether the value is not None."""

    assert (v := self._value) is not None, f"{v} expected not to be None."
    return self

  def be(self, o: Any) -> "AssertValue":
    """Checks whether the value is the same as another."""

    assert (v := self._value) is o, f"{v} expected to be {o}."
    return self

  def not_be(self, o: Any) -> "AssertValue":
    """Checks whether the value is not the same as another."""

    assert (v := self._value) is not o, f"{v} expected not to be {o}."
    return self

  def be_eq(self, o: Any) -> "AssertValue":
    """Checks whether the value is equal to another."""

    assert (v := self._value) == o, f"{v} expected to be equal to {o}."
    return self

  def not_be_eq(self, o: Any) -> "AssertValue":
    """Checks whether the value is not equal to another."""

    assert (v := self._value) != o, f"Expected {v} to be different."
    return self

  def be_lt(self, o: Any) -> "AssertValue":
    """Checks whether the value is less than another."""

    assert (v := self._value) < o, f"{v} expected to be less than {o}."
    return self

  def be_le(self, o: Any) -> "AssertValue":
    """Checks whether the value is less than or equal to another."""

    assert (v := self._value) <= o, f"{v} expected to be less than or equal to {o}."
    return self

  def be_gt(self, o: Any) -> "AssertValue":
    """Checks whether the value is greater than another."""

    assert (v := self._value) > o, f"{v} expected to be greater than {o}."
    return self

  def be_ge(self, o: Any) -> "AssertValue":
    """Checks whether the value is greater than o equal to another."""

    assert (v := self._value) >= o, f"{v} expected to be greater than or equal to {o}."
    return self

  def contain(self, o: Any) -> "AssertValue":
    """Checks whether the iterable value contains a given value."""

    assert o in (v := self._value), f"{v} expected to contain {o}."
    return self

  def not_contain(self, o: Any) -> "AssertValue":
    """Checks whether the iterable value doesn't contain a given value."""

    assert o not in (v := self._value), f"{v} expected not to contain {o}."
    return self

  def be_in(self, i: Iterable[Any]) -> "AssertValue":
    """Checks whether the value is in an iterable."""

    assert (v := self._value) in i, f"{v} expected to be in {i}."
    return self

  def not_be_in(self, i: Iterable[Any]) -> "AssertValue":
    """Checks whether the value is not in an iterable."""

    assert (v := self._value) not in i, f"{v} expected not to be in {i}."
    return self

  def have_len(self, size: int) -> "AssertValue":
    """Checks whether the value has a given length."""

    assert len(v := self._value) == size, f"{v} expected to have length {size}."
    return self

  def not_have_len(self, size: int) -> "AssertValue":
    """Checks whether the value has a given length."""

    assert len(v := self._value) != size, f"{v} expected not to have length {size}."
    return self

  def throw(self, E: type[Exception] = Exception, match: str | None = None) -> None:
    """Checks whether a function raises an error.

    Args:
      E: Exception class to be raised and caught.
      match: Pattern to comply the message.
    """

    # (1) pre
    if not callable(v := self._value):
      raise TypeError("should.throw() expects wrapped value to be callable.")

    # (2) call and assert
    try:
      v()
    except Exception as e:
      assert_caught_error(e, E, match)
    else:
      raise AssertionError(f"{v.__name__} expected to raise '{E}'. Nothing raised.")
