import os
from scr.loteria import sorteio
from scr.perguntas_e_respostas import perguntas_e_respostas

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
    user = input('''Escolha o Modo de jogo:
          [S]olo
          [M]ultijogador
          ''').lower()
    if user == 's':
        jogador[0]['nome'] = input('Qual o seu nome?')
    elif user == 'm':
        indice = 0
        multiplayer = True

        while multiplayer:
            jogador[indice]['nome'] = input('Digite o nome do jogador:')
            if indice == 0:
                indice += 1
                jogador[indice]['nome'] = input('Digite o nome do jogador:')
            user = input('') # Em construçao
            multiplayer = False
        
    return jogador


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
        perguntas_e_respostas()
    else:
        input('Opção invalida\nAperte ENTER para retornar ao menu')
        continue