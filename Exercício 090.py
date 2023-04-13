#   Desafio 090
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

info = {}
info['nome'] = str(input('Nome do aluno: '))
info['media'] = float(input('Média do aluno: '))

if info['media'] >= 7:
    info['situacao'] = 'Aprovado'
elif info['media'] >= 5:
    info['situacao'] = 'Recuperação'
else:
    info['situacao'] = 'Reprovado'

for k, v in info.items():
    print(f'{k} é {v}')

import time
time.sleep(60)