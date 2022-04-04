# Component 3 generates tokens to play with V2


import random

tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]
balance = 10

# Test loop to generate 20 tokens
for token in range(20):
    token = random.choice(tokens)
    print(token, end='\n')


    # Adjust balance
    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1
    else:
        balance -= .50

    #Output
    print(f"Token: {token}, Balance: ${balance}")




