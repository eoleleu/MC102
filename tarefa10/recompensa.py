'''contador = list()

def calc_prob(p, n):
    
    if n == 1:
        return p
    else:
        return calc_prob(p * 1/6, n-1) + p

def prob(n, x, soma, p):
    if x == soma:
        return p
    if n == 0:
        return 0
    for i in range(1,7):
        aux = prob( n - 1, x, soma + i, p * 1/6)
        contador.append(aux)
        if aux != 0:
            break
    
    return 0

def main():
    n, x = input().split()
    n = int(n)
    x = int(x)
    #resultado = calc_prob(1/6, x)
    prob(n, x, 0, 1) 
    print(f'{sum(contador):.3f}')
main()'''

def calcular_probabilidade(n, x):
    if n == 0:
        return 0
    if n >= 1:
        aux = 0

        if x == 1:
            aux += 1/6
        elif x > 1:
            aux += 1/6*calcular_probabilidade(n-1, x-1)
        if x == 2:
            aux += 1/6
        elif x > 2:
            aux += 1/6*calcular_probabilidade(n-1, x-2)   
        if x == 3:
            aux += 1/6
        elif x > 3:
            aux += 1/6*calcular_probabilidade(n-1, x-3)
        if x == 4:
            aux += 1/6
        elif x > 4:
            aux += 1/6*calcular_probabilidade(n-1, x-4) 
        if x == 5:
            aux += 1/6
        elif x > 5:
            aux += 1/6*calcular_probabilidade(n-1, x-5)   
        if x == 6:
            aux += 1/6
        elif x > 6:
            aux += 1/6*calcular_probabilidade(n-1, x-6) 

        return aux 

def main():

    n, x = input().split()
    n = int(n)
    x = int(x)

    resultado = calcular_probabilidade(n, x)
    print(f'{resultado:.3f}')
main()