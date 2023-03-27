def busca_binaria(lista, i, j, n):
 

    if i<=j:
        k = (j + i) // 2
    
        if lista[k] == n:
            return 1
 
        elif lista[k] > n:
            return busca_binaria(lista, i, k - 1, n)
 
        else:
            return busca_binaria(lista, k + 1, j, n)
 
    else:
        return -1
def main():
    lista = list(map(int,input().split()))
    lista = sorted(lista)
    n = int(input())
    soma = 0
    while True:
        result = busca_binaria(lista, 0, len(lista)-1, n)
    
    
        if result == 1:
            soma += 1
            lista.remove(n)
        else:
            break

    print(soma)

main()

