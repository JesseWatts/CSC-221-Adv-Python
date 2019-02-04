# -*- coding: utf-8 -*-
"""
CSC 221
M1HW1
Jesse Watts
Goal: Gold
23 Jan 19
"""

word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "beer on the wall.")
    print("Take one down,")
    print("pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num -1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()
