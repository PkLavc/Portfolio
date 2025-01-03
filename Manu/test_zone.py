from scr.data import *

jogador = [
    {
        'nome': 'Prediogorado',
        'pontuacao': 0
    },
]

def modo_de_jogo():
    escolha = input('''Escolha o Modo de jogo:
          [S]olo
          [M]ultijogador
          ''').lower()

    def multiplayer():
        while True:
            try:
                num_jogadores = int(input('Qual a quantidade de jogadores?\n'))
                if num_jogadores < 1:
                    print("Deve haver pelo menos um jogador.")
                    continue
                break
            except ValueError:
                print('Apenas números!')

        for indice in range(num_jogadores):
            nome_jogador = input(f'Digite o nome do jogador {indice + 1}: ')
            if nome_jogador: 
                jogador.append({'nome': nome_jogador, 'pontuacao': 0})
            else:
                jogador.append({'nome': nome_jogador_data(), 'pontuacao': 0})

    if escolha == 's':
        user = input('Qual o seu nome?')
        if user != '': 
            jogador[0]['nome'] = user
    elif escolha == 'm':
        multiplayer()
    else:
        print("Opção inválida. Tente novamente.")

modo_de_jogo()
print(jogador)