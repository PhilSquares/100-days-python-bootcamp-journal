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


## Day 3 — Beginner - Control Flow and Logical Operators

### Conditional Statements
  - Conditional statements allow programs to make decisions.

Basic syntax:

```python
if condition:
    do_this
elif another_condition:
    do_this_instead
else:
    do_this_if_all_else_fails
```

## Comparison Operators:
  - Used to compare values:

| Operator | Meaning |
|---------|--------|
| `==` | Equal to |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

Example:
```python
age = 18

if age >= 18:
    print("You can vote.")
else:
    print("You are underage.")
```

## Logical Operators
  - Used to combine conditions.

### Logical Operators

| Operator | Meaning |
|---------|--------|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses a condition |

Example:
```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

## Nested Conditionals
  - Conditionals inside other conditionals.

Example:
```python
choice = input("Left or right? ").lower()

if choice == "left":
    print("You move forward.")
    if choice == "left":
        print("You found treasure!")
else:
    print("Game over.")
```
Used heavily in decision-based games like `Treasure Island`.

String Methods for Input Handling

`.lower()` converts text to lowercase:

```python
user_input = input("Type YES or NO: ").lower()
```

This prevents issues with:
  - YES vs yes
  - Yes vs yEs

## Control Flow Design
Control flow is the order in which code executes.

With conditionals, you can:
  - Block access to logic
  - Create branching paths
  - Build interactive programs
  - Simulate game states

This is the foundation for:
  - Game loops
  - Validation systems
  - Menu systems
  - User authentication logic

---

## Day 4 - Beginner - Randomisation and Python Lists

### The Random Module 
Python provides a built-in `random` module for generating random values.

Common functions:

```python
import random

random.randint(1, 10)   # Random integer between 1 and 10 (inclusive)
random.random()        # Random float between 0 and 1
```

### Python Lists
Lists store multiple values in a single variable.

Example:
```python
fruits = ["apple", "banana", "cherry"]
```
Access items using indexing:
```python
fruits[0]  # "apple"
fruits[1]  # "banana"
```

### List Length
Use `len()` to get the size of a list:
```python
len(fruits)  # 3
```

### Random Selection from a List
A common pattern is choosing a random element:
```python
import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
```

Or by index:
```python
index = random.randint(0, 2)
computer_choice = choices[index]
```

### Using Lists with Game Logic
  - Lists are useful for:
  - Mapping numeric input to values
  - Storing game states
  - Managing collections of options

Example:
```python
options = ["rock", "paper", "scissors"]
user_choice = int(input("Choose 0, 1, or 2: "))
print(options[user_choice])
```

### Why This Matters
Randomness + lists are foundational for:
  - Games
  - Simulations
  - Sampling data
  - AI behavior
  - Probabilistic systems


## Day 5 - Beginner - Python Loops

### 🔁 For Loops

Used to repeat an action a specific number of times.

```python
for i in range(0, 5):
    print(i)
```

### 📋 Lists
Lists store multiple values in a single variable.

```python
fruits = ["apple", "banana", "cherry"]
```

Add items to a list using:
```python
fruits.append("orange")
```

### 🎲 Random Module
Import the random module to generate random values:

```python
import random
```

Pick a random item from a list:
```python
random.choice(my_list)
```

Shuffle a list in-place:
```python
random.shuffle(my_list)
```

### 🔗 Building Strings from Lists
Convert a list into a string by looping through it:
```python
password = ""
for char in password_list:
    password += char
```

### 💡 Key Takeaways
- Loops are ideal for repetitive tasks.
- Lists allow dynamic data storage and manipulation.
- Randomization is essential for generating secure outputs.
- Shuffling ensures unpredictability in generated results.