import itertools
import math


def minimum_absolute_difference(arr):

    a = sorted(arr)

    res = math.inf

    for x, y in zip(a, a[1:]):
        r = abs(x - y)

        if r < res:
            res = r

    return res


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))

    result = minimum_absolute_difference(arr)

    print(result)
