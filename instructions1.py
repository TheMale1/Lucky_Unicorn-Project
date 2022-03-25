###Took function from checker function1 as the basis for this new function
# which incorparates both yes/no and show instructions


# Yes/No checking function
def yes_no(question_text):
    while True:


        # Ask the user if they have played the game before
         answer = input(question_text).lower()
        # If they say yes, output 'Program continues'
         if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no, output 'display instructions'
         elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # else show 'error'
         else:
            print("Invalid answer. Please enter yes/no")


         print(f"You entered '{answer}' ")


# Function to display instructions
def instructions():
    print("========== How to Play ==========")
    print()
    print("The rules of the game will go here")
    print()
    print("=================================")
    print("Program continues")
    print()

# Main routine goes here...
played_before = yes_no ("Have you played this game before: ")

if played_before == "No":
    instructions()
else:
    print()
    print("Program continues")

