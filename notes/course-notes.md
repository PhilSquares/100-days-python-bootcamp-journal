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
---

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
---

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
---


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
---

## Day 6 - Beginner - Python Functions & Karel

### 🧩 Python Functions

Functions allow you to group reusable code into a single block that can be called multiple times.

Define a function using the `def` keyword:

```python
def greet():
    print("Hello!")
```

Call the function:
  ```python
  greet()
  ```

Benefits of functions:
 - Improves code readability
 - Reduces repetition
 - Makes programs easier to maintain
 - Allows logical separation of tasks

 🔁 Creating Helper Functions
   - Sometimes we build new behavior using existing functions.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```
This creates a reusable function for turning right even if the environment only provides `turn_left()`.

  🔄 While Loops
  - A while loop repeats code as long as a condition remains true.

```python
while not at_goal():
    move()
```
This loop continues executing until the goal condition becomes true.

🧠 Conditional Logic for Decision Making
  - Programs often need to make decisions based on environment conditions.

```python
if right_is_clear():
    turn_right()
elif front_is_clear():
    move()
else:
    turn_left()
```
This logic checks conditions in order and executes the first valid action.

🧭 Maze Solving Strategy (Right-Hand Rule)
The maze challenge uses a common navigation algorithm:
1. If you can turn right, turn right and move.
2. Else if you can go forward, move forward.
3. Otherwise turn left.

This strategy ensures that a robot following a wall will eventually reach the exit in many maze structures.

💡 Key Takeaways
  - Functions help organize complex logic into reusable components.
  - Helper functions simplify repetitive tasks.
  - while loops allow programs to react dynamically to changing conditions.
  - Combining loops with conditional logic enables algorithmic problem solving.
---

## Day 7 - Beginner - Hangman
### 🎯 Game State Management

Games require tracking multiple pieces of state:

- `lives` → remaining attempts
- `game_over` → controls loop termination
- `correct_letters` → stores correct guesses

Example:

```python
lives = 6
game_over = False
correct_letters = []
```
### 🔁 While Loop for Game Execution
The game runs continuously until a win or loss condition is met:

```python
while not game_over:
    # game logic here
```

### 📋 Tracking User Input
Store correct guesses to preserve progress:

```python
correct_letters.append(guess)
```

Prevent duplicate guesses:
```python
if guess in correct_letters:
    print("Already guessed")
```

### 🧱 Building Dynamic Output
Rebuild the displayed word on every loop iteration:
```python
display = ""

for letter in chosen_word:
    if letter in correct_letters:
        display += letter
    else:
        display += "_"
```

### ❤️ Lives System
Track incorrect guesses:

```python
if guess not in chosen_word:
    lives -= 1
```
End the game when lives reach zero:

```python
if lives == 0:
    game_over = True
```

### 🏁 Win Condition
Check if the user has guessed all letters:

```python
if "_" not in display:
    game_over = True
```

### 💡 Key Takeaways
- Managing state is critical in interactive applications.
- Lists are useful for tracking progress over time.
- Loops + conditionals form the backbone of game logic.
- Clear separation of responsibilities improves readability (to be improved with functions later).
---

## Day 8 - Beginner - Function Parameters & Caesar Cipher
### 🧩 Function Parameters

Functions can accept inputs (parameters) to make them reusable and dynamic.

Example:

```python
def greet(name):
    print(f"Hello, {name}")
```

Call the function:
```python 
greet("Phil")
```

### 🔄 Functions with Multiple Parameters
You can pass multiple values into a function:

```python
def calculate_total(price, tax):
    return price + tax
```

### 🔁 Reusable Logic Design
Instead of writing separate functions for encoding and decoding, you can use one function with conditional logic:

```python 
if direction == "decode":
    shift *= -1
```

### 🔤 Working with Index Positions
You can find the position of a letter in a list:

```python 
position = alphabet.index(letter)
```

Then shift it:
```python 
new_position = position + shift
```

### 🔁 Modulo Operator (%)
The modulo operator ensures values wrap around within a fixed range.

```python
shifted_position %= len(alphabet)
```
This prevents index errors and keeps values within bounds.

### 🧠 Handling Edge Cases
Not all characters should be transformed.

```python
if letter not in alphabet:
    output_text += letter
```
This preserves:
 - Spaces
 - Numbers
 - Symbols

### 🔁 Continuous Program Execution
Use a loop to allow repeated user interaction:

```python
while should_continue:
    # run program
```

### 💡 Key Takeaways
 - Parameters make functions flexible and reusable.
 - Modulo arithmetic is essential for circular data structures.
 - A single function can handle multiple behaviors with conditional logic.
 - Handling edge cases improves program robustness.
 - This pattern mirrors real-world data transformation in backend systems.
---

## Day 9 - Beginner - Dictionaries, Nesting, and the Secret Auction
### 📦 Dictionaries (Key-Value Pairs)

Dictionaries store data as key-value pairs.

Example:

```python
bids = {
    "Alice": 100,
    "Bob": 150
}
```

- Keys must be unique.
- Values can be any data type.

### ➕ Adding Data to a Dictionary
 - Add new entries dynamically:

```python
bids["Charlie"] = 200
```

### 🔁 Iterating Through a Dictionary
 - Loop through keys:

```python
for bidder in bids:
    print(bidder)
```

 - Access values:

```python
for bidder in bids:
    print(bids[bidder])
```

### 🧠 Finding the Maximum Value
 - Track the highest value while iterating:

```python
highest_bid = 0
winner = ""

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
```

### 🧩 Functions for Separation of Concerns
 - Encapsulate logic into functions:

```python
def find_highest_bidder(bidding_record):
    # logic here
```

 - Benefits:
   - Cleaner code
   - Easier debugging
   - Reusability

### 🔁 Looping for Continuous Input
 - Use a loop to collect multiple inputs:

```python 
while continue_bidding:
    # collect input
```

### 🧱 Nesting (Preview Concept)
 - Dictionaries can store more complex structures:

```python
users = {
    "Alice": {"bid": 100, "location": "NY"},
    "Bob": {"bid": 150, "location": "CA"}
}
```

This is useful for:
  - APIs
  - Database records
  - JSON data structures

### 💡 Key Takeaways
- Dictionaries are ideal for structured data storage.
- Iterating through dictionaries enables data processing.
- Separating logic into functions improves code quality.
- This pattern mirrors real-world backend systems (e.g., request payloads, database queries).
---

## Day 10 - Beginner - Functions with Outputs
### 🔁 Functions with Return Values

Functions can return data using the `return` keyword:

```python
def add(n1, n2):
    return n1 + n2
```
- `return` sends the result back to where the function was called.
- Unlike `print()`, returned values can be stored and reused.

### 🧠 Print vs Return
```python
def example():
    print("Hello")   # Outputs to console
    return "Hello"   # Sends value back
```
- `print()` → displays output.
- `return` → passes value for further use.

### 🗂 Storing Functions in Data Structures
Functions can be stored in dictionaries and called dynamically:

```python
operations = {
    "+": add,
    "-": subtract
}

result = operations["+"](2, 3)  # Calls add(2, 3)
```

This pattern enables clean and scalable logic handling.

### 🔁 While Loops for Continuous Execution
```python
while should_continue:
    # perform operation
```

Used to:
  - Keep programs running.
  - Allow repeated user interaction.

### 🔄 Recursion
Recursion occurs when a function calls itself:

```python 
def calculator():
    ...
    calculator()
```

Used here to:
  - Restart the calculator program.

### ⚠️ Note:
- Recursion must have a stopping condition.
- Excessive recursion can lead to stack overflow.

### 💡 Key Takeaways
- Functions with `return` enable reusable and flexible code.
- Dictionaries can map user input to functionality.
- Loops allow continuous interaction.
- Recursion is powerful but should be used carefully.
---

## Day 11 - Beginner - The Blackjack Capstone Project
### 🧩 Breaking Down Complex Problems

Large programs should be divided into smaller functions:

```python
def deal_card():
def calculate_score(cards):
def compare(u_score, c_score):
```

Each function has a single responsibility, making the code easier to read and maintain.

### ♠️ Game Logic Design
Key components of the Blackjack game:
  - Initial card dealing
  - Player decision loop (hit or stand)
  - Dealer logic (draw until >= 17)
  - Final score comparison

### 🃏 Handling Special Cases
Blackjack (Natural 21)
```python
if sum(cards) == 21 and len(cards) == 2:
    return 0
```

- Returning 0 acts as a special flag value for Blackjack.

### Ace Adjustment
```python
if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
```

- Prevents the player from busting unnecessarily. 

### 🔁 Game Flow Control
Player Turn
 - Continue drawing cards until:
     - Player chooses to stop
     - Player busts
     - Player hits Blackjack

### Dealer Turn
```python
while computer_score < 17:
    computer_cards.append(deal_card())
```

- Dealer follows fixed rules

### ⚖️ Comparing Scores
Encapsulate logic in a dedicated function:
```python
def compare(u_score, c_score):
```

Benefits:
  - Cleaner main logic
  - Easier debugging
  - Reusable logic

### 💡 Key Takeaways
- Break complex systems into small, focused functions.
- Use helper functions to improve readability.
- Handle edge cases explicitly.
- Separate game logic from user interaction when possible.
- This is your first end-to-end application-style project.
---

## Day 12 - Beginner - Scope & Number Guessing Game
### 🌍 Variable Scope

Scope determines where a variable is accessible in your code.

#### Local Scope
Variables defined inside a function are only accessible within that function:

```python
def my_function():
    x = 10  # Local variable
```

### Global Scope
- Variables defined outside functions can be accessed anywhere:

```python
x = 10  # Global variable
```

### ⚠️ Modifying Global Variables
- Avoid modifying global variables directly inside functions.
     - Instead: 
       - Pass values as parameters.
       - Return updated values.

```python
def update_turns(turns):
    return turns - 1
```

### 🔢 Constants
- Constants are variables that should not change.

```python
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
```

- Use uppercase naming convention.
- Improves readability and maintainability.

### 🎯 Game Flow Structure
1. Generate a random number.
2. Set difficulty (number of attempts).
3. Loop until:
  - User guesses correctly.
  - User runs out of attempts. 

### 🔁 While Loop for Game Logic
```python
while guess != answer:
```

Used to:
  - Continuously prompt user input.
  - Evaluate guesses dynamically.

### 🔄 Returning Updated State
```python
turns = check_answer(guess, answer, turns)
```

- Functions can return updated values.
- Helps maintain clean and predictable state.

### 💡 Key Takeaways
- Scope controls where variables can be accessed.
- Avoid unnecessary global variables.
- Use functions to manage and update state.
- Constants improve code clarity.
- This pattern is foundational for larger applications.
---

## Day 13 - Beginner - Debugging: How to Find and Fix Errors in your Code

### 🐞 Types of Errors

#### 1. Syntax Errors
- Occur when code violates Python syntax rules.
- Example: missing colon, incorrect indentation.

#### 2. Runtime Errors
- Occur during execution.
- Example: index out of range.

#### 3. Logic Errors
- Code runs but produces incorrect results.
- Hardest to detect.

---

### 🔍 Debugging Techniques

#### 1. Describe the Problem
- Understand what the code is supposed to do.
- Identify where expectations differ from reality.

---

#### 2. Reproduce the Bug
- Ensure the issue can be consistently triggered.
- Helps isolate the root cause.

---

#### 3. Play Computer
- Step through code manually.
- Track variable values at each step.

---

#### 4. Use Print Statements
```python
print(variable)
```

- Helps trace execution flow.
- Quick and effective debugging method.

#### 5. Use a Debugger
- Set breakpoints.
- Step through code line by line.
- Inspect variable state in real time.

### ⚠️ Common Mistakes
- Off-by-one errors in loops: 

```python
range(1, 20)  # Does NOT include 20
```

- Assignment vs comparison:

```python
x = 5   # assignment
x == 5  # comparison
```

- Indexing errors:

```python
list[6]  # Out of range if list has 6 items (0-5)
```

### 💡 Key Takeaways
- Debugging is a structured process, not guesswork.
- Always verify assumptions about your code.
- Use tools (print, debugger) to inspect behavior.
- Strong debugging skills = strong engineering skills.
---

## Day 14 - Beginner - Higher/Lower Game Project
### 🧱 Modular Code Structure
Breaking code into multiple files improves readability and maintainability:

- `main.py` → Core game logic
- `art.py` → UI elements (ASCII art)
- `game_data.py` → Dataset used in the game

---

### 🔁 Game Loop Pattern
A `while` loop is used to keep the game running:

```python
while game_should_continue:
    # game logic here
```

Key concept:
- Maintain a game state variable (e.g., game_should_continue).
- Update it based on user success/failure.

### 🎲 Random Data Selection
- Use the random module to select items dynamically:

```python
import random
account = random.choice(data)
```
- Ensures variability in gameplay.

### 🧠 Function Design
- Functions help isolate logic:

```python
def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"
```

Benefits:
- Improves readability.
- Encourages reuse.
- Simplifies debugging.

### ⚖️ Comparison Logic
- Compare two values and return a boolean result:

```python
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
```

### 📊 State Management
Track values across iterations:
- score → increments on correct answers
- game_should_continue → controls loop execution

### 💡 Key Takeaways
- Modularization is essential for scalable applications.
- Game loops are a common real-world programming pattern.
- Clean function design leads to more maintainable code.
- Separating data from logic improves flexibility and reusability.
---

## Day 15 - Intermediate - Local Development Environment Setup & Coffee Machine Project

### 🧱 Structured Program Design
Large programs should be broken into smaller, focused functions:

- `is_resource_sufficient()` → validation
- `process_coins()` → input handling
- `is_transaction_successful()` → payment logic
- `make_coffee()` → state mutation

---

### 📦 Nested Dictionaries
Used to represent structured data like menus:

```python
MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    }
}
```

- Allows easy access:
```python
MENU["latte"]["ingredients"]["water"]
```

## 🔁 Application Loop
- Main program runs continuously until turned off:

```python
while is_on:
    choice = input("What would you like?: ")
```

## ⚙️ State Management
- Track application state using variables:
  - resources → available ingredients
  - profit → total money earned

```python
resources["water"] -= 50
profit += drink_cost
```

## 💰 Handling Transactions
Break payment logic into steps:

1. Accept input (coins).
2. Calculate total.
3. Compare with cost.
4. Return change if necessary.

```python
if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
```

## 🧪 Validation Before Execution
- Always validate before performing an action:

```python
if is_resource_sufficient(drink["ingredients"]):
```

## 💡 Key Takeaways
- Real-world programs require structured logic and state management.
- Separating concerns improves scalability and readability.
- Validation and error handling are critical in production systems.
- This project mirrors backend service flows (request → validation → processing → response).
---

## Day 16 - Intermediate - Object Oriented Programming (OOP)
### 🧠 What is OOP?
Object-Oriented Programming is a programming paradigm that organizes code into objects, which combine data and behavior.

---

### 🧱 Classes vs Objects
- **Class** → Blueprint for creating objects  
- **Object** → Instance of a class

```python
class Dog:
    def bark(self):
        print("Woof")

my_dog = Dog()
my_dog.bark()
```

### ⚙️ Attributes vs Methods
- Attributes → Variables attached to an object (data)
- Methods → Functions that belong to an object (behavior)

💡 A method is called a method instead of a function because it belongs to a class and defines what an object can do.

### 🧩 Example from Project
```python
coffee_maker = CoffeeMaker()
coffee_maker.report()
```

- coffee_maker → object
- report() → method

### 🧱 Encapsulation
- Combining data and behavior into a single unit (class):

```python
class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300}
```

### 🧠 Key Benefits of OOP
- Better organization
- Improved scalability
- Easier maintenance
- Reusable components

### 💡 Key Takeaways
- Objects have attributes (data) and methods (behavior).
- Multiple objects can be created from the same class.
- OOP is widely used in backend systems and large applications.
---