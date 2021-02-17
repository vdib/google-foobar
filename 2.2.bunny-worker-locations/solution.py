import cProfile
import random

test = []
for i in range(1000):
    test.append((random.randint(1, 100000), (random.randint(1, 100000))))

def solution(x, y):
    return (y * (y - 1))/2 + (x * (x - 1)) / 2 + (x - 1) * y + 1

def solution2(x, y):
    num = 1.0

    for i in range(y):
        num += i

    for i in range(1, x):
        num += y + i

    return num

def test1():
    for x, y in test:
        solution(x,y)

def test2():
    for x, y in test:
        solution2(x,y)

cProfile.run('test2()')
cProfile.run('test1()')