import sys
from stats import get_chars,get_words_count,get_words,sort_chars_dict

def main():

    if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    book_path = sys.argv[1]

    text = get_words(book_path)
    num_words= get_words_count(text)
    chars= get_chars( text)
    chars_list= sort_chars_dict(chars)
    print_report( book_path,num_words,chars_list)

def print_report(book_path, num_words, chars_sorted_list):
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"total words : {num_words} ")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")


main()