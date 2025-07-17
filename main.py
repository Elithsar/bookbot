import sys
from stats import count_words, count_chars_sorted

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    char_list = count_chars_sorted(text)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in char_list:
          if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print(f"============= END ===============")

main()
