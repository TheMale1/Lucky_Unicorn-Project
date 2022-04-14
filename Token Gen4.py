# Component 3 generates tokens to play with V3


import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE


for token in range(1, 10):
    number = random.randint(1,100)

    # adjust balance
    # if number between 1 and 5
    # user gets a unicorn
    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4

        #if the random number is between 6 and 36
        #(subtract 1 from the balance)
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

    print(f"Token: {token}, Balance: ${balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")






