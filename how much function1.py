### Component 2 (How much) 4
#Changing v3 into a function
#also needed to change user_balance to the more generic variable 'response'
#and to change the condition and position of the number comparison into the loop
#to make the function recyclable


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


# Main routine
user_balance = num_check("How much would you like to play with: $", 1, 10)
print(f"Your playing with ${user_balance}")
