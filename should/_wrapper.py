import inspect
import json
import re
from abc import ABC

from ._util import fmt

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any, Iterable


class Wrapper(ABC):
  """Base for the wrappers.

  Attributes:
    value: Value wrapped to check.
  """

  def __init__(self, value: Any):
    self._value = value

  def _json(self) -> "Wrapper":
    """Checks whether the value is a valid JSON."""

    try:
      assert json.loads(self._value)
      return self
    except:
      raise AssertionError(f"{fmt(self._value)} expected to be a valid JSON string.")

  def _like(self, pat: str | re.Pattern) -> "Wrapper":
    """Checks whether the value complies with a given pattern."""

    assert re.search(pat, v := self._value) is not None, f"{fmt(v)} expected to be like {pat!r}."
    return self

  def _not_like(self, pat: str | re.Pattern) -> "Wrapper":
    """Checks whether the value doesn't comply with a given pattern."""

    assert re.search(pat, v := self._value) is None, f"{fmt(v)} expected not to be like {pat!r}."
    return self

  def _start_with(self, prefix: str) -> "Wrapper":
    """Checks whether the value starts with a given prefix."""

    self._instance_of(str)
    assert (v := self._value).startswith(prefix), f"{fmt(v)} expected to start with {prefix!r}."
    return self

  def _end_with(self, suffix: str) -> "Wrapper":
    """Checks whether the value ends with a given suffix."""

    self._instance_of(str)
    assert (v := self._value).endswith(suffix), f"{fmt(v)} expected to end with {suffix!r}."
    return self

  def _instance_of(self, cls: type | str) -> "Wrapper":
    """Checks whether the value is an instance of the given type."""

    if isinstance(cls, str):
      assert type(v := self._value).__name__ == cls, f"{fmt(v)} expected to be instance of {cls}."
    else:
      assert isinstance(v := self._value, cls), (
        f"{fmt(v)} expected to be instance of {cls.__name__}."
      )

    return self

  def _not_instance_of(self, cls: type | str) -> "Wrapper":
    """Checks whether the value is not an instance of the given type."""

    if isinstance(cls, str):
      assert type(v := self._value).__name__ != cls, (
        f"{fmt(v)} expected not to be instance of {cls}."
      )
    else:
      assert not isinstance(v := self._value, cls), (
        f"{fmt(v)} expected not to be instance of {cls.__name__}."
      )

    return self

  def _isclass(self) -> "Wrapper":
    """Checks whether the value is a class object."""

    assert inspect.isclass(v := self._value), f"{fmt(v)} expected to be a class object."
    return self

  def _is_fn(self) -> "Wrapper":
    """Checks that the value is a function object."""

    assert inspect.isfunction(v := self._value), f"{fmt(v)} expected to be a function object."
    return self

  def _is_async_fn(self) -> "Wrapper":
    """Checks that the value is an async/coroutine function object."""

    assert inspect.iscoroutinefunction(v := self._value), (
      f"{fmt(v)} expected to be an async/coroutine function object."
    )
    return self

  _is_coro_fn = _is_async_fn

  def _is_coro(self) -> "Wrapper":
    """Checks that the value is a coroutine."""

    assert inspect.iscoroutine(v := self._value), f"{fmt(v)} expected to be a coroutine."
    return self

  def _callable(self) -> "Wrapper":
    """Checks whether the value is callable."""

    assert callable(v := self._value), f"{fmt(v)} expected to be callable."
    return self

  def _not_callable(self) -> "Wrapper":
    """Checks whether the value is not callable."""

    assert not callable(v := self._value), f"{fmt(v)} expected not to be callable."
    return self

  def _true(self) -> "Wrapper":
    """Checks whether the value is true."""

    assert (v := self._value), f"{fmt(v)} expected to be True."
    return self

  def _false(self) -> "Wrapper":
    """Checks whether the value is false."""

    assert not (v := self._value), f"{fmt(v)} expected to be False."
    return self

  def _none(self) -> "Wrapper":
    """Checks whether the value is None."""

    assert (v := self._value) is None, f"{fmt(v)} expected to be None."
    return self

  def _not_none(self) -> "Wrapper":
    """Checks whether the value is not None."""

    assert (v := self._value) is not None, f"{fmt(v)} expected not to be None."
    return self

  def _same_as(self, o: Any) -> "Wrapper":
    """Checks whether the value is the same as another."""

    assert (v := self._value) is o, f"{fmt(v)} expected to be {o}."
    return self

  def _not_same_as(self, o: Any) -> "Wrapper":
    """Checks whether the value is not the same as another."""

    assert (v := self._value) is not o, f"{fmt(v)} expected not to be {o!r}."
    return self

  def _eq(self, o: Any) -> "Wrapper":
    """Checks whether the value is equal to another."""

    assert (v := self._value) == o, f"{fmt(v)} expected to be equal to {o!r}."
    return self

  def _not_eq(self, o: Any) -> "Wrapper":
    """Checks whether the value is not equal to another."""

    assert (v := self._value) != o, f"Expected {fmt(v)} to be different."
    return self

  def _lt(self, o: Any) -> "Wrapper":
    """Checks whether the value is less than another."""

    assert (v := self._value) < o, f"{fmt(v)} expected to be less than {o!r}."
    return self

  def _le(self, o: Any) -> "Wrapper":
    """Checks whether the value is less than or equal to another."""

    assert (v := self._value) <= o, f"{fmt(v)} expected to be less than or equal to {o!r}."
    return self

  def _gt(self, o: Any) -> "Wrapper":
    """Checks whether the value is greater than another."""

    assert (v := self._value) > o, f"{fmt(v)} expected to be greater than {o!r}."
    return self

  def _ge(self, o: Any) -> "Wrapper":
    """Checks whether the value is greater than o equal to another."""

    assert (v := self._value) >= o, f"{fmt(v)} expected to be greater than or equal to {o!r}."
    return self

  def _in(self, i: Iterable[Any]) -> "Wrapper":
    """Checks whether the value is in an iterable."""

    assert (v := self._value) in i, f"{fmt(v)} expected to be in {i!r}."
    return self

  def _not_in(self, i: Iterable[Any]) -> "Wrapper":
    """Checks whether the value is not in an iterable."""

    assert (v := self._value) not in i, f"{fmt(v)} expected not to be in {i!r}."
    return self

  def _empty(self) -> "Wrapper":
    """Asserts the value is empty."""

    assert len(v := self._value) == 0, f"{fmt(v)} expected to have length 0."
    return self

  def _not_empty(self) -> "Wrapper":
    """Asserts the value is not empty."""

    assert len(v := self._value) != 0, f"{fmt(v)} expected to have length greater than 0."
    return self

  def _len(self, size: int) -> "Wrapper":
    """Checks whether the value has a given length."""

    assert len(v := self._value) == size, f"{fmt(v)} expected to have length {size!r}."
    return self

  def _not_len(self, size: int) -> "Wrapper":
    """Checks whether the value does not have a given length."""

    assert len(v := self._value) != size, f"{fmt(v)} expected not to have length {size!r}."
    return self
