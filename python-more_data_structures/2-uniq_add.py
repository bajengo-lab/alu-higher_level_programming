#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = []

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)

    total = 0
    for number in unique_numbers:
        total += number

    return total
