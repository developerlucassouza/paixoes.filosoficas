#   Desafio 093
# Crie um programa que gerencie o aprovamento de um jogador de futebola. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada jogo. No final, tudo será guardado em um dicionário 

dados = {}

dados['Jogador'] = str(input('Nome do Jogador: '))
dados['Partidas'] = int(input(f'Partidas de {dados["Jogador"]}: '))
partidas = []
for c in range(0, dados['Partidas']):
    partidas.append(int(input(f'Gols no jogo {c+1}: ')))
dados['Gols por partida'] = partidas[:]

print('=-'*30)
for k, v in dados.items():
    print(f'{k} - {v}')

import time
time.sleep(60)