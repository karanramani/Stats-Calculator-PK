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
