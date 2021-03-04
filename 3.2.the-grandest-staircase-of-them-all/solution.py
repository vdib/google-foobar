# import math


def solution(n):

    s = [[0] * (n+1) for i in range(n+1)]

    s[0][0] = 1

    for total in range(1, n+1):
        for h in range(n+1):
            s[total][h] = s[total-1][h]

            if h >= total:
                s[total][h] += s[total - 1][h - total]

    return s[n][n] - 1


print(solution(9))
