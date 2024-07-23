import sys

def main():
    book = input("Choose a book: ")
    book_path = f"books/{book}.txt"

    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = count_characters(text)
    report = make_report(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"The book {path} was not found.")
        sys.exit()
    except Exception as e:
        print(f"An error has occurred: {e}")
        sys.exit()
    

def get_word_count(text):
    words = text.split()   
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count    

def sort_on(dict):
    return dict["num"]

def make_report(char_count):
    dict_list = []
    for char in char_count:
        dict_list.append({"char": char, "num": char_count[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


main()

        