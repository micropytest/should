# Should

An assertion lib for **MicroPython** and **MicroPytest**.

## Install

```bash
micropython -m mip install github:micropytest/should
```

## Usage

Import the **`should`** object from the library to start making assertions.

```python
from should import should
```

### Equality and identity

- **`should(value).be(expected)`**: Asserts that the actual value is the same object as the expected value.

- **`should(value).not_be(expected)`**: Asserts that the actual value is not the same object as the expected value.

- **`should(value).be_eq(expected)`**: Asserts that the actual value is equal to the expected value (`==`).

- **`should(value).not_be_eq(expected)`**: Asserts that the actual value is not equal to the expected value (`!=`).

```python
should(5).be_eq(5)
should("hello").not_be_eq("world")
```

### Truthiness and None

- **`should(value).be_true()`**: Asserts that the value is truthy.

- **`should(value).be_false()`**: Asserts that the value is falsy.

- **`should(value).be_none()`**: Asserts that the value is **`None`**.

- **`should(value).not_be_none()`**: Asserts that the value is not **`None`**.

```python
should(True).be_true()
should(0).be_false()
should(None).be_none()
should("value").not_be_none()
```

### Comparisons

- **`should(value).be_gt(expected)`**: Asserts that the value is greater than the expected value (`>`).

- **`should(value).be_ge(expected)`**: Asserts that the value is greater than or equal to the expected value (`>=`).

- **`should(value).be_lt(expected)`**: Asserts that the value is less than the expected value (`<`).

- **`should(value).be_le(expected)`**: Asserts that the value is less than or equal to the expected value (`<=`).

```python
should(10).be_gt(5)
should(10).be_ge(10)
should(5).be_lt(10)
should(5).be_le(5)
```

### Collections and containment

- **`should(value).contain(item)`**: Asserts that the value contains the given item.

- **`should(value).not_contain(item)`**: Asserts that the value does not contain the given item.

- **`should(value).be_in(collection)`**: Asserts that the value is present in the given collection.

- **`should(value).not_be_in(collection)`**: Asserts that the value is not present in the given collection.

- **`should(value).have_len(length)`**: Asserts that the value has the specified length.

- **`should(value).not_have_len(length)`**: Asserts that the value does not have the specified length.

```python
my_list = [1, 2, 3, 4]

should(my_list).contain(3)
should(my_list).not_contain(5)
should(3).be_in(my_list)
should(5).not_be_in(my_list)

should("hello").have_len(5)
should([1, 2]).not_have_len(3)
```

### Types and callability

- **`should(value).be_instance_of(class)`**: Asserts that the value is an instance of the given class.

- **`should(value).not_be_instance_of(class)`**: Asserts that the value is not an instance of the given class.

- **`should(value).be_callable()`**: Asserts that the value is callable (e.g., a function).

- **`should(value).not_be_callable()`**: Asserts that the value is not callable.

```python
should("a string").be_instance_of(str)
should(123).not_be_instance_of(str)

def my_func():
    pass

should(my_func).be_callable()
should(123).not_be_callable()
```

### String matching

- **`should(value).be_like(pattern)`**: Asserts that the string value matches the given regular expression pattern.

- **`should(value).not_be_like(pattern)`**: Asserts that the string value does not match the given regular expression pattern.

```python
should("assertion test").be_like("assert")
should("micropython").not_be_like("java")
```

### Exception Handling

#### Using a wrapped value

- **`should(fn).throw(exception=None, message_pattern=None)`**: Asserts that a callable raises a specific exception, optionally matching the exception message against a regex pattern.

```python
should(fn).throw()
should(fn).throw(ValueError)
should(fn).throw(ValueError, "is an error")
```

#### Using a context manager

- **`should.throw(exception=None, message_pattern=None)`**: Asserts that a callable raises a specific exception, optionally matching the exception message against a regex pattern.

```python
# check for exception raised
with should.throw():
  # code where the exception should be raised

# check for the exception type
with should.throw(ValueError):
  # code where the exception should be raised

# check for the exception type and message
with should.throw(ValueError, "is an error"):
  # code where the exception should be raised
```

### Assertions on items

**`should(value).have()`** allows works with items, for example, from a dictionary.
Example:

```python
should(dict(x=12, y=34)).have("x").eq(12)
should(dict(x=12, y=34)).not_have("z")
```

When this assert method used, the following assert methods can be used:

- **`should(v).have(i).like(pattern: str | re.Pattern)`**

- **`should(v).have(i).not_like(pattern: str | re.Pattern)`**

- **`should(v).have(i).instance_of(cls: type)`**:

- **`should(v).have(i).not_instance_of(cls: type)`**

- **`should(v).have(i).to_true()`**:

- **`should(v).have(i).to_false()`**

- **`should(v).have(i).same_as(o: Any)`**, similar to **`be()`**

- **`should(v).have(i).not_same_as(o: Any)`**

- **`should(v).have(i).len(size: int)`**

- **`should(v).have(i).eq(o: Any)`**

- **`should(v).have(i).not_eq(o: Any)`**

- **`should(v).have(i).lt(o: Any)`**

- **`should(v).have(i).le(o: Any)`**

- **`should(v).have(i).gt(o: Any)`**

- **`should(v).have(i).ge(o: Any)`**

- **`should(v).have(i).included_in(i: Iterable[Any])`**

- **`should(v).have(i).not_in(i: Iterable[Any])`**

