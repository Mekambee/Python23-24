import time
import sys
if __name__ == "__main__":
    argv = sys.argv[1]
    percent = 0
    loading_line = '|' + '-'*int(argv) + '|'
    for i in range(1, int(argv)+1):
        loading_line = loading_line[:i] + '=' + loading_line[i+1:]
        percent += 2
        print(loading_line, f"{percent}%", end="\r", flush=True)
        time.sleep(0.1)
    time.sleep(2)