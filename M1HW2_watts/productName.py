# -*- coding: utf-8 -*-
"""
CSC 221
Product name
Jesse Watts
Goal: Gold
30 Jan 19
"""

def main():
    """ Program asks user for name of product, price, and quantity.
    Display price before tax, and the total cost after adding 4% state
    and 2% county sales tax."""
    
    # Determine the variables
    itemName = (str(input("What is the name of the product? ")))
    itemPrice = (float(input("How much does it cost? ")))
    itemQuantity = (int(input("How many do you want? ")))
    
    # The state and county taxes should be constants
    STATE_TAX = .04
    COUNTY_TAX = .02
    
    # Calculate the subtotal
    subTotal = itemQuantity * itemPrice
   
    
    # Determine the state tax
    stateTax = subTotal * STATE_TAX
    
    # Determine the county tax
    countyTax = subTotal * COUNTY_TAX
    
    # Determine the total cost
    totalCost = subTotal + stateTax + countyTax
    
    # Display the prices
    # Use a currency format to round to 2 decimal places.
    print()
    print("You ordered ",itemQuantity, itemName,".")
    print()
    print("The subtotal for your purchase is $",subTotal,".")
    print()
    print("The state tax applied is $ {0:.2f}".format(stateTax),".")
    print()
    print("The county tax applied is $ {0:.2f}".format(countyTax),".")
    print()
    print("The total cost of your purchase is ${0:.2f}".format(totalCost),".")
    
# Run the program
main()
    
    
    
    

