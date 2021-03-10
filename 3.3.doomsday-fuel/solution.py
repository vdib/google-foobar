from __future__ import division
import fractions as f
from functools import reduce


def matrix_squared(mat):
    size = len(mat)

    result = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat[i][k] * mat[k][j]
    return result


def solution(m):
    '''
    The problem is related to the Markov Chain with the 'terminal' state being the 'absorbing' state
    The output should be the probability of each absorbing state in fraction form as number of steps reach infinity
    = A^inf * A0
    In this solution we're just raising the matrix to the power of 1024 and approximate
    '''
    terminal_states = []
    # create probability matrix
    mat_prob = [[0 for i in range(len(m))] for i in range(len(m))]
    for v_from in range(len(m)):
        if sum(m[v_from]) != 0:
            mat_prob[v_from] = [i / sum(m[v_from]) for i in m[v_from]]
        else:
            terminal_states.append(v_from)
            mat_prob[v_from][v_from] = 1

    for i in range(10):
        mat_prob = matrix_squared(mat_prob)

    output = [f.Fraction(mat_prob[0][i]).limit_denominator() for i in terminal_states]
    denoms = [n.denominator for n in output]
    gcd = reduce(lambda a, b: a*b//f.gcd(a, b), denoms)
    output = [int(n.numerator * (gcd / n.denominator)) for n in output]
    output.append(int(gcd))

    return output
