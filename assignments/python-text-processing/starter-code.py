import string
from collections import Counter

INPUT_FILE = "sample-text.txt"
OUTPUT_FILE = "processed-text.txt"

PUNCTUATION_TO_REMOVE = string.punctuation.replace(".", "")


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def count_sentences(text):
    return sum(text.count(marker) for marker in [".", "?", "!"])


def clean_text(text):
    text_lower = text.lower()
    text_clean = text_lower.translate(str.maketrans("", "", PUNCTUATION_TO_REMOVE))
    return text_clean


def get_unique_sorted_words(text):
    words = text.split()
    return sorted(set(words))


def get_word_counts(text):
    words = text.split()
    return Counter(words)


def write_processed_text(text, path):
    words = text.split()
    with open(path, "w", encoding="utf-8") as file:
        file.write(" ".join(words))


def main():
    raw_text = read_file(INPUT_FILE)
    line_count = raw_text.count("\n") + 1 if raw_text else 0
    word_count = len(raw_text.split())
    sentence_count = count_sentences(raw_text)

    cleaned = clean_text(raw_text)
    unique_words = get_unique_sorted_words(cleaned)
    word_counts = get_word_counts(cleaned)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print("Top 5 most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word}: {count}")

    write_processed_text(cleaned, OUTPUT_FILE)
    print(f"Processed text written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
