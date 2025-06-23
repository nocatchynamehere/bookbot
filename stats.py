def get_num_words(words):
    return len(words)

def get_num_letters(words):
    alphabet = {}
    for word in words:
        letters = list(word.lower())
        for letter in letters:
            if letter in alphabet:
                alphabet[letter] += 1
            else:
                alphabet[letter] = 1
    return alphabet