import os
import json

import scr as modo

save = '.\\saves\\'
jogadores = []
save_jogador = save + 'jogadores_save.json'

def limpar():
    os.system('cls')

limpar()
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
limpar()

def recuperar_save():
    global jogadores
    with open(save_jogador, 'r', encoding = 'utf8') as data:
        jogadores = json.load(data)

def salvamento():
    with open(save_jogador, 'w', encoding = 'utf8') as data:
        json.dump(
            jogadores,
            data,
            indent = 2
        )

try:
    recuperar_save()
except:
    salvamento()

class player():

    def __init__(self, nome, pontuacao = 0, jogos = 0):
        self.nome = nome
        self.pontuacao = pontuacao
        self.jogos = jogos

        jogador = vars(self)
        if jogador not in jogadores:
            jogadores.append(jogador)
        salvamento()

def sem_nome_player():
    player(nome = 'Prediogorado')

def modo_de_jogo():
    escolha = input('''Escolha o Modo de jogo:
          [S]olo
          [M]ultijogador
          ''').lower()

    def multiplayer():
        while True:
            try:
                num_jogadores = int(input('Qual a quantidade de jogadores?\n'))
                if num_jogadores <= 1:
                    print("Deve haver pelo menos um jogador.")
                    continue
                break
            except ValueError:
                print('Apenas números!')

        for indice in range(num_jogadores):
            nome_jogador = input(f'Digite o nome do jogador {indice + 1}:\n')
            if nome_jogador:
                player(nome = nome_jogador)
            else:
                sem_nome_player()
        return

    if escolha == 's':
        nome_jogador = input('Qual o seu nome?\n')
        if nome_jogador != '': 
            player(nome = nome_jogador)
            return
        else:
            sem_nome_player()
            return
    elif escolha == 'm':
        multiplayer()
    else:
        print("Opção inválida. Tente novamente.")
        modo_de_jogo()

modo_de_jogo()

opcoes_modos = (
'Escolher novamente o modo de jogo',
'Pontuacao Jogadores',
'Escolher jogo'
)

opcoes_modulos = (
'Loteria',
'Perguntas e Respostas'
)

def opcoes_iniciais():
    print('Escolha uma opção')
    indice_menu = 1
    for opcao in opcoes_modos:
        print(f'{indice_menu}) {opcao}')
        indice_menu += 1
    user = int(input())
    return user

def modulos():
    indice_menu = 1
    for opcao in opcoes_modulos:
        print(f'{indice_menu}) {opcao}')
        indice_menu += 1
    user = int(input())
    return user

while True:
    limpar()

    user = opcoes_iniciais()

    if user == 1:
        limpar()
        modo_de_jogo()
        continue
    if user == 2:
        limpar()
        for jogador in jogadores:
            nome = jogador['nome']
            jogos = jogador['jogos']
            pontuacao = jogador['pontuacao']
            print(f"Player: {nome:<20} Jogou {str(jogos):<3} partidas\t\tPontuacao Total: {str(pontuacao):<5}")
        input('Enter parea continuar')
        continue
    if user == 3:
        limpar()
        user = modulos()


# ======================================== Sorteio ========================================
    if user == 1:
        while True:
            modo.sorteio()
            user = input(f'Aperte ENTER para continuar ou [E]xit para sair\n').lower()
            if user == 'e':
                break
            elif user == '':
                continue

# ================================= Perguntas e respostas =================================
    if user == 2:
        while True:
            modo.perguntas_e_respostas()
            user = input(f'Aperte ENTER para continuar ou [E]xit para sair\n').lower()
            if user == 'e':
                break
            elif user == '':
                continue

# ==================================== SFinal da Main ====================================

    else:
        input('Opção invalida\nAperte ENTER para retornar ao menu')
        continue