import os
from scr.loteria import sorteio
from scr.perguntas_e_respostas import perguntas_e_respostas
from scr.data import *

os.system('cls')
input('''
_______________________________________________________________________
|                                                                      |
| Projeto em conjunto com a namorada (Eu programo | Ela cria o roteiro)|
|                Aqui teremos muitos "RTT" e amor*                     |
|______________________________________________________________________|
                            ^_^  ||    ^_^
                          ( ^.^ )||  ( ^.~ )
                           >    >||    > <
Aperte ENTER para iniciar (Não tem mais volta)\n''')

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


opcoes = ('Loteria',
          'Perguntas e Respostas')

while True:
    os.system('cls')

    print('Escolha uma opção')
    indice_menu = 1
    for opcao in opcoes:
        print(f'{indice_menu}) {opcao}')
        indice_menu += 1
    user = int(input())

    if user == 1:
        while True:
            sorteio()  
            user = input(f'Aperte ENTER para continuar ou [E]xit para sair\n').lower()
            if user == 'e':
                break
            elif user == '':
                continue

    elif user == 2:
        while True:
            perguntas_e_respostas()
            user = input(f'Aperte ENTER para continuar ou [E]xit para sair\n').lower()
            if user == 'e':
                break
            elif user == '':
                continue

    else:
        input('Opção invalida\nAperte ENTER para retornar ao menu')
        continue