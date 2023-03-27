# lê o número de alimentos que serão imputados
n = int(input())

lista_alimentos = []

refeicoes = []

proteina = 0.0
carboidrato = 0.0
gordura = 0.0

# lê cada linha e armazena o alimentos e os valores nutricionais na lista de alimentos
for _ in range(n):
    alimentos = input().split()
    lista_alimentos.append(alimentos)

# lê cada linha e armazena os refeicoes que Juan consumiu
for _ in range(3):
    ler_refeicoes = input().split()
    refeicoes.append(ler_refeicoes)

# compara as refeicoes de Juan com a lista de alimentos & armazena os valores nutricionais deles
for refeicao in refeicoes:
    for alimento in refeicao:
        for y in lista_alimentos:
            if y[0] == alimento:
                proteina = proteina + float(y[1])
                carboidrato = carboidrato + float(y[2])
                gordura = gordura + float(y[3])

# verifica se a quantidade de proteina está em falta ou excesso
if proteina < 140:
    p = 140 - proteina
    print(f'{p:.1f} gramas de proteína em falta')
else:
    pp = proteina - 140
    print(f'{pp:.1f} gramas de proteína em excesso ')

# verifica se a quantidade de carboidrato está em falta ou excesso
if carboidrato < 210:
    c = 210 - carboidrato
    print(f'{c:.1f} gramas de carboidrato em falta')
else:
    cc = carboidrato - 210
    print(f'{cc:.1f} gramas de carboidrato em excesso ')

# verifica se a quantidade de gordura está em falta ou excesso
if gordura < 56:
    g = 56 - gordura
    print(f'{g:.1f} gramas de gordura em falta')
else:
    gg = gordura - 56
    print(f'{gg:.1f} gramas de gordura em excesso ')
