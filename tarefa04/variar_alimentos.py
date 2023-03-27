# lê os alimentos que juan gosta
alimentos = input().split()

# lê o número de dias do cardapio
n = int(input())

cardapios = []

# armazena o cardapio de cada dia em uma lista chamada 'cardapios'
for _ in range(n):
    a = input().split()
    cardapios.append(a)

cardapios_processado = []

# separa os alimentos que Juan gosta com os que ele não gosta 
for cardapio in cardapios:
    # cria um cardapio provisório onde armazena apenas as datas
    cardapio_provisorio = [cardapio[0]]
    # compara cada alimento do cardapio original e armazena no cardapio provisorio apenas os que Juan gosta
    for x in cardapio[1:]:
        if x in alimentos:
            cardapio_provisorio.append(x)
    cardapios_processado.append(cardapio_provisorio)


cardapios = cardapios_processado # cardapios agora tem apenas alimentos que Juan gosta 

maximo = 0
par_de_dias = [0, 1]

# compara cada dia do cardapio com todos os de baixo
for i in range(len(cardapios)):
    for j in range(i + 1, len(cardapios)):
        # conta o número de elementos diferentes entre carpadios[i] e carpadios[j] sem contar as datas
        n = len(cardapios[i][1:]) + len(cardapios[j][1:])
        # evitar a repeticao de itens
        for a in cardapios[i][1:]:
            if a in cardapios[j][1:]:
                n = n - 1
        # se essa contagem foi maior que maximo, então maximo recebe essa contagem
        if n > maximo:
            maximo = n
            par_de_dias = [i, j] # recebe os indices das listas, em que a soma dos alimentos que Juan gosta é máximo


print(f'Juan pode comer {maximo} alimentos diferentes')

# arrumando a sintaxe para passar no teste do bot
for x in range(len(cardapios[par_de_dias[0]])):
    print(cardapios[par_de_dias[0]][x], end=" ")

print('')

for x in range(len(cardapios[par_de_dias[1]])):
    print(cardapios[par_de_dias[1]][x], end=" ")


