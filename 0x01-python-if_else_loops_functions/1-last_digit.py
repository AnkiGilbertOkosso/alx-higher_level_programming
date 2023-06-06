#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10 if number >= 0 else ((-number % 10) * -1)
msg = f"last digit of {number} is {last_num}"

if last_num == 0:
    print(f"{msg} and is 0")
elif last_num > 5 and last_num % 10 != 0:
    print(f"{msg} and is greater thab 5")
else:
    print(f"{msg} and is less that 6 and not 0")
