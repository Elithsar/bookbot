from stats import count_words, count_chars_sorted

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    char_list = count_chars_sorted(text)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in char_list:
          if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print(f"============= END ===============")

main()
