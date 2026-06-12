---
title: "Python Text Processing"
difficulty: "Beginner"
estimated_time: "45-60 minutes"
---

# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice Python string handling, file input/output, and text manipulation by extracting information and transforming file contents.

## 📝 Tasks

### 🛠️ Read and analyze text from a file

#### Description
Write code to open a text file, read its contents, and count information about the text.

#### Requirements
Completed program should:

- Open `sample-text.txt` for reading.
- Count the total number of words in the file.
- Count the total number of lines.
- Count the number of sentences by using punctuation markers like `.`, `?`, and `!`.

### 🛠️ Clean and normalize text

#### Description
Clean the text by removing punctuation, converting it to lowercase, and splitting it into words.

#### Requirements
Completed program should:

- Remove punctuation characters from the text.
- Convert all text to lowercase.
- Split the cleaned text into individual words.
- Output a sorted list of unique words.

### 🛠️ Count word frequencies

#### Description
Analyze how often each word appears in the text.

#### Requirements
Completed program should:

- Count how often each word appears.
- Print the top 5 most common words and their counts.
- Handle repeated words in a case-insensitive way.

### 🛠️ Save a transformed version of the text

#### Description
Write the cleaned text back to a new file in a standardized format.

#### Requirements
Completed program should:

- Write cleaned text to `processed-text.txt`.
- Use single spaces between words.
- Preserve sentence boundaries by keeping one punctuation mark per sentence ending.
