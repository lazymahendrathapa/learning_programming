def find_number(arr, k):

    if k in arr:
        return 'YES'

    else:
        return 'NO'

if __name__ == '__main__':
    n = int(input()) 
    
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    k = int(input())

    print(find_number(arr, k))
