from stats import get_book_text, get_num_words, get_counting_characters,sort_count
import sys

def main():

    argv = sys.argv
    if(len(argv)<=1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    list = sort_count(get_counting_characters(text))
    print("--------- Character Count -------")
    for l in list:
        print(f"{l["char"]}: {l["num"]}")
    print("============= END ===============")
main()
