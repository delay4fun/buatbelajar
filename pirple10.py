# ## Introduction to Importing

# import random as r 

# # random.seed(1)
# randInt = r.randint(0 ,10)
# print(randInt)

# randFloat = r.random()
# print(randFloat)

# randUniform = r.uniform(1, 11)
# print(randUniform)

### ====================================
## Alternative Import Methods

# import random as r

# simpleList = [1,3,5,7,11]
# pickElement = r.choice(simpleList)
# print(pickElement)
# print(simpleList)
# r.shuffle(simpleList)
# print(simpleList)

### ======================================
## The Time Library

# import time

# currentTime = time.time()
# print("Hello")
# print("World")
# pastTime = time.time()
# print(pastTime - currentTime)

# print("1")
# time.sleep(3)
# print("2")

# for i in range(1, 11):
#     print(i)
#     time.sleep(1)


### ==========================
## The Math Library

import math

val = 3.14

sqrtVal = math.sqrt(val)
print(sqrtVal)

expVal = math.exp(val)
print(expVal)

## val is float
# factVal = math.factorial(val)
# print(factVal)

sinVal = math.sin(val)
print(sinVal)

floorVal = math.floor(val)
print(floorVal)

ceilVal = math.ceil(val)
print(ceilVal)
