#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    args = sys.argv[1:]

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
