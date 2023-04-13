#   Desafio 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# - Quantas pessoas foram cadastradas
# - Média de idade do grupo
# - Lista com todas as mulheres
# - Uma lista com todos com idade acima da média

grupo = []
pessoa = {}
qtd = int(input('Quantas pessoas quer cadastrar?: '))
for c in range(0, qtd):
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: ')).upper()
    pessoa['Idade'] = int(input('Idade: '))
    print('===========================')
    grupo.append(pessoa.copy())
    pessoa.clear()

print('+{0:-^20}+{0:-^20}+{0:-^20}+'.format('-'))
for k in grupo[0].keys():
    print('|{:^20}'.format(k), end='')
print('|')
print('+{0:-^20}+{0:-^20}+{0:-^20}+'.format('-'))
for pessoa in grupo:
    print('|{:^20}|{:^20}|{:^20}|'.format(pessoa['Nome'], pessoa['Sexo'], pessoa['Idade']))
print('+{0:-^20}+{0:-^20}+{0:-^20}+'.format('-'))

import time
time.sleep(60)