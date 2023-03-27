def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fatorial(n-1)

def combinations(n,k):
    
    result = (fatorial(n)) / (fatorial(k) * fatorial(n-k))
    return result

a = list(map(int, (input().split())))
n = a[0]
k= a[1]

print(int(combinations(n,k)))  