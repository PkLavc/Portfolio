jogador = [
        {
            'nome': 'Prediogorado',
            'pontuacao': 0
        },
        ]

def modo_de_jogo():
    user = input('''Escolha o Modo de jogo:
          [S]olo
          [M]ultijogador
          ''').lower()

    def multiplayer():
            indice = 0
            while True:
                try:
                    user = int(input('Qual a quantidade de jogadores?\n'))
                    break
                except ValueError:
                    print('Apenas numeros!')

            jogador[0]['nome'] = input('Digite o nome do jogador:')

            while indice < user:
                indice += 1
                jogador.add['nome'] = input('Digite o nome do jogador:')
                jogador[indice]['pontuacao'] = 0


    if user == 's':
        user = input('Qual o seu nome?')
        if user != '':
            jogador[0]['nome'] = user
    elif user == 'm':
        multiplayer()

modo_de_jogo()
print(jogador)