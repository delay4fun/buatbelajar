from itertools import combinations
a = [1,4,9,16,25,36,49,64,81,100]

for i in range(len(a)):
    for x in combinations(a,i+1):
        if sum(x) == 100:
            print(list(x))
           
