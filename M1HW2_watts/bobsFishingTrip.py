# -*- coding: utf-8 -*-
"""
CSC 221
Bob's fishing trip
Jesse Watts
Goal: Gold
30 Jan 19
"""

"""Write a program that asks Bob how many fish he caught over a 3 day period
and calculates the average number of fish caught per day."""


"Use a for and range statement to get Bob's number of fish." 
for i in range (1):
    fishFri = int(input("Bob, how many fish did you catch on Friday? "))
    fishSat = int(input("Bob, how many fish did you catch on Saturday? "))
    fishSun = int(input("Bob, how many fish did you catch on Sunday? "))
    
    "Calculate the total number of fish caught."
    totalFish = fishFri + fishSat + fishSun

"Display the total and average number of fish Bob caught."
print()
print("Bob, you caught a total of ", totalFish, "fish.")
print()
print("Bob, the average number of fish you caught was {0:.1f}".format(totalFish / 3), "fish per day.")
    
    
        
