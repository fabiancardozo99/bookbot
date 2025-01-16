# Function to read the content of a file (book)
def read_file(book_path):
    with open(book_path) as f:
        book_content = f.read()
    
    return book_content

# Function to count the number of words in a file (book)
def count_words(book):
    count = 0
    words = book.split()

    for word in words:
        count += 1
    
    return count

# Function calculate how many times a character repeats in the text
def count_chars(book):
    characters = {}

    for char in book:
        lower_char = char.lower()
        if lower_char not in characters:
            characters[lower_char] = 1
        else:
            characters[lower_char] += 1
    
    return characters

# Key function for sort() method
def sort_dict(dict):
    return dict["num"]

# Function to convert a dictionary in a list of dictionaries
def dict_to_sorted_list(chars_dict):
    sorted_list = []

    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_dict)

    return sorted_list

def main():
    book_path = "books/frankenstein.txt"
    book_content = read_file(book_path)
    number_of_words = count_words(book_content)
    number_of_chars = count_chars(book_content)
    sorted_list_chars = dict_to_sorted_list(number_of_chars)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document\n")

    for item in sorted_list_chars:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


main()