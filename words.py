def print_upper_words(words, must_start_with=None):
    """Given a list of words, print out each word in uppercase on a separate line.  Prints out only words that start with letters in must_start_with if provided."""

    for word in words:
        if must_start_with:
            for letter in must_start_with:
                if word.startswith(letter):
                    print(f"{word.upper()}")
                    break
        else:
            print(f"{word.upper()}")