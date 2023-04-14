#   Desafio 095
# Aprimore o Desafio 093 para ele funcionar com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador

dados = {}
time = []

qtd = int(input('Quantos jogadores quer cadastrar?: '))

for c in range(0, qtd):

    print('=-'*30)
    print(f'--- Jogador {c+1} ---')

    dados['Cód'] = c + 1
    dados['Jogador'] = str(input('Nome do Jogador: '))
    dados['Partidas'] = int(input(f'Partidas de {dados["Jogador"]}: '))

    partidas = []
    totalGols = 0
    for c in range(0, dados['Partidas']):
        partidas.append(int(input(f'Gols no jogo {c+1}: ')))
        totalGols += partidas[c]

    dados['Gols'] = partidas[:]
    dados['Total de Gols'] = totalGols
    time.append(dados.copy())

print('=-'*30)

print('+{0:-<5}+{0:-<20}+{0:-<20}+{0:-<20}+{0:-<20}+'.format('-'))
for c, k in enumerate(time[0].keys()):
    if c == 0:
        print('|{:^5}'.format(str(k)), end='')
    else: 
        print('|{:^20}'.format(str(k)), end='')

print('|')

print('+{0:-<5}+{0:-<20}+{0:-<20}+{0:-<20}+{0:-<20}+'.format('-'))

for jogador in time:
    for c, v in enumerate(jogador.values()):
        if c == 0:
            print('|{:>5}'.format(str(v)), end='')
        else: 
            print('|{:^20}'.format(str(v)), end='')
    print('|')

print('+{0:-<5}+{0:-<20}+{0:-<20}+{0:-<20}+{0:-<20}+'.format('-'))

while True:
    print('=-'*30)
    cod = int(input('Mostrar dados de qual jogados? (999 para parar): '))
    if cod == 999:
        break 
    else:
        print(f'Jogos de: {time[cod-1]["Jogador"]}')
        for c, gols in enumerate(time[cod-1]['Gols']):
            print(f'Jogo {c+1} - {gols} gols')