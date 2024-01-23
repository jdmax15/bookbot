def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    print(file_contents)

main()
