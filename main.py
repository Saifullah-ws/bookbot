# python
from stats import get_num_words, count_characters, list_of_dictionaries
import sys
def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            book_path = sys.argv[1]

        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_count = count_characters(text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        list_of_dictionaries(char_count)
        
        #
        
def get_book_text(path):
        with open(path) as f:
            return f.read()


main() 
