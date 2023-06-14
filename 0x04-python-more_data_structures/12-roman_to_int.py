#!/usr/bin/python3

def to_sub(data):
    sub = 0
    max_list = max(data)

    for n in data:
        if max_list > n:
            sub += n

    return (max_list - sub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lists = list(roman_number.keys())

    num = 0
    first_roman = 0
    data = [0]

    for i in roman_string:
        for n in lists:
            if n == i:
                if roman_number.get(i) <= first_roman:
                    num += to_sub(data)
                    data = [roman_number.get(i)]
                else:
                    data.append(roman_number.get(i))

                first_roman = roman_number.get(i)
    num += to_sub(data)

    return (num)
