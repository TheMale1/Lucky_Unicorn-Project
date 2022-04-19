###LU base component. Components added after they have been created and tested###
import random

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
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with. It must be a number between 1-10")
    print()
    print("Then press <enter> to play. You will get a random token which might"
          " be a Horse, a Zebra, a Donkey, or a Unicorn")
    print()
    print("It will cost you $1 to play each round but, depending on your prize, you could "
          " win some of your money back.")
    print("These are the payout amounts:\n"      
          "\tUnicorn: $4 (Increases balance by $4)\n"
          "\tHorse/Zebra: $0.5 (Decreases balance by $0.5)\n"
          "\tDonkey: $1 (Decreases balance by $1)\n")
    print("\nSee if you can avoid the Donkeys and get the Unicorns to finish"
          " with more money than you started!\n")

    print("*" * 50)
    print()


import random

# Function to generate random balance
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    while play_again != "x":
        rounds_played += 1
        print(formatter(".", f"Round {rounds_played}"))
        number = random.randint(1, 100)

        if 1 <= number <= 5:
            token = "Unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got a Unicorn"))
            print()
            print(f"Your balance is ${balance}")

        elif 6 <= number <= 36:
            token = "Donkey"
            balance -= 1
            print(formatter("#", "Bad luck, you got a Donkey!"))
            print()
            print(f"Your balance is ${balance}")

        else:
            if number % 2 == 0:
                token = "Zebra"
                balance -= 0.5
                print(formatter("@", "You got a Zebra. Better luck next time."))
                print()
                print(f"Your balance is ${balance}")

            else:
              token = "Horse"
              balance -= 0.5
              print(formatter("%", "Oh No! You got a Horse"))
              print()
              print(f"Your balance is ${balance}")

    # Output
        if balance < 1:
            print("\nSorry you are out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play again\n<enter> to"
                            " play"
                             " again or 'x' to exit ").lower()
        print()
    return balance


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


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

# Main routine goes here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no ("Have you played this game before: ")

if played_before == "No":
    instructions()


# Ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with: $", 1, 10)
print(f"Your playing with ${starting_balance}")

starting_balance = 10
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"You finished with ${closing_balance:.2f}")
print(formatter("*", "Better luck next time"))
