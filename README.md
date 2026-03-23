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

- **`should().throw(exception=None, message_pattern=None)`**: Asserts that a callable raises a specific exception, optionally matching the exception message against a regex pattern.

```python
# check for the exception type
with should().throw(ValueError):
  raise ValueError("This is an error")

# check for the exception type and message
with should().throw(ValueError, "is an error"):
  raise ValueError("This is an error")
```
