import math
import random
import numpy as np

start=0


lst=sorted(list(set(np.random.randint(1, 1000, random.randint(10,100)))))

end=len(lst)-1

print(lst)

x=int(input())  

while start<=end:
    n=(start+end)//2
    if lst[n]==x:
        print(f'Find: {n} {lst[n]}')
        break
    elif lst[n]<x:
        start=n+1
    else:
        end=n-1
