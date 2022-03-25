###LU base component. Components added after they have been created and tested###


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
    print()


# Number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
    "please enter a number between {} and {}\n".format(low, high)


    while True:
        try:
            response = int(input(question))


            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here...
played_before = yes_no ("Have you played this game before: ")

if played_before == "No":
    instructions()


# Ask the user how much they want to play with
user_balance = num_check("How much would you like to play with: $", 1, 10)
print(f"Your playing with ${user_balance}")
