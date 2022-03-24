# Ask the user if they have played the game before
show_instructions = input("Have you played this game before (Yes/No) : ")
# If they say yes, output 'Program continues'
if show_instructions == "Yes":
    print("Program continues")

# If no, output 'display instructions'
elif show_instructions == "No":
    print("Display instructions")

# else show 'error'
else:
    print("Invalid answer. Please enter Yes/No")


