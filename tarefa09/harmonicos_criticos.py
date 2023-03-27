def calcular_thd_harmonicos_criticos(lista_tensoes, thd_de_todos):
    i = 1
    thd = 0
    thd_80 = thd_de_todos*0.8
    somaPow = 0

    while thd < thd_80:
        somaPow = somaPow + lista_tensoes[i]**2
        thd = somaPow**(1/2)
        thd = (thd/(lista_tensoes[0]))*100
        i+=1

    return thd, i-1

def calcular_thd_total(lista_tensoes):
    j = 0
    for i in lista_tensoes[1:]:
        j = j + i**2
    j = j ** (1/2)
    j = (j/(lista_tensoes[0]))*100
    return j

def main():
    #print(input())
    lista_tensoes = input().split()
    lista_tensoes = list(map(int, lista_tensoes))

    #print(lista_tensoes)

    thd_de_todos = calcular_thd_total(lista_tensoes)
    #print(f'{thd_de_todos:.2f} %')

    thd_de_harmonicos_criticos, n_criticos = calcular_thd_harmonicos_criticos(lista_tensoes, thd_de_todos)

    print(f'Número de harmônicos críticos: {n_criticos}')
    print(f'THD de harmônicos críticos: {thd_de_harmonicos_criticos:.2f} %')
    print(f'THD de todos os harmônicos: {thd_de_todos:.2f} %')
main()