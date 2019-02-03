def hour_glass(arr):
    
    """
    arr = []
    arr.append(list(map(int,'1 1 1 0 0 0'.split())))
    arr.append(list(map(int,'0 1 0 0 0 0'.split())))
    arr.append(list(map(int,'1 1 1 0 0 0'.split())))
    arr.append(list(map(int,'0 0 2 4 4 0'.split())))
    arr.append(list(map(int,'0 0 0 2 0 0'.split())))
    arr.append(list(map(int,'0 0 1 2 4 0'.split())))
    """

    h, w = len(arr), len(arr[0])
    
    sums = []

    for i in range(h - 2):
        for j in range(w - 2):
            sums.append(sum(arr[j][i:i+3]) + sum(arr[j+2][i:i+3]) + arr[j+1][i+1])

    return max(sums)
    
    
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hour_glass(arr)

    print(result)
