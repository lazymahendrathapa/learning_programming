from collections import defaultdict

def min_bribes(q):

    count = defaultdict(int)
    
    res = sorted(q)

    for i in range(len(q)):
        for j in range(len(q)-1):

            if q[j+1] < q[j]:

                q[j+1], q[j] = q[j], q[j+1]
                count[q[j+1]] += 1
    
        if res == q:
            break

    result = count.values()
    
    for i in result:
        if i > 2:
            print('Too chaotic')
            return
    
    print(sum(result))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))

        min_bribes(q)
