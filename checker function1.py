### Yes/No checking function based on checker test3


# Functions go here
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

# Main routine goes here
show_instructions = yes_no("Have you played this game before: ")
print(f"You entered '{show_instructions}' ")
print()
having_fun = yes_no("Are you having fun: ")
print(f"You entered '{having_fun}' ")
