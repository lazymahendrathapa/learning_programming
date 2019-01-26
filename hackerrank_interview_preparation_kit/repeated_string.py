def repeated_string(s, n):
    
    count = s.count('a')

    rep = int(n / len(s))

    count *= rep

    count += s[:n%len(s)].count('a')
    
    return count

if __name__ == '__main__':
    s = input()
    n = int(input())

    result = repeated_string(s, n)

    print(result)

