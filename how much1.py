### Component 2 (how much)
# Ask user how much they want to play with and check that the input is a valid integer between 1 and 10
# If it is, this will become the balance of their account


user_balance = int(input("How much do you want to play with (Must be a "
                         "whole number between 1 and 10): $ "))

# Keep asking until a valid amount is entered
while not 1 <= user_balance <= 10:
    print("Invalid answer. Enter an integer between 1 and 10")
    # Ask for the input
    user_balance = int(input("How much do you want to play with: $"))

print(f"Your balance is ${user_balance}")








