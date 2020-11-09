import random
import math
from random import sample
import numpy as np
import scipy.stats as st
import statistics
from Calculator import Calculator

print("\n")
print("\n")

# Random Generator function
#
# 1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
print ("Generating random number integer (without a seed):")
print(random.randrange(100,200))

print ("Generating random number decimal (without a seed):")
print(round(random.uniform(1,10),4))

print("\n")
print("------------------------------------------------------")
print("\n")

# 2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

print ("Generating random number integer (with a seed):")
random.seed(10)
print(random.randint(5,50))
print ("Generating random number decimal (with a seed):")
random.seed(10.0)
print(round(random.uniform(1,30),4))

print("\n")
print("------------------------------------------------------")
print("\n")

# 3a. Generate a list of N random numbers without a seed and between a range of numbers - Both Integer and Decimal

randomA = []
randomB = []
for i in range(0,30):
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

# 3b. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal

randomX = []
randomY = []
for i in range(0,30):
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

# Population Sampling functions
#
# 1. Simple random sampling
print("Simple Random Sampling from Integer without a Seed list:\n")
simpleA= sample(randomA,15)
print(simpleA)
print("\n")
print("Simple Random Sampling from Float without a Seed list:\n")
simpleB= sample(randomB,15)
print(simpleB)

print("\n")
print("------------------------------------------------------")
print("\n")
# 2. Confidence Interval For a Sample

print("Confidence Interval For a Sample from Integer without a Seed List")
confidenceInterval= st.t.interval(alpha=0.95, df=len(simpleA)-1, loc=np.mean(simpleA), scale=st.sem(simpleA))
print(confidenceInterval)

print("\n")
print("------------------------------------------------------")
print("\n")

# 3. Margin of Error

n = random.choice(simpleA)
z = Calculator.zscore(randomA)
t = Calculator.std1(randomA)

print("Margin of Error: ")

print(Calculator.margin_of_error(n, z, t))

print("\n")
print("------------------------------------------------------")
print("\n")

# Cochran’s Sample Size Formula

p = random.choice(simpleB)
e = random.choice(simpleB)

print("Cochran's Sample size formula")
print(Calculator.cochran(z, p, e))

print("\n")
print("------------------------------------------------------")
print("\n")

# How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
width = random.choice(simpleB)
a = confidenceInterval[0]/2
b = Calculator.zscore(confidenceInterval)
p = width/2
q = 0.50
p2 = 1-q
c = q*p2
d = a / b
e = d * d
Final = c*e
print("How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation):")
print(Final)

print("\n")
print("------------------------------------------------------")
print("\n")

# Descriptive Statistics functions - PRIYESHA

print("Descriptive Statistics functions: \n")
# Calculator.mean()
a = [1,2,3,4,5]
print(Calculator.mean1(a))

print("mean:")

print("\n")
print("------------------------------------------------------")
print("\n")

print("median:")
a = [1,2,3,4,5,6]
print(Calculator.median1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("mode:")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.mode1(a))

print("\n")
print("------------------------------------------------------")
print("\n")

print("variance")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.variance1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("standardDeviation")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.std1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("zscore:")
a = [1,1,2,3,5,6,11,7,5,5,8,10,13,13]
print(Calculator.zscore(a))

print("\n")
print("------------------------------------------------------")
print("\n")

print("Exception divide by 0 using a randomchoice value:")

while True:
    try:
        x = randomchoice1/0
        continue
    except:
        print("error cannot divide by 0")
        break
        exit(1)

print("\n")
print("------------------------------------------------------")
print("\n")


print("Exception for empty list:")

while True:
    try:
        empList = []
        x = empList/randomchoice1
    except:
        print("Error empty list")
        break
        exit(1)



