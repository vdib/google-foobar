import cProfile
import random

def solution2(x, y):
    return (sum(x) - sum(y)) * (len(x) - len(y))

def solution(x, y):
    if(len(x) > len(y)):

        sortedL = sorted(x)
        sortedS = sorted(y)

    else:
        sortedL = sorted(y)
        sortedS = sorted(x)

    for l, s in zip(sortedL, sortedS):
        if(l != s):
            return l


x = []
y = []
# num = random.randint(1, 1000000)
num = 1000000
num2 = num + 1
for i in range(num):
    x.append(random.randint(1, 1000000))
for i in range(num2):
    y.append(random.randint(1, 1000000))

def test1():
    # for x1,y1 in zip(x, y):
    solution(x,y)

def test2():
    solution2(x,y)

cProfile.run('test1()')
cProfile.run('test2()')