from unittest import TestCase

from should import should
from should._assert import AssertItemValue

v = dict(x=12, y=34, z="1234", t=True, f=False)


class TestShouldItem(TestCase):
  def test_like(self) -> None:
    """Check that should(v).have(i).like(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("z").like("23"), AssertItemValue)

  def test_like_raises_error(self) -> None:
    """Check that should(v).have(i).like(v) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("z").like("the damned")

    self.assertEqual(str(out.exception), "'1234' expected to be like 'the damned'.")

  def test_not_like(self) -> None:
    """Check that should(v).have(i).not_like(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("z").not_like("the godfathers"), AssertItemValue)

  def test_not_like_raises_error(self) -> None:
    """Check that should(v).have(i).not_like(v) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("z").not_like("23")

    self.assertEqual(str(out.exception), "'1234' expected not to be like '23'.")

  def test_instance_of(self) -> None:
    """Check that should(v).have(i).instance_of(cls) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").instance_of(int), AssertItemValue)

  def test_instance_of_raises_error(self) -> None:
    """Check that should(v).have(i).instance_of(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").instance_of(str)

    self.assertEqual(str(out.exception), "12 expected to be instance of <class 'str'>.")

  def test_not_be_instance_of(self) -> None:
    """Check that should(v).have(i).not_instance_of(cls) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").not_instance_of(str), AssertItemValue)

  def test_not_instance_of_raises_error(self) -> None:
    """Check that should(v).have(i).not_instance_of(cls) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").not_instance_of(int)

    self.assertEqual(str(out.exception), "12 expected not to be instance of <class 'int'>.")

  def test_to_true(self) -> None:
    """Check that should(v).have(i).to_true() returns the wrapper."""

    self.assertIsInstance(should(v).have("t").to_true(), AssertItemValue)

  def test_to_true_raises_error(self) -> None:
    """Check that should(v).have(i).to_true() raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("f").to_true()

    self.assertEqual(str(out.exception), "False expected to be True.")

  def test_to_false(self) -> None:
    """Check that should(v).have(i).to_false() returns the wrapper."""

    self.assertIsInstance(should(v).have("f").to_false(), AssertItemValue)

  def test_to_false_raises_error(self) -> None:
    """Check that should(v).have(i).to_false() raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("t").to_false()

    self.assertEqual(str(out.exception), "True expected to be False.")

  def test_same_as(self) -> None:
    """Check that should(v).have(i).same_as(v2) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").same_as(12), AssertItemValue)

  def test_same_as_raises_error(self) -> None:
    """Check that should(v).have(i).same_as(v2) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").same_as("None")

    self.assertEqual(str(out.exception), "12 expected to be None.")

  def test_not_same_as(self) -> None:
    """Check that should(v).have(i).not_same_as(v2) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").not_same_as("None"), AssertItemValue)

  def test_not_same_as_raises_error(self) -> None:
    """Check that should(v).have(i).not_same_as(v2) raises error."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").not_same_as(12)

    self.assertEqual(str(out.exception), "12 expected not to be 12.")

  def test_eq(self) -> None:
    """Check that should(v).have(i).eq(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").eq(12), AssertItemValue)

  def test_eq_raises_err(self) -> None:
    """Check that should(v).have(i).eq(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").eq(34)

    self.assertEqual(str(out.exception), "12 expected to be equal to 34.")

  def test_not_eq(self) -> None:
    """Check that should(v).have(i).not_eq(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").not_eq(34), AssertItemValue)

  def test_not_eq_raises_err(self) -> None:
    """Check that should(v).have(i).not_eq(v) raises error if equal."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").not_eq(12)

    self.assertEqual(str(out.exception), "Expected 12 to be different.")

  def test_lt(self) -> None:
    """Check that should(v).have(i).lt(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").lt(1111), AssertItemValue)

  def test_lt_raises_err(self) -> None:
    """Check that should(v).have(i).lt(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").lt(11)

    self.assertEqual(str(out.exception), "12 expected to be less than 11.")

  def test_le(self) -> None:
    """Check that should(v).have(i).le(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").le(123), AssertItemValue)

  def test_le_raises_err(self) -> None:
    """Check that should(v).have(i).le(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").le(11)

    self.assertEqual(str(out.exception), "12 expected to be less than or equal to 11.")

  def test_gt(self) -> None:
    """Check that should(v).have(i).gt(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").gt(0), AssertItemValue)

  def test_gt_raises_err(self) -> None:
    """Check that should(v).have(i).gt(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").gt(123)

    self.assertEqual(str(out.exception), "12 expected to be greater than 123.")

  def test_ge(self) -> None:
    """Check that should(v).have(i).ge(v2) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").ge(0), AssertItemValue)

  def test_ge_raises_err(self) -> None:
    """Check that should(v).have(i).ge(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").ge(124)

    self.assertEqual(str(out.exception), "12 expected to be greater than or equal to 124.")

  def test_len(self) -> None:
    """Check that should(v).have(i).len(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("z").len(4), AssertItemValue)

  def test_len_raises_err(self) -> None:
    """Check that should(v).have(i).len(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("z").len(2)

    self.assertEqual(str(out.exception), "1234 expected to have length 2.")

  def test_included_in(self) -> None:
    """Check that should(v).have(i).included_in(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").included_in([12, 34, 56]), AssertItemValue)

  def test_included_in_raises_err(self) -> None:
    """Check that should(v).have(i).included_in(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").included_in([13, 57])

    self.assertEqual(str(out.exception), "12 expected to be in [13, 57].")

  def test_not_in(self) -> None:
    """Check that should(v).have(i).not_io(v) returns the wrapper."""

    self.assertIsInstance(should(v).have("x").not_in([]), AssertItemValue)

  def test_not_in_raises_err(self) -> None:
    """Check that should(v).have(i).not_in(v) raises error if different."""

    with self.assertRaises(AssertionError) as out:
      should(v).have("x").not_in([12, 34])

    self.assertEqual(str(out.exception), "12 expected not to be in [12, 34].")
