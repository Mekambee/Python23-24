import sys
def rysuj_miarke(length):
    string_measure = '|....' * length + '|'
    numbers = ''
    for i in range(0, length+1):
        space = 5 - len(str(i))
        numbers += ' ' * space + str(i)
    print(string_measure)
    print(numbers.lstrip())

if __name__ == "__main__":
    argv = sys.argv[1]
    rysuj_miarke(int(argv))
