def count_swaps(a):
    length = len(a)
    
    number_of_swap = 0

    for i in range(length):
        for j in range(length - 1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                number_of_swap += 1
    
    print(f'Array is sorted in {number_of_swap} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    count_swaps(a)


