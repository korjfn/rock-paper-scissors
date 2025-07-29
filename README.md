# 🎮 Rock, Paper, Scissors – Python Game

## 📋 Description

A fun and interactive **Rock 🪨 Paper 📃 Scissors ✂️** game built in Python where you compete against the computer. The program tracks the score, gives real-time results, and continues playing until you decide to quit.

---

## 💡 Features

- 🧠 Computer selects a random move each round  
- 📊 Score tracking for both user and computer  
- 🔁 Continuous gameplay until user types `'quit'`  
- 🧼 Input validation with friendly messages  
- 🎉 Emoji-enhanced feedback for an engaging experience

---

## 🕹️ Example Gameplay

```text
Welcome to rock 🪨  Paper 📃 Scissors ✂️  
Choose rock paper or scissors(or 'quit' to stop)  
> rock  
the computer chose: scissors  
You win this round!🏆🥇  
score: You 1 | 0 computer

Choose rock paper or scissors(or 'quit' to stop)  
> quit
````

---

## 🚀 How It Works

1. The game runs in a loop until the user types `'quit'`.
2. Each round:

   * The user inputs their choice: `rock`, `paper`, or `scissors`
   * The computer randomly selects one of the three options
   * The winner is determined using standard game rules
   * Scores are updated and displayed
3. If the user types anything invalid, it prompts them again.

---

## 🧠 Concepts Used

* Lists
* Conditional statements
* Loops (`while True`)
* Random selection with `random.choice()`
* String handling and formatting

---

## 🛠 Requirements

* Python 3.x
  (No external libraries needed)

---

## ▶️ Running the Script

```bash
python rock_paper_scissors.py
```

---

## 🧰 Ideas for Future Enhancements

* Add a "best of 5" or "first to 3 wins" mode
* Add a GUI using Tkinter or a web version with Flask
* Track and display a match history
* Include sound effects or animations (for advanced users)

---

## 👨‍💻 Author

**alex**
[GitHub Profile](https://github.com/korjfn)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).