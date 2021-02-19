def solution(n):
    n = int(n)
    i = 0
    while(n != 1):
        if n & 1:
            if ((n + 1) & 0b11 == 0) and n > 3:
                n += 1
                i += 1
            else:
                n -= 1
                i += 1
        else:
            n = n >> 1
            i += 1
    return i
