def jumping_on_clouds(c):

    jump = 0
    
    i = 0
    
    length = len(c)

    while i < length:
        

        j = i + 1
        k = i + 2
        
        if k < length and c[k] == 0:
            i = k

        else:
            i = j
        
        jump += 1
    
    return jump - 1

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    print(result)
