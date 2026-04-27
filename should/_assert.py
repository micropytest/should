import re

from ._util import assert_caught_error
from ._wrapper import Wrapper

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any, Iterable


class AssertValue(Wrapper):
  """A wrapper for a value to check."""

  def be_json(self) -> "AssertValue":
    """Checks whether the value is a valid JSON string."""

    return self._json()  # type: ignore

  def be_like(self, pat: str | re.Pattern) -> "AssertValue":
    """Checks whether the value complies with a given pattern."""

    return self._like(pat)  # type: ignore

  def not_be_like(self, pat: str | re.Pattern) -> "AssertValue":
    """Checks whether the value doesn't comply with a given pattern."""

    return self._not_like(pat)  # type: ignore

  def start_with(self, prefix: str) -> "AssertValue":
    """Checks whether the value starts with a given prefix."""

    return self._start_with(prefix)  # type: ignore

  def end_with(self, suffix: str) -> "AssertValue":
    """Checks whether the value ends with a given suffix."""

    return self._end_with(suffix)  # type: ignore

  def be_instance_of(self, cls: type) -> "AssertValue":
    """Checks whether the value is an instance of the given type."""

    return self._instance_of(cls)  # type: ignore

  def not_be_instance_of(self, cls: type) -> "AssertValue":
    """Checks whether the value is not an instance of the given type."""

    return self._not_instance_of(cls)  # type: ignore

  def be_class(self) -> "AssertValue":
    """Checks whether the value is a class object."""

    return self._isclass()  # type:ignore

  def be_callable(self) -> "AssertValue":
    """Checks whether the value is callable."""

    return self._callable()  # type: ignore

  def not_be_callable(self) -> "AssertValue":
    """Checks whether the value is not callable."""

    return self._not_callable()  # type: ignore

  def be_true(self) -> "AssertValue":
    """Checks whether the value is true."""

    return self._true()  # type: ignore

  def be_false(self) -> "AssertValue":
    """Checks whether the value is false."""

    return self._false()  # type: ignore

  def be_none(self) -> "AssertValue":
    """Checks whether the value is None."""

    return self._none()  # type: ignore

  def not_be_none(self) -> "AssertValue":
    """Checks whether the value is not None."""

    return self._not_none()  # type: ignore

  def be(self, o: Any) -> "AssertValue":
    """Checks whether the value is the same as another."""

    return self._same_as(o)  # type: ignore

  def not_be(self, o: Any) -> "AssertValue":
    """Checks whether the value is not the same as another."""

    return self._not_same_as(o)  # type: ignore

  def be_eq(self, o: Any) -> "AssertValue":
    """Checks whether the value is equal to another."""

    return self._eq(o)  # type: ignore

  def not_be_eq(self, o: Any) -> "AssertValue":
    """Checks whether the value is not equal to another."""

    return self._not_eq(o)  # type: ignore

  def be_lt(self, o: Any) -> "AssertValue":
    """Checks whether the value is less than another."""

    return self._lt(o)  # type: ignore

  def be_le(self, o: Any) -> "AssertValue":
    """Checks whether the value is less than or equal to another."""

    return self._le(o)  # type: ignore

  def be_gt(self, o: Any) -> "AssertValue":
    """Checks whether the value is greater than another."""

    return self._gt(o)  # type: ignore

  def be_ge(self, o: Any) -> "AssertValue":
    """Checks whether the value is greater than o equal to another."""

    return self._ge(o)  # type: ignore

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

    return self._in(i)  # type: ignore

  def not_be_in(self, i: Iterable[Any]) -> "AssertValue":
    """Checks whether the value is not in an iterable."""

    return self._not_in(i)  # type: ignore

  def have(self, name: str) -> "AssertItemValue":
    """Check whether the value has a given item."""

    assert name in (v := self._value), f"{v} expected to have item '{name}'."
    return AssertItemValue(v[name])

  def not_have(self, name: str) -> "AssertValue":
    """Check whether the value has a given item."""

    assert name not in (v := self._value), f"{v} expected not to have item '{name}'."
    return self

  def have_len(self, size: int) -> "AssertValue":
    """Checks whether the value has a given length."""

    return self._len(size)  # type: ignore

  def not_have_len(self, size: int) -> "AssertValue":
    """Checks whether the value does not have a given length."""

    return self._not_len(size)  # type: ignore

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
      raise AssertionError(
        f"{getattr(v, '__name__', str(v))} expected to raise '{getattr(E, '__name__', str(E))}'. Nothing raised."
      )


class AssertItemValue(Wrapper):
  """A wrapper for the value to check."""

  def like(self, pat: str | re.Pattern) -> "AssertItemValue":
    """Checks whether the value complies with a given pattern."""

    return self._like(pat)  # type: ignore

  def not_like(self, pat: str | re.Pattern) -> "AssertItemValue":
    """Checks whether the value doesn't comply with a given pattern."""

    return self._not_like(pat)  # type: ignore

  def instance_of(self, cls: type) -> "AssertItemValue":
    """Checks whether the value is an instance of the given type."""

    return self._instance_of(cls)  # type: ignore

  def not_instance_of(self, cls: type) -> "AssertItemValue":
    """Checks whether the value is not an instance of the given type."""

    return self._not_instance_of(cls)  # type: ignore

  def to_true(self) -> "AssertItemValue":
    """Checks whether the value is true."""

    return self._true()  # type: ignore

  def to_false(self) -> "AssertItemValue":
    """Checks whether the value is false."""

    return self._false()  # type: ignore

  def same_as(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is the same as another."""

    return self._same_as(o)  # type: ignore

  def not_same_as(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is not the same as another."""

    return self._not_same_as(o)  # type: ignore

  def len(self, size: int) -> "AssertItemValue":
    """Checks whether the value has a given length."""

    return self._len(size)  # type: ignore

  def eq(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is equal to another."""

    return self._eq(o)  # type: ignore

  def not_eq(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is not equal to another."""

    return self._not_eq(o)  # type: ignore

  def lt(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is less than another."""

    return self._lt(o)  # type: ignore

  def le(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is less than or equal to another."""

    return self._le(o)  # type: ignore

  def gt(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is greater than another."""

    return self._gt(o)  # type: ignore

  def ge(self, o: Any) -> "AssertItemValue":
    """Checks whether the value is greater than o equal to another."""

    return self._ge(o)  # type: ignore

  def included_in(self, i: Iterable[Any]) -> "AssertItemValue":
    """Checks whether the value is in an iterable."""

    return self._in(i)  # type: ignore

  def not_in(self, i: Iterable[Any]) -> "AssertItemValue":
    """Checks whether the value is not in an iterable."""

    return self._not_in(i)  # type: ignore
