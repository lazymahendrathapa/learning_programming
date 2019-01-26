from collections import Counter

def sock_merchant(n, ar):

    val = dict(Counter(ar))

    count = 0
    for v in val.values():
        count += int(v / 2)
    
    return count 

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    print(result)
