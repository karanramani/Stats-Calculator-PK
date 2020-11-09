import random

print("\n")
print("\n")

# Random number without a seed (SINGLE)
print ("Generating random number integer (without a seed):")
print(random.randrange(100,200))

print ("Generating random number decimal (without a seed):")
print(round(random.uniform(1,10),4))

print("\n")
print("------------------------------------------------------")
print("\n")

# Random number with a seed (SINGLE)
print ("Generating random number integer (with a seed):")
random.seed(10)
print(random.randint(5,50))
print ("Generating random number decimal (with a seed):")
random.seed(10.0)
print(round(random.uniform(1,30),4))
print("\n")
print("------------------------------------------------------")
print("\n")

# Random number list without a seed
randomA = []
randomB = []
for i in range(0,10):
    x = random.randrange(100,200)
    y = round(random.uniform(1,10),4)
    randomA.append(x)
    randomB.append(y)

print("Random Numbers list Without SEED: \n")
print("Integer Numbers: ")
print(randomA)
print("\nFloat Numbers: ")
print(randomB)
print("\n")
print("------------------------------------------------------")
print("\n")

# Random Number List with a seed
randomX = []
randomY = []
for i in range(0,10):
    random.seed(10)
    a = random.randint(5,50)
    b = round(random.uniform(1,10),4)
    randomX.append(a)
    randomY.append(b)

print("\nRandom Numbers list With SEED: \n")
print("Integer Numbers: ")
print(randomX)
print("\nFloat Numbers: ")
print(randomY)
print("\n")
print("------------------------------------------------------")
print("\n")

# 4. Select a random item from a list
    # Random item from list without seed
randomchoice1 = random.choice(randomA)
randomchoice2 = random.choice(randomB)

print("Random Choice 1 (From Integer list without seed): ")
print(randomchoice1)
print("Random Choice 2 (From Float list without seed): ")
print(randomchoice2)
print("\n")
print("------------------------------------------------------")
print("\n")

print("\n")

# 5. Set a seed and randomly.select the same value from a list
randomchoicewseed1 = random.choice(randomX)
randomchoicewseed2 = random.choice(randomY)

print("Random Choice 1 (From Integer list with seed): ")
print(randomchoicewseed1)

print("Random Choice 2 (From Float list with seed): ")
print(randomchoicewseed2)

print("\n")
print("------------------------------------------------------")
print("\n")

# 6. Select N number of items from a list without a seed
N = 10
print("N number of items from a list without a seed(Integer):")
print(random.sample(randomA, N))
print("\n")
print("N number of items from a list without a seed(Float):")
print(random.sample(randomB, N))
print("\n")

print("\n")
print("------------------------------------------------------")
print("\n")

# 7. Select N number of items from a list with a seed
print("N number of items from a list with a seed(Integer):")
print(random.sample(randomX, N))
print("\n")
print("N number of items from a list with a seed(Float):")
print(random.sample(randomY, N))

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")