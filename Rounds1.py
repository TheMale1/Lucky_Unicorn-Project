import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

while play_again!= "x":
    rounds_played += 1
    number = random.randint(6, 36)

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

    print(f"Round {rounds_played}. Token: {token}. Balance: {balance:.2f}")
    if balance < 1:
        print("\nSorry but you have run out of money")

