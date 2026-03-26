# Day 12 Project — Number Guessing Game

## 📖 Description
A command-line number guessing game where the player attempts to guess a randomly generated number between 1 and 100.

Features:
- Two difficulty levels:
  - Easy (10 attempts)
  - Hard (5 attempts)
- Feedback after each guess:
  - Too high
  - Too low
- Game ends when:
  - The player guesses correctly
  - The player runs out of attempts

---

## 🛠 Skills Practiced
- Variable scope (local vs global)
- Function design and return values
- Control flow with loops and conditionals
- Game state management
- Use of constants for configuration
- Random number generation

---

## ▶️ How to Run
```bash
python main.py
```

## 🎯 Example Gameplay
```python
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Choose a difficulty. Type 'easy' or 'hard': hard

You have 5 attempts remaining to guess the number.
Make a guess: 50
Too low.

Guess again.
You have 4 attempts remaining...
```

## 💡 Key Takeaway
- This project highlights how scope and function design work together to manage application state, which is critical for building scalable and maintainable programs.
---