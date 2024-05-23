def main():
    book = r"books/frankenstein.txt"
    text = get_book_text(book)
    num_words = get_word_count(text)
    num_letters = count_letters(text)
    print_report(book, num_words, num_letters)
def print_report(title, words, letters):
    report_title = print(f"--- Begin report of {title} ---")
    print(f"{words} words are in this book\n")

    for char in letters:
        l = letters[char]
        if char.isalpha():
            print(f"the \'{char}\' character was found {letters[char]} times")
    print("\n--- End report ---")
def count_letters(w):
    letter_dict = {}
    words = w.split()
    # words = words.lower()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict
def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_word_count(text):
    words = text.split()
    return len(words)
main()
