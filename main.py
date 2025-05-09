import sys
from stats import get_num_words
from stats import count_character
from stats import sorted_list


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    character_count = count_character(book_text)
    sorted_char = sorted_list(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_info in sorted_char:
        print(f"{char_info['char']}: {char_info['num']}")

    print("============= END ===============")


main()
