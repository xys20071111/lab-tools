import os,sys

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            filename = line.strip()
            os.unlink(filename)