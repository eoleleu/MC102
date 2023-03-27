n_doadores = int(input())
soma_do_peso = 0
aptoM = 0
aptoF = 0

for _ in range(n_doadores):
    peso, sexo, g_or_a, n_doacoes, dias_decorridos = input().split()
    peso = float(peso)
    n_doacoes = int(n_doacoes)
    dias_decorridos = int(dias_decorridos)
    if peso >= 50:
        if sexo == 'M':
            if n_doacoes <= 4:
                if dias_decorridos > 60:
                    aptoM = aptoM + 1
                    soma_do_peso = soma_do_peso + peso
        if sexo == 'F':
            if g_or_a == 'N':
                if n_doacoes <= 3:
                    if dias_decorridos > 90:
                        aptoF += 1
                        soma_do_peso += peso

if (aptoF == 0) and (aptoM == 0):
    media = 0
else:
    media = soma_do_peso / (aptoF + aptoM)

print(f'Número de doadores aptos do sexo M: {aptoM}')
print(f'Número de doadores aptos do sexo F: {aptoF}')
print(f'Peso médio de doadores aptos: {media:.1f}')


            
    

        

    

