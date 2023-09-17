import random

numList = [i for i in range(-50, 50)]

for i in range(50):
    profits = random.choices(numList, k = 15)
    print(profits)