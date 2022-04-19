import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

while play_again != "x":
    rounds_played += 1
    number = random.randint(1, 100)

    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4

    elif 6 <= number <= 36:
        token = "Donkey"
        balance -= 1

    else:
        if number % 2 == 0:
            token = "Zebra"
            balance -= 0.5

        else:
            token = "Horse"
            balance -= 0.5

    # Output
    print(f"Round {rounds_played}. Token {token}. Balance ${balance:.2f}")
    if balance < 1:
        print("\nSorry you are out of money")
    else:
        play_again = input("\nDo you want to play again?\n<enter> to play"
                           " again or 'x' to exit").lower()
        print()

    print("Thanks for playing")
    print(f"You started with ${TEST_AMOUNT:.2f}")
    print(f"You finished with ${TEST_AMOUNT:.2f}")
    print("Goodbye")

