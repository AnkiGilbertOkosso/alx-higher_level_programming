#!/usr/bin/python3
for n in reversed(range(97, 123)):
    print("{:c}".format(n if (n % 2 == 0) else (n - 32)), end='')
