# Day 3 Project — Treasure Island 🏝️

## 📖 Description:
Treasure Island is a **text-based adventure game** where the player makes a series of choices in an attempt to find hidden treasure.

The game presents the user with different scenarios and paths, and each decision determines whether they progress or reach a *Game Over* state. The goal is to choose the correct sequence of actions to successfully find the treasure.

This project demonstrates how simple logic and user input can be used to create an interactive game experience entirely in the terminal.

---

## 🛠 Skills Practiced:
- Conditional logic (`if`, `elif`, `else`)
- Nested decision trees
- Handling user input with `input()`
- String methods (`.lower()`)
- Writing readable control flow
- Basic game design logic

---

## ▶️ How to Run:
In your terminal, navigate to this folder and run:

```bash
python main.py
```

## 🎮 Gameplay Flow:
1. The player starts at a crossroads and chooses a direction.
2. Based on the choice, they encounter a lake and must decide how to cross.
3. Finally, the player selects a door inside a mysterious house.
4. Only one correct path leads to the treasure — all others result in failure.

## 🎯 Example Output:
```text
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad, where do you want to go? Type "left" or "right".
> left
You've come to a lake. There is an island in the middle of the lake. 
Type "wait" to wait for a boat. Type "swim" to swim across.
> wait
You arrive at the island unharmed. There is house with 3 doors. 
One red, one yellow, and one blue. Which color do you choose?
> yellow
You found the treasure. You Win!
```

## 💡 Notes:
This project focuses on logic and control flow, not graphics or UI. It’s a foundation for future projects that involve:
  - Game loops
  - State management
  - More complex branching narratives


---
 