
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman-style word guessing game in Python to practice strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Create the game loop and word selection

#### Description
Write a Python program that randomly selects a secret word from a predefined list and lets the player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- randomly choose a word from a predefined list
- prompt the player for single-letter guesses
- display the current word progress as `_ _ _ _`
- track and show remaining incorrect attempts

### 🛠️ Add win/lose logic and player feedback

#### Description
Implement game rules that update progress, prevent repeated guesses from wasting attempts, and show a clear result message when the game ends.

#### Requirements
Completed program should:

- reveal correct letters in the word as guesses are made
- prevent repeated guesses from counting as extra incorrect attempts
- end with a win message when the word is fully guessed
- end with a lose message when the player runs out of attempts
