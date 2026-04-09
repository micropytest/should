from unittest import TestCase

from should import should
from should._assert import AssertItemValue
from should._should import AssertValue


class TestShould(TestCase):
  def test_be_like(self) -> None:
    """Check that should(v1).be_like(v2) returns the wrapper."""

    self.assertIsInstance(should("this is an assertion test").be_like("an assert"), AssertValue)

  def test_be_like_raises_error(self) -> None:
    """Check that should(v1).be_like(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should("this is an assertion test").be_like("the damned")

    self.assertEqual(
      str(out.exception),
      "'this is an assertion test' expected to be like 'the damned'.",
    )

  def test_not_be_like(self) -> None:
    """Check that should(v1).not_be_like(v2) returns the wrapper."""

    self.assertIsInstance(
      should("this is an assertion test").not_be_like("the godfathers"),
      AssertValue,
    )

  def test_not_be_like_raises_error(self) -> None:
    """Check that should(v1).not_be_like(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should("this is an assertion test").not_be_like("an assertion")

    self.assertEqual(
      str(out.exception),
      "'this is an assertion test' expected not to be like 'an assertion'.",
    )

  def test_be_instance_of(self) -> None:
    """Check that should(v1).be_instance_of(cls) returns the wrapper."""

    self.assertIsInstance(should(123).be_instance_of(int), AssertValue)

  def test_be_instance_of_raises_error(self) -> None:
    """Check that should(v1).be_instance_of(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_instance_of(str)

    self.assertEqual(str(out.exception), "123 expected to be instance of <class 'str'>.")

  def test_not_be_instance_of(self) -> None:
    """Check that should(v1).not_be_instance_of(cls) returns the wrapper."""

    self.assertIsInstance(should(123).not_be_instance_of(str), AssertValue)

  def test_not_be_instance_of_raises_error(self) -> None:
    """Check that should(v1).not_be_instance_of(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(123).not_be_instance_of(int)

    self.assertEqual(str(out.exception), "123 expected not to be instance of <class 'int'>.")

  def test_be_callable(self) -> None:
    """Check that should(v1).be_callable() returns the wrapper."""

    self.assertIsInstance(should(lambda: None).be_callable(), AssertValue)

  def test_be_callable_raises_error(self) -> None:
    """Check that should(v1).be_callable(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_callable()

    self.assertEqual(str(out.exception), "123 expected to be callable.")

  def test_not_be_callable(self) -> None:
    """Check that should(v1).not_be_callable() returns the wrapper."""

    self.assertIsInstance(should(123).not_be_callable(), AssertValue)

  def test_not_be_callable_raises_error(self) -> None:
    """Check that should(v1).not_be_callable(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(lambda: None).not_be_callable()

    self.assertTrue("expected not to be callable" in str(out.exception))

  def test_be_true(self) -> None:
    """Check that should(v1).be_true() returns the wrapper."""

    self.assertIsInstance(should(True).be_true(), AssertValue)

  def test_be_true_raises_error(self) -> None:
    """Check that should(v1).be_true() raises error."""

    with self.assertRaises(AssertionError) as out:
      should(False).be_true()

    self.assertEqual(str(out.exception), "False expected to be True.")

  def test_be_false(self) -> None:
    """Check that should(v1).be_false() returns the wrapper."""

    self.assertIsInstance(should(False).be_false(), AssertValue)

  def test_be_false_raises_error(self) -> None:
    """Check that should(v1).be_false() raises error."""

    with self.assertRaises(AssertionError) as out:
      should(True).be_false()

    self.assertEqual(str(out.exception), "True expected to be False.")

  def test_be_none(self) -> None:
    """Check that should(v1).be_none() returns the wrapper."""

    self.assertIsInstance(should(None).be_none(), AssertValue)

  def test_be_none_raises_error(self) -> None:
    """Check that should(v1).be_none() raises error."""

    with self.assertRaises(AssertionError) as out:
      should(True).be_none()

    self.assertEqual(str(out.exception), "True expected to be None.")

  def test_not_be_none(self) -> None:
    """Check that should(v1).not_be_none() returns the wrapper."""

    self.assertIsInstance(should("None").not_be_none(), AssertValue)

  def test_not_be_none_raises_error(self) -> None:
    """Check that should(v1).not_be_none() raises error."""

    with self.assertRaises(AssertionError) as out:
      should(None).not_be_none()

    self.assertEqual(str(out.exception), "None expected not to be None.")

  def test_be(self) -> None:
    """Check that should(v1).be(v2) returns the wrapper."""

    self.assertIsInstance(should(None).be(None), AssertValue)

  def test_be_raises_error(self) -> None:
    """Check that should(v1).be(v2) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(None).be("None")

    self.assertEqual(str(out.exception), "None expected to be None.")

  def test_not_be(self) -> None:
    """Check that should(v1).not_be(v2) returns the wrapper."""

    self.assertIsInstance(should(None).not_be("None"), AssertValue)

  def test_not_be_raises_error(self) -> None:
    """Check that should(v1).not_be(v2) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(None).not_be(None)

    self.assertEqual(str(out.exception), "None expected not to be None.")

  def test_be_eq(self) -> None:
    """Check that should(v1).be_eq(v2) returns the wrapper."""

    self.assertIsInstance(should(123).be_eq(123), AssertValue)

  def test_be_eq_raises_err(self) -> None:
    """Check that should(v1).be_eq(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_eq(321)

    self.assertEqual(str(out.exception), "123 expected to be equal to 321.")

  def test_not_be_eq(self) -> None:
    """Check that should(v1).not_be_eq(v2) returns the wrapper."""

    self.assertIsInstance(should(123).not_be_eq(321), AssertValue)

  def test_not_be_eq_raises_err(self) -> None:
    """Check that should(v1).not_be_eq(v2) raises error if equal."""

    with self.assertRaises(AssertionError) as out:
      should(123).not_be_eq(123)

    self.assertEqual(str(out.exception), "Expected 123 to be different.")

  def test_be_lt(self) -> None:
    """Check that should(v1).be_lt(v2) returns the wrapper."""

    self.assertIsInstance(should(123).be_lt(124), AssertValue)

  def test_be_lt_raises_err(self) -> None:
    """Check that should(v1).be_lt(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_lt(123)

    self.assertEqual(str(out.exception), "123 expected to be less than 123.")

  def test_be_le(self) -> None:
    """Check that should(v1).be_le(v2) returns the wrapper."""

    self.assertIsInstance(should(123).be_le(123), AssertValue)

  def test_be_le_raises_err(self) -> None:
    """Check that should(v1).be_le(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_le(122)

    self.assertEqual(str(out.exception), "123 expected to be less than or equal to 122.")

  def test_be_gt(self) -> None:
    """Check that should(v1).be_gt(v2) returns the wrapper."""

    self.assertIsInstance(should(123).be_gt(122), AssertValue)

  def test_be_gt_raises_err(self) -> None:
    """Check that should(v1).be_gt(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_gt(123)

    self.assertEqual(str(out.exception), "123 expected to be greater than 123.")

  def test_be_ge(self) -> None:
    """Check that should(v1).be_ge(v2) returns the wrapper."""

    self.assertIsInstance(should(123).be_ge(123), AssertValue)

  def test_be_ge_raises_err(self) -> None:
    """Check that should(v1).be_ge(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(123).be_ge(124)

    self.assertEqual(str(out.exception), "123 expected to be greater than or equal to 124.")

  def test_contain(self) -> None:
    """Check that should(v1).contain(v2) returns the wrapper."""

    self.assertIsInstance(should([12, 34, 56]).contain(34), AssertValue)

  def test_contain_raises_err(self) -> None:
    """Check that should(v1).contain(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should("123").contain("4")

    self.assertEqual(str(out.exception), "123 expected to contain 4.")

  def test_not_contain(self) -> None:
    """Check that should(v1).not_contain(v2) returns the wrapper."""

    self.assertIsInstance(should([12, 34, 56]).not_contain(123456), AssertValue)

  def test_not_contain_raises_err(self) -> None:
    """Check that should(v1).not_contain(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should("123").not_contain("2")

    self.assertEqual(str(out.exception), "123 expected not to contain 2.")

  def test_be_in(self) -> None:
    """Check that should(v1).be_in(v2) returns the wrapper."""

    self.assertIsInstance(should(34).be_in([12, 34, 56]), AssertValue)

  def test_be_in_raises_err(self) -> None:
    """Check that should(v1).be_in(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should("123").be_in("4")

    self.assertEqual(str(out.exception), "123 expected to be in 4.")

  def test_not_be_in(self) -> None:
    """Check that should(v1).not_be_io(v2) returns the wrapper."""

    self.assertIsInstance(should("xx").not_be_in("123456"), AssertValue)

  def test_not_be_in_raises_err(self) -> None:
    """Check that should(v1).not_be_in(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should("2").not_be_in("123")

    self.assertEqual(str(out.exception), "2 expected not to be in 123.")

  def test_have_len(self) -> None:
    """Check that should(v1).have_len(v2) returns the wrapper."""

    self.assertIsInstance(should([12, 34, 56]).have_len(3), AssertValue)

  def test_have_len_raises_err(self) -> None:
    """Check that should(v1).have_len(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should("123").have_len(4)

    self.assertEqual(str(out.exception), "123 expected to have length 4.")

  def test_not_have_len(self) -> None:
    """Check that should(v1).not_have_len(v2) returns the wrapper."""

    self.assertIsInstance(should([12, 34, 56]).not_have_len(2), AssertValue)

  def test_not_have_len_raises_err(self) -> None:
    """Check that should(v1).not_have_len(v2) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should("123").not_have_len(3)

    self.assertEqual(str(out.exception), "123 expected not to have length 3.")

  def test_have(self) -> None:
    """Check that should(v).have("item") returns a wrapper."""

    self.assertIsInstance(should(dict(x=12, y=34)).have("x"), AssertItemValue)

  def test_have_raises_err(self) -> None:
    """Check that should(v).have("item") raises error if item not existing."""

    with self.assertRaises(AssertionError) as out:
      should(dict()).have("x")

    self.assertEqual(str(out.exception), "{} expected to have item 'x'.")

  def test_not_have(self) -> None:
    """Check that should(v).not_have("item") if not existing."""

    should(dict()).not_have("x")

  def test_not_have_raises_err(self) -> None:
    """Check that should(v).not_have("iem") raises error if existing."""

    with self.assertRaises(AssertionError) as out:
      should(dict(x=12)).not_have("x")

    self.assertEqual(str(out.exception), "{'x': 12} expected not to have item 'x'.")
