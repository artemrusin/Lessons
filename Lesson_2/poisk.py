import math
import random
import numpy as np




'''lst=sorted(list(set(np.random.randint(1, 1000, random.randint(10,100)))))'''

def poisk_bin(start,finish,long,x):
    start-=1
    lst=sorted(list(set(np.random.randint(start, finish, long))))
    end=long-1
    while start<=end:
        n=(start+end)//2
        if lst[n]==x:
            print(f'Find: {n} {lst[n]}')
            break
        elif lst[n]<x:
            start=n+1
        else:
            end=n-1
    print('Элемента нет')


x=int(input())
y=int(input())
z=int(input())
w=int(input())

poisk_bin(x,y,z,w)


