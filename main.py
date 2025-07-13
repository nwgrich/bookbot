from stats import get_num_words, get_char_count, sort_dict
import sys

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            return f.read()
    except FileNotFoundError:
        print(f"{path_to_file} was not found")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}... ")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    dict_list_descending = sort_dict(get_char_count(text))

    for dict in dict_list_descending:
        if dict[0].isalpha():
            print(f"{dict[0]}: {dict[1]}")
    print("============= END ===============")

main()
