def counting_sort(array, maxval=200):

    n = len(array)

    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array


def find_median(array):
    l = counting_sort(array)
    l_len = len(l)

    if l_len < 1:
        return None

    if l_len % 2 == 0:
        return (l[(l_len-1)//2] + l[(l_len+1)//2]) / 2.0
    else:
        return l[(l_len - 1)//2]

def activity_notifications(expenditure, d):
    
    count = 0

    for i in range(d, len(expenditure)):

        if i< d:
            continue
              
        arr = expenditure[i-d:i]
        
        median = find_median(arr)
          
        if  expenditure[i] >= 2 * median:
            count += 1
    
    return count

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])
    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activity_notifications(expenditure, d)

    print(result)
