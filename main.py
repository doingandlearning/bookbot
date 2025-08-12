from stats import get_num_words, get_character_count, get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
            file_contents = f.read()
    return file_contents



def main(filepath):
    contents =get_book_text(filepath)
    word_count = get_num_words(contents)
    sorted_list = get_sorted_list(contents)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
    """)
    for item in sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"{item["letter"]}: {item["amount"]}")
    print("============= END ===============")



if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])


