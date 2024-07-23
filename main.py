def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    print(text)

    word_count = get_word_count(text)
    print(f"Words: {word_count}")

    char_dict = count_characters(text)
    print(char_dict)

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
    with open(path) as f:
        return f.read()

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
    print(f"dict_list: {dict_list}")
    return dict_list


main()

        