from stats import count_words

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()
