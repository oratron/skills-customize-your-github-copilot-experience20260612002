
---
title: "Hangman Game Challenge"
difficulty: "Intermediate"
estimated_time: "45-60 minutes"
---

# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, conditionals, and user input to guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Game Setup

#### Description
Create a function that chooses a random word from a predefined list and initializes the game state.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Initialize the current guess state using underscores for unknown letters.
- Set a maximum number of incorrect attempts.

### 🛠️ Letter Guessing

#### Description
Implement the main guessing loop to accept user letters, update the displayed word, and handle guesses.

#### Requirements
Completed program should:

- Accept a single letter guess from the user.
- Reveal correctly guessed letters in the word display.
- Track and show incorrect letters separately.
- Update and display the remaining attempts.

### 🛠️ End Conditions

#### Description
Add logic to end the game when the player guesses the word or uses all attempts.

#### Requirements
Completed program should:

- End with a win message when the full word is revealed.
- End with a lose message when attempts reach zero.
- Display the correct word if the player loses.

### 🛠️ Game Feedback

#### Description
Provide clear progress and feedback during gameplay.

#### Requirements
Completed program should:

- Show current progress in `_ _ _` format.
- Display which letters have already been guessed.
- Print a final summary message after the game ends.
