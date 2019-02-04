# -*- coding: utf-8 -*-
"""
CSC 221
M1T1_Watts
Goal: Gold
16 Jan 2019
"""

def main():
    """
    Author: Watts, Jesse
    This program will calculate the
    largest fishing pole that can
    for diagonally in a box.
    """
    poleLength = 0;
    boxLength = 0;
    boxWidth = 0;
    
    # Determine the length of the pole, length and width of the box.
    poleLength = float(input("What is the length of the pole in feet?  "))
    boxLength = float(input("What is the box length in feet?  "))
    boxWidth = float(input("What is the box width in feet?  "))
    
    poleLength = poleLength**2
    boxLength = boxLength**2
    boxWidth = boxWidth**2
    
    # Get box dimensions
    boxSize = boxLength * boxWidth
    print()
    
    print("This box will hold a fishing pole up to",boxSize,
              "feet in length.")
    print()
    
    # Use a decision based statement to determine whether pole will fit.
    if poleLength <= boxSize:
        print("Your fishing pole will fit.")
        
    else:
        print("This box will not hold the fishing pole.")

main()