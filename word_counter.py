def count_words(sentence: str) -> dict:
    """Return word analysis for given sentence.

    Raises ValueError if sentence is empty or only whitespace.
    Returns a dict with keys: 'word_count', 'char_count', 'longest_word'.
    """
    sentence = sentence.strip()
    if sentence == "":
        raise ValueError("Empty sentence")

    words = sentence.split()
    word_count = len(words)
    char_count = len(sentence.replace(" ", ""))
    longest_word = max(words, key=len)

    return {
        "word_count": word_count,
        "char_count": char_count,
        "longest_word": longest_word,
    }


def word_counter():
    """Command-line wrapper for backward compatibility."""
    try:
        sentence = input("Enter a sentence: ").strip()
        results = count_words(sentence)
    except ValueError:
        print("You entered nothing.")
        return

    print("\nResults:")
    print("Number of words:", results["word_count"])
    print("Characters (no spaces):", results["char_count"])
    print("Longest word:", results["longest_word"])


if __name__ == "__main__":
    word_counter()
