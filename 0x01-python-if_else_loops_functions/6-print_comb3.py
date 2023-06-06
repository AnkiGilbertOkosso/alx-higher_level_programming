#!/usr/bin/python3
for numb in range(100):
    if int(numb / 10) != numb % 10 and int(numb / 10) < numb % 10:
        print("{}{}".format(int(numb / 10), numb % 10), end="")
        if (numb != 89):
            print(", ", end="")
print("")
