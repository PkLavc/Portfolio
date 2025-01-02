import os

def perguntas_e_respostas():
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

        print(f'Pergunta {indice + 1}\n{perguntas[indice]["Pergunta"]}')
        i = 1
        for opcao in perguntas[indice]['Opções']:
            print(f'{i}) {opcao}')
            i += 1
        user = input('Qual a opção está correta?\n')

        try:
            user = int(user) - 1
            if perguntas[indice]['Resposta'] == perguntas[indice]['Opções'][user]:
                print('Acertou!')
                acertos += 1
            else:
                print('Você errou!')
                erros += 1
        except:
            print('Opção inválida, digite apenas o número da opção')

        print(f'Acertos {acertos}\t Erros: {erros}')
        indice += 1

        if indice == len(perguntas):
            print(f'Você chegou ao fim das perguntas')
            indice = 0
            break
