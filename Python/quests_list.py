import os
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
    input(f'Acertos {acertos}\t Erros: {erros}\nAperte Enter para continuar')
    indice += 1

    if indice == len(perguntas):
        indice = 0