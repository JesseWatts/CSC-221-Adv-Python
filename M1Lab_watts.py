# -*- coding: utf-8 -*-
"""
CSC 221
M1 Lab
Jesse Watts
23 Jan 19
"""

def main():
    
    """ Bottles of beer song"""
    # 1 use a var
    bottles = 99
    
    # Use a while loop
    while bottles >= 0:
        print(bottles, "bottles of beer on the wall.")
        bottles = bottles - 1
        
    # 2 use a for loops
    """
    for beer in range (99,-1,-1):
        print(beer, "beers")
    """
    
        
        
        
if __name__ == "__main__":
    main()