#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1

    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))

    if n >= 1:
        n = 0
        for arg in sys.argv:
            if n != 0:
                print("{}: {}".format(n, arg))
            n += 1
