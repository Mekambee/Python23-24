import sys
if __name__ == "__main__":
    argv = sys.argv[1]
    string_measure = '|....' * int(argv) + '|'
    numbers = ''
    for i in range(0, int(argv)+1):
        space = 5 - len(str(i))
        numbers += ' ' * space + str(i)
    print(string_measure)
    print(numbers.lstrip())
