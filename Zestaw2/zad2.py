import re
from collections import Counter
def stringCounter(string):
    words = re.findall(r'\b[a-zA-Z0-9]+\b',string)
    letters = re.findall(r'[a-zA-Z]', string)
    digits = re.findall(r'[0-9]', string)
    print(f"Dła słowa: {string}  \n Liczba słów: {len(words)} \n Liczba liter: {len(letters)} \n Liczba cyfr: {len(digits)}")

    print("Częstość występowania poszczególnych liter:")

    letter_frequency = Counter(letter.lower() for letter in letters)
    sorted(letter_frequency)
    for letter, count in letter_frequency.items():
        print(f"{letter}: {count}")

    print("Częstość występowania poszczególnych cyfr:")

    digit_frequency = Counter(digit for digit in digits)
    sorted(digit_frequency)
    for digit, count in digit_frequency.items():
        print(f"{digit}: {count}")

if __name__ == "__main__":
    test_word = "Ala a b ma kota 4 5 6 $$$$$ #"
    stringCounter(test_word)
