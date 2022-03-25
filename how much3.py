### Component 2 (how much) 3
#More efficient method - includes valid range as teh basis of the while loop
# which eliminates the need tto use the 'valid'  variable

# Main routine
error = "That was not a valid input\n"
user_balance = 0

# Keep asking until a valid amount is entered
while not 1 <= user_balance <= 10:
    try:
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much would you like to play with: $"))
        print()

    except ValueError:
        print(error)

print(f"Your playing with ${user_balance}")
