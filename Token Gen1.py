# Component 3 generates tokens to play with V1


import random

tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]

# Test loop to generate 20 tokens
for token in range(20):
    token = random.choice(tokens)
    print(token, end='\n')



