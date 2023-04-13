#   Desafio 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

infos = {}
infos['Nome'] = str(input('Nome: '))
infos['Idade'] = 2023 - int(input('Ano de nascimento: '))
infos['CTPS'] = int(input('Carteira de Trabalho (0 para "não tem"): '))
if infos['CTPS'] != 0:
    infos['Ano de Contratação'] = int(input('Ano de contratação: '))
    infos['Salário'] = int(input('Salário: R$'))
    infos['Aposentadoria'] = 60 - (2023 - infos['Ano de Contratação'])

print('=-'*30)

for k, v in infos.items():
    print(f'{k} é {v}')

import time
time.sleep(60)