# Component 3 generates tokens to play with V3


import random

tokens = ["Unicorn",
         "Horse", "Horse", "Horse",
          "Donkey", "Donkey", "Donkey",
           "Zebra", "Zebra", "Zebra"]

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Test loop to generate 20 tokens
for token in range(10):
    token = random.choice(tokens)
    print(token, end='\n')

    # Adjust balance
    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1
    else:
        balance -= .50

    # Output
    print(f"Starting balance was ${STARTING_BALANCE:.2f}")
    print(f"Final balance is {balance:.2f}")

