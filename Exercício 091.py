#   Desafio 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esse resultados em um dicionário. No final, mostre esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from operator import itemgetter
import time

jogos = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6),}

for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
    time.sleep(1)

ranking = sorted(jogos.items(), key = itemgetter(1), reverse=True)

print('=-'*30)
for c in range(0, len(ranking)):
    print(f'{c+1}° Colocado: {ranking[c][0]} que tirou {ranking[c][1]}')
    

time.sleep(60)