import os 
import random

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
            'nome': 'Usuario',
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
            os.system('cls')
            numeros_sorteados = ['', '','', '','', '']
            aposta = ['', '','', '','', '']
            acertos = 0

            # def sortear():
            #     for indice in range(6):
            #         numeros_sorteados[indice] = str(random.randint(1, 60))
            #     return numeros_sorteados

            # while True:
            #     sortear()
            #     rtt_repeticao = [0, 0, 0, 0, 0, 0]
            #     teste_1 = 0
            #     while teste_1 != 6:
            #         teste_2 = 5
            #         while teste_2 != -1:
            #             if numeros_sorteados[teste_1] == numeros_sorteados[teste_2]:
            #                 rtt_repeticao[teste_1] += 1
            #             teste_2 -= 1

            #         teste_1 += 1
            #     if rtt_repeticao != [2, 2, 2, 2, 2, 2]: 
            #         break

            def sortear_numeros():
                return random.sample(range(1, 61), 6)
            
            numeros_sorteados = sortear_numeros()
            
            Manu = input('Insira 6 numeros, separados por "," de 1 a 60\n')

            try:
                i = 0
                for converter in Manu:
                    if converter != ',':
                        aposta[i] += converter
                    else:
                        i += 1
            except:
                print('Quantidade de numeros excedida\nExcedentes ignorados')

            # for _ in range(6):
            #     if aposta[_] in numeros_sorteados:
            #         acertos += 1
            
            # if acertos == 6:
            #     print('Voce ganhou na Mega Sena da virada')
            # elif acertos == 5:
            #     print('Voce ganhou um Pudim de Pao')
            # elif acertos == 4:
            #     print('Voce ganhou uma balinha')
            # elif acertos == 3:
            #     print('Voce ganhou 50 centavos')
            # elif acertos == 2:
            #     print('Voce ganhou uma pedrinha')
            # elif acertos == 1:
            #     print('Voce ganhou uma bolinha de peleleca')
            # else:
            #     print('O mundo nao gosta de voce. Voce levou um espirro na cara')

            acertos = set(numeros_sorteados) & set(aposta)

            if len(acertos) == 6:
                print('Voce ganhou na Mega Sena da virada')
            elif len(acertos) == 5:
                print('Voce ganhou um Pudim de Pao')
            elif len(acertos) == 4:
                print('Voce ganhou uma balinha')
            elif len(acertos) == 3:
                print('Voce ganhou 50 centavos')
            elif len(acertos) == 2:
                print('Voce ganhou uma pedrinha')
            elif len(acertos) == 1:
                print('Voce ganhou uma bolinha de peleleca')
            else:
                print('O mundo nao gosta de voce. Voce levou um espirro na cara')


            user = input(f'Resultado da Mega Sena {numeros_sorteados}\nAperte ENTER para continuar ou [E]xit para sair\n').lower()
            
            if user == 'e':
                break
        continue

    elif user == 2:
        perguntas = [
        {
            'Pergunta': 'Quanto é 2+2?',
            'Opções': ['1', '3', '4', '5'],
            'Resposta': '4',
        },
        {
            'Pergunta': 'Quanto é 5*5?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': '25',
        },
        {
            'Pergunta': 'Quanto é 10/2?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': '5',
        },
        ]
        indice = 0
        acertos = 0
        erros = 0

        while True:
            os.system('cls')

            print(f'Pergunta {indice + 1}\n{perguntas[indice]['Pergunta']}')
            i = 1
            for opcao in perguntas[indice]['Opções']:
                print(f'{i}) {opcao}')
                i += 1
            user = input('Qual a opcao esta correta?\n')

            try:
                user = int(user) - 1
                if perguntas[indice]['Resposta'] == perguntas[indice]['Opções'][user]:
                    print('Acertou!')
                    acertos += 1
                else:
                    print('Voce errou!')
                    erros += 1

            except:
                print('Opcao invalida, digite apenas o resultado')

            print(f'Acertos {acertos}\t Erros: {erros}')
            indice += 1

            if indice == len(perguntas):
                print(f'Voce chegou ao fim de {opcoes[1]}')
                indice = 0

            user = input('Aperte ENTER para continuar ou [E]xit para sair\n').lower()
        
            if user == 'e':
                break
        continue

    elif user == 3:
        ...
    else:
        input('Opção invalida\nAperte ENTER para retornar ao menu')
        continue