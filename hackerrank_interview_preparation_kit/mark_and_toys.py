def maximum_toys(prices, k):
    prices = sorted(prices)

    result = 0
    count = 0

    for i in prices:

        result += i

        if result < k:
            count += 1
        else:
            break

    return count


if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximum_toys(prices, k)

    print(result)
