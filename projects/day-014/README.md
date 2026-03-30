# Day 14 Project — Higher/Lower Game

## 📖 Description
A command-line game where users compare two celebrities, brands, or organizations and guess which one has a higher social media following.

Each correct guess increases the user's score and continues the game with a new comparison. The game ends when the user makes an incorrect guess.

---

## 🛠 Skills Practiced
- Modular code structure (separating logic, data, and UI).
- Working with dictionaries and lists.
- Random data selection using the `random` module.
- Function design and reusability.
- Conditional logic and comparisons.
- Game loop implementation and state management.

---

## ▶️ How to Run
```bash
python main.py
```
```markdown
🎯 Example Gameplay
Compare A: Instagram, a social media platform, from United States.
VS
Against B: Cristiano Ronaldo, a footballer, from Portugal.

Who has more followers? Type 'A' or 'B':
> a

You're right! Current score: 1
```

## 📁 Project Structure
```markdown
day-014/
├── main.py        # Game logic
├── art.py         # ASCII art for UI
├── game_data.py   # Dataset of accounts and follower counts
└── README.md      # Project documentation
```

## 💡 Key Takeaways
- Structuring projects across multiple files improves scalability.
- Separating data from logic is a core software engineering principle.
- Game loops are a practical way to understand stateful program execution.
---