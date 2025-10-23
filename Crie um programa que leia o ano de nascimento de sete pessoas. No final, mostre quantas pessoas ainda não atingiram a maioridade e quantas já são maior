from datetime import date
ano_atual = date.today().year

qtd = int(input('Quantas pessoas? '))
maiores = menores = iguais = 0

for i in range(1, qtd + 1):
    nascimento = int(input(f'Ano de nascimento {i}: '))
    idade = ano_atual - nascimento
    print(idade)
    if idade > 18:
        maiores += 1
    elif idade < 18:
        menores += 1
    else:
        iguais += 1

print('____________________________________________')
print(f'MAIORES DE 18 ANOS: {maiores}')
print(f'MENORES DE 18 ANOS: {menores}')
print(f'IGUAIS A 18 ANOS: {iguais}')
print('____________________________________________')
