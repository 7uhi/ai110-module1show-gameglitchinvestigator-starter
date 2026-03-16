# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Guess a # between 1 and 100. If I enter 1, it tells me to go lower. If I enter 0, same thing.
- It says attempts left: 1, but the game ended and told me I am out of attempts.
- Told me to go higher when I typed in 50 and 75, but the secret number was 28.
- Clicking New Game does not allow me to submit a new guess. Keeps saying “Game over. Start a new game to try again."
- Attempts allowed 8 on sidebar but says 7 on game.
- Easy mode has less attempts than hard mode.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
An AI suggestion that was correct was to change the hard difficulty range from return 1,50 to return 1,500 so it matches the difficulty. I verified the result by running a test in test_game_logic.py and also by changing the difficulty in the game itself to see if it reflected the changes made.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
For the bugs I fixed so far, I did not notice an AI suggestion that was incorrect or misleading.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided whether a bug was really fixed by checking if it passed the pytest and also by going into the game and checking if it works myself.
- Describe at least one test you ran (manual or using pytest)  
and what it showed you about your code.
One test I ran manually was for the difficulty range bug. I went on the game and cycled between the difficulties (Easy, Normal, Hard) and the range increased as the difficulty increased, reflecting the fix. It showed that the code worked.
- Did AI help you design or understand any tests? How?
AI did help me design and understand these tests as it generated the test_game_logic.py, and I could better understand how to create and use tests for bugs.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
