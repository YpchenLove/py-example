import random
print(random.choice(range(8, 10)))

print(random.random())

list = [1, 2, 3, 4, 5]

random.shuffle(list)

print(list)
print(random.uniform(2, 3))
print("randrange(1,100, 2) : ", random.randrange(1, 100, 20))
