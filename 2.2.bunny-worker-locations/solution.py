import cProfile
import random

test = []
for i in range(1000000):
    test.append((random.randint(1, 100000), (random.randint(1, 100000))))

def solution(x, y):
    return (y * (y - 1))/2 + (x * (x - 1)) / 2 + (x - 1) * y + 1

def solution_max(x,y):
    return (y-2)*(y-1)*0.5+(x*y)+(x-1)*x*0.5

def solution_simplified(x, y):
    return (y**2 + x**2 - x - 3*y + 2*x*y + 2) / 2

#simons
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

def test_max():
    for x, y in test:
        solution_max(x,y)

def test_simplified():
    for x, y in test:
        solution_simplified(x,y)

# print(solution(*test[100]), solution2(*test[100]), solution_max(*test[100]), solution_simplified(*test[100]))
cProfile.run('test_simplified()')
cProfile.run('test1()')
# cProfile.run('test2()')
cProfile.run('test_max()')