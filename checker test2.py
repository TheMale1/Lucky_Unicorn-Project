###LU Yes / No
# Simplifies the input by converting it to lower case. Also accepts y or n as  abbreviations.
# Prints result of user choice as well as input - for testing
###

# Ask the user if they have played the game before
show_instructions = input("Have you played this game before (yes/no): ").lower()
# If they say yes, output 'Program continues'
if show_instructions == "yes" or "y":
    print("Program continues")

# If no, output 'display instructions'
elif show_instructions == "no" or "n":
    print("Display instructions")

# else show 'error'
else:
    print("Invalid answer. Please enter yes/no")


print(f"You entered '{show_instructions}' ")
