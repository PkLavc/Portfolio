import os 
import random

'''
Projeto com a namorada
Considerar como ALPHA 0.000000001 :D
'''

while True:
    os.system('cls')
    numeros_sorteados = ['', '','', '','', '']
    aposta = ['', '','', '','', '']
    acertos = 0

    def sortear():
        for indice in range(6):
            numeros_sorteados[indice] = str(random.randint(1, 60))
        return numeros_sorteados

    while True:
        sortear()
        rtt_repeticao = [0, 0, 0, 0, 0, 0]
        teste_1 = 0
        while teste_1 != 6:
            teste_2 = 5
            while teste_2 != -1:
                if numeros_sorteados[teste_1] == numeros_sorteados[teste_2]:
                    rtt_repeticao[teste_1] += 1
                teste_2 -= 1

            teste_1 += 1
        if rtt_repeticao != [2, 2, 2, 2, 2, 2]: 
            break

    # input(numeros_sorteados)
    
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

    for _ in range(6):
        if aposta[_] in numeros_sorteados:
            acertos += 1
    
    if acertos == 6:
        print('Voce ganhou na Mega Sena da virada')
    elif acertos == 5:
        print('Voce ganhou um Pudim de Pao')
    elif acertos == 4:
        print('Voce ganhou uma balinha')
    elif acertos == 3:
        print('Voce ganhou 50 centavos')
    elif acertos == 2:
        print('Voce ganhou uma pedrinha')
    elif acertos == 1:
        print('Voce ganhou uma bolinha de peleleca')
    else:
        print('O mundo nao gosta de voce. Voce levou um espirro na cara')
    input(f'Resultado da Mega Sena {numeros_sorteados}\nAperte enter para continuar')

