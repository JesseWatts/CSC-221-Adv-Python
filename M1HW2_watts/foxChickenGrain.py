# -*- coding: utf-8 -*-
"""
CSC 221
Fox, chicken, and grain
Jesse Watts
Goal: Gold
30 Jan 19
"""

def main():
    """main program.  Solves the fox, chicken, and grain problem."""
    # variables for the three actors
    # true is near, false is far
    fox = True
    chicken = True
    grain = True
    
    # start
    update(fox, chicken, grain)
    
    # Step 1
    fox = False
    update(fox, chicken, grain)
    
    # Step 2
    chicken = False
    update(fox, chicken, grain)
    
    # step 3
    grain = False
    update(fox, chicken, grain)
    
    

def update(fox, chicken, grain):
    """On each turn, prints out the position of each actor.
    input: position of fox, chicken, and grain (boolean)
    returns: none"""
    
    if fox == True:
        print("Fox is on the near side.")
    elif fox == False:
        print("Fox is on the far side.")
    elif chicken == True:
        print("Chicken is on the near side.")
    elif chicken == False:
        print("Chicken is on the far side.")
    elif grain == True:
        print("Grain is on the near side.")
    elif grain == False:
        print("Grain is on the far side.")
    else:
        print("Fox, chicken, and grain are on the far side.")
    
    

# Start the program
main()

