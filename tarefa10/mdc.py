def maximo_divisor_comum(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return maximo_divisor_comum(a, b)  

def main():
    a = list(map(int, (input().split())))
    n = a[0]
    k= a[1]
    resultado = maximo_divisor_comum(n, k)
    print(resultado)
main()