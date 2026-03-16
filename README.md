# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] The game's purpose is to guess a number given a range. You can use hints which will tell you if you should guess higher or lower.
- [ ] Detail which bugs you found.
Bug 1 — Hard difficulty range was too easy.
get_range_for_difficulty("Hard") returned (1, 50) — a smaller range than Normal (1–100), making Hard easier, not harder.
Bug 2 - Hint direction messages were flipped.
Problem: When a guess was too high, the message said "Go HIGHER!" and when too low, it said "Go LOWER!" — the opposite of correct.
Bug 3: Secret number regenerates on every rerun.
The "New Game" button always uses 1, 100 regardless of difficulty. Also, the session state isn't reset for attempts, status, history, or score when clicking New Game.
- [ ] Explain what fixes you applied.
Fix for Bug 1: Changed the Hard range to (1, 500).
Fix for Bug 2: Swapped the hint messages to match the actual outcome.

## 📸 Demo

- [ ] [![alt text](<CleanShot 2026-03-15 at 21.23.29@2x.png>)]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
