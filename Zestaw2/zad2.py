import re
def stringCounter(string):
    words_count = len(re.findall(r'\b[a-zA-Z0-9]+\b',string))
    letters_count = len(re.findall(r'[a-zA-Z]', string))
    digits_count = len(re.findall(r'[0-9]', string))
    print(f"Dła słowa[ {string} ]: \n Liczba słów: {words_count} \n Liczba liter: {letters_count} \n Liczba cyfr: {digits_count}")


if __name__ == "__main__":
    test_word = "Ala a b ma kota 4 5 6 $$$$$ #"
    stringCounter(test_word)
