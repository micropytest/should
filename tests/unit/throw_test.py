from unittest import TestCase

from should import should


class TestShouldThrowWithContextManager(TestCase):
  def test_throw_without_exc_cls(self) -> None:
    """Check that should.throw() doesn't raise error."""

    with should.throw() as out:
      raise ValueError("This is a test.")

    self.assertIsInstance(out := out.exception, ValueError)
    self.assertEqual(str(out), "This is a test.")

  def test_throw_with_exc_cls(self) -> None:
    """Check that should.throw(cls) doesn't raise error."""

    with should.throw(ValueError) as out:
      raise ValueError("This is a test.")

    self.assertIsInstance(out := out.e, ValueError)
    self.assertEqual(str(out), "This is a test.")

  def test_throw_raises_error_due_to_nothing_raised(self) -> None:
    """Check that should.throw() raises error if nothing raised."""

    with self.assertRaises(AssertionError) as out:
      with should.throw():
        pass

    self.assertEqual(str(out.exception), "Expected <class 'Exception'> to be raised.")

  def test_throw_raises_error_due_to_other_exc(self) -> None:
    """Check that should.throw() raises error if other exception raised."""

    with self.assertRaises(AssertionError):
      with should.throw(OSError):
        raise ValueError("Other exception")

  def test_throw_raises_error_due_to_other_exc_msg(self) -> None:
    """Check that should.throw() raises error if exception raised with other message."""

    with self.assertRaises(AssertionError):
      with should.throw(ValueError, "xxx"):
        raise ValueError("Other exception")


class TestShouldThrow(TestCase):
  @staticmethod
  def raise_value_error() -> None:
    raise ValueError("This is a test.")

  def test_throw_raises_error_due_to_not_callable(self) -> None:
    """Check that should(value).throw() raises error due to not callable."""

    with self.assertRaises(TypeError) as out:
      should(123).throw()

    self.assertEqual(str(out.exception), "should.throw() expects wrapped value to be callable.")

  def test_throw_without_exc_cls(self) -> None:
    """Check that should(fn).throw() doesn't raise error."""

    should(self.raise_value_error).throw()

  def test_throw_with_exc_class(self) -> None:
    """Check that should(fn),throw() doesn't raise error."""

    should(self.raise_value_error).throw(ValueError)

  def test_throw_raises_error_due_to_nothing_raised(self) -> None:
    """Check that should(fn).throw() raises error if nothing raised."""

    with self.assertRaises(AssertionError) as out:
      should(lambda: None).throw()

    self.assertEqual(
      str(out.exception),
      "<lambda> expected to raise '<class 'Exception'>'. Nothing raised.",
    )

  def test_throw_raises_error_due_to_other_exc(self) -> None:
    """Check that should(fn).throw(E) raises error if other exception raised."""

    with self.assertRaises(AssertionError) as out:
      should(self.raise_value_error).throw(OSError)

    self.assertEqual(
      str(out.exception),
      "Expected error (<class 'ValueError'>) to be instance of <class 'OSError'>.",
    )

  def test_throw_raises_error_due_to_other_exc_msg(self) -> None:
    """Check that should(fn).throw(E, msg) raises error if exception raised with other message."""

    with self.assertRaises(AssertionError) as out:
      should(self.raise_value_error).throw(ValueError, "xxx")

    self.assertEqual(
      str(out.exception),
      "Expected error message 'This is a test.' to be like 'xxx'.",
    )
