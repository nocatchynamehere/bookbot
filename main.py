from stats import get_num_words, get_num_letters
import sys

def get_book_text(get_filepath):
    with open(get_filepath) as f:
        return f.read()

def splitify_book(whole_book):
    return whole_book.split()

def sort_on(items):
    return items["count"]

def letter_dict_convert(letter_count):
    letter_dict_list = []

    for letter, count in letter_count.items():
        format_letter_count = {}
        format_letter_count["letter"] = letter
        format_letter_count["count"] = count
        letter_dict_list.append(format_letter_count)
    return letter_dict_list
        

def main(get_filepath):
    whole_book = get_book_text(get_filepath)
    words = splitify_book(whole_book)
    word_count = get_num_words(words)
    letter_count = get_num_letters(words)
    letter_dict_list = letter_dict_convert(letter_count)
    letter_dict_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {get_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter_count_pair in letter_dict_list:
        letter = letter_count_pair["letter"]
        if letter.isalpha():
            num_letter = letter_count_pair["count"]
            print(f"{letter}: {num_letter}")
        else:
            continue
    print("============= END ===============")   

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)