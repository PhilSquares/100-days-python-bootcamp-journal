# Day 15 Project — Coffee Machine ☕️

## 📖 Description
A command-line coffee machine simulation that allows users to:
- Select a drink (espresso, latte, cappuccino).
- Insert coins to pay for the drink.
- Receive change if overpaid.
- View a resource report (water, milk, coffee, and profit).

The system validates available resources before fulfilling an order and updates internal state after each transaction.

---

## 🛠 Skills Practiced
- Function decomposition and separation of concerns
- Working with nested dictionaries
- State management using variables
- Conditional logic and control flow
- Simulating real-world systems (transactions, inventory)
- Input handling and user interaction

---

## ▶️ How to Run
```bash
python main.py
```

## 🎯 Example Interaction
```python
What would you like? (espresso/latte/cappuccino):
> latte

Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0

Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

## 📊 Features
- Resource validation before drink preparation.
- Coin-based payment system.
- Change calculation.
- Real-time resource tracking.
- Report command for system status.

## 📁 Project Structure
```python
day-015/
├── main.py     # Core application logic
└── README.md   # Project documentation
```

## 💡 Key Takeaways
- This project simulates a real-world system with multiple interacting components.
- Breaking logic into functions improves readability and maintainability.
- Managing state is a foundational concept for backend development.