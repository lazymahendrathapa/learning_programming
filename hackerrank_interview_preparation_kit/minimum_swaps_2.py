def minimum_swap(arr):
    count = 0
    sort = sorted(arr)

    for i in range(len(arr)-1):

        valid = arr[i:]
        min_val = sort[i]

        idx = valid.index(min_val) + i

        if i != idx:
            arr[i], arr[idx] = arr[idx], arr[i]

            count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swap(arr)

    print(res)
