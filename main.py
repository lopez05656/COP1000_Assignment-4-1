"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.
charge = 35
EXTRA_CHARGE = 4
numChars = float(input("How many characters are in your customer's sign: "))
color = str(input("Please enter your customer's preferred sign text color: "))
woodType = str(input("Please Enter your customer's preferred wood type: "))

# Write assignment and if statements here as appropriate.
if numChars > 8:
    charge += (numChars - 5) * EXTRA_CHARGE

if woodType == str("Oak") or str("oak"):
    charge = charge + 20

#if woodType == str("Pine") or str("pine"):
    #charge = charge - 20

if color == str("Gold") or str("gold"):
    charge += 15

#if color == str("Black") or str("black"):
    #charge = charge + 5

# Output Charge for this sign.
print("Your total for this order is $" + str(charge))
