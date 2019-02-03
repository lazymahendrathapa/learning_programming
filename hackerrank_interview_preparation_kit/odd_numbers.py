def odd_number(l, r):
    result = []

    for i in range(l, r + 1):
        if i % 2 == 1:
            result.append(i)
    
    return result

if __name__ == '__main__':
    l = int(input().rstrip())
    r = int(input().rstrip())

    result = odd_number(l, r)

    print('\n'.join(map(str,result)))
