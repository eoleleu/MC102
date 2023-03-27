#!python3

nome = input('Nome do doador(a): ')
idade = int(input('Idade: '))

if idade >= 16 and idade <= 60:
    if idade < 18:
        da = input('Possui documento de autorização (S/N)? ')
        if da == 'S' or da == 's':
            print('Doador apto. Encaminhar para a próxima etapa!')
        else:
            print('Doador não atende os requisitos de idade.')
    else:
        print('Doador apto. Encaminhar para a próxima etapa!')
elif idade > 60 and idade <= 69:
    da = input('Já realizou doação anterior (S/N)? ')
    if da == 'S' or da == 's':
        pd = int(input('Idade da primeira doação: '))
        if pd <= 60:
                print('Doador apto. Encaminhar para a próxima etapa!')
        else:
                print('Doador não atende os requisitos de idade.')
    else:
        print('Doador não atende os requisitos de idade.')
else:
    print('Doador não atende os requisitos de idade.')
