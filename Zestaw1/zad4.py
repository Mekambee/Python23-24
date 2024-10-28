import time
import sys

if __name__ == "__main__":
    argv = int(sys.argv[1])
    loading_line = '|' + '-' * argv + '|'

    for i in range(1, argv + 1):
        loading_line = loading_line[:i] + '=' + loading_line[i + 1:]
        percent = int((i / argv) * 100)
        print(loading_line, f"{percent}%", end="\r", flush=True)
        time.sleep(0.1)

    time.sleep(2)