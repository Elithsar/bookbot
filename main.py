def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
