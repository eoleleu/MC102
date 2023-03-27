def fatorial(n):
    if n == 0:
        return 1
    else:
        return fatorial(n-1)*n

def main():
    n = int(input())
    resultado = fatorial(n)
    print(resultado)
main()
