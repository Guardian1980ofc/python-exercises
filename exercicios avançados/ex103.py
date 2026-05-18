def ficha(jogador='<desconecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()

if n == '':
    n = '<desconecido>'

if g == '':
    g = 0
else:
    g = int(g)

ficha(n, g)
