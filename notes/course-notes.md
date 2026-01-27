# 📚 Course Notes

## Day 1 — Working with Variables in Python

### 🖨 Printing
- Output text to the console using:
  ```python
  print("Hello World")
  ```

### 👤 User Input
- Prompt users for input with:
  ```python
  input("What is your name?")
  ```
- By default, input returns a string.

### 📝 Variables
- Store values for reuse in your program.
- Naming conventions:
1. Use descriptive names **(user_name, city_name)**.
2. Use **snake_case**.
3. Avoid **reserved keywords**.

### 💡 Extra Notes
- String concatenation allows combining variables and strings with the + operator.
- Comments **(# This is a comment)** are useful for explaining code.
- Debugging tip: print intermediate values to ensure your program is working as expected.

## Day 2 — Understanding Data Types & String Manipulation

### Mathematical Operations in Python

Python supports all standard arithmetic operators:

| Operation | Example | Result | Description |
|----------|--------|--------|-------------|
| Division | `5 / 3` | `1.6667` | Returns a float |
| Floor Division | `5 // 3` | `1` | Rounds down to nearest integer |
| Exponent | `2 ** 2` | `4` | Raises a number to a power |

---

### Type Checking

Use the built-in `type()` function to determine the data type of a value:

```python
type(12)       # int
type("Hello") # str
type(3.14)    # float
type(True)    # bool
```

Type Casting

Convert between data types using built-in functions:

```python
int("123")     # 123
float("3.5")  # 3.5
str(42)       # "42"
```

Rounding & Integer Conversion
Flooring

Converting a float to an integer removes the decimal:

```python
int(11.4)  # 11
```

Rounding

The `round()` function rounds to the nearest value:

```python
round(11.5)  # 12
```

`round()` can also accept a second argument for decimal precision:

```python
bmi = 30.85399449035813
round(bmi, 2)

# Result: 30.85
```

F-Strings (Formatted Strings)

F-strings make it easy to mix text with variables.

```python
score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, winning: {is_winning}")
```

They are faster, cleaner, and more readable than string concatenation.