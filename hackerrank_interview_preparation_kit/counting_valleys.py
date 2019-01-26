def counting_valleys(n, s):
    
    if not s:
        return 0

    up_count= 0
    down_count= 0
    
    valley_count = 0

    for c in s:

        if up_count == 0 and down_count == 0 and c == 'U':
            up_count +=1 
        
        elif up_count == 0 and down_count == 0 and c == 'D':
            down_count -=1 
        
        elif up_count == 0:
            if c == 'U':
                down_count += 1 
            elif c == 'D':
                down_count -= 1
            
            if down_count == 0:
                valley_count += 1

        elif down_count == 0:
            if c == 'U':
                up_count += 1 
            elif c == 'D':
                up_count -= 1
        
    return valley_count


if __name__ == '__main__':
    n = int(input())
    s = input()

    result = counting_valleys(n, s)

    print(result)
