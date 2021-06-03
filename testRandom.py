import random
from time import sleep

lis = [0]
value1 = 0
value2 = list('10'*70)

for i in lis:
    value1 += 1
    lis.append(value1)
    random.shuffle(value2)
    sleep(0.5)
    print (''.join(value2))
    
