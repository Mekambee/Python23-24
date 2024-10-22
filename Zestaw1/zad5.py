import os
import time
#funkcja do czyszczenia ekranu terminala dla lepszego efektu
#polecenie czyszczace terminal na windowsie(nazwa - nt) to cls, dla pozostałych systemów - clear
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_text_at_position(text, position, max_height):
    clear_terminal()
    for i in range(max_height):
        if i == position:
            print(text)
        else:
            print()

if __name__ == "__main__":
    text = "Hello world!"
    max_height = 10
    position = 0
    direction = 1

    while True:
        print_text_at_position(text, position, max_height)
        time.sleep(0.1)
        position += direction
        if position == 0 or position == max_height - 1:
            direction *= -1
