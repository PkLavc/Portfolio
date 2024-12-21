import os
import random

while True:
    os.system('cls')

    opcao = ''
    cpf_user = ''
    cpf_gerado = ''
    cpf_multiplicado = 0
    cpf_gerado_formatado = ''
    cpf_resto_divisao = ''
    multiplicacao = 10
    validador = ''

    user = input('\tOque deseja?\n[V]alidar CPF\n[G]erar CPF\n[S]air\n').lower()
    if user[0] == 'v':
        user = input('Digite o CPF:\n')
        opcao = 'validar'
    elif user[0] == 'g':
        opcao = 'gerar'
    elif user[0] == 's':
        break
    else:
        input('Opcao invalida, aperte qualquer tecla para continuar\n')
        continue
    
    if opcao == 'validar':
        for _ in user:
            if _ in '0123456789':
                cpf_user += _
        teste_repeticao = cpf_user[0] * 11
        if teste_repeticao == cpf_user:
            input('CPF Invalido, aperte qualquer tecla para continuar\n')
            continue
        if len(cpf_user) == 11:
            cpf_gerado = cpf_user[:9]
        else:
            input('CPF Invalido, aperte qualquer tecla para continuar\n')
            continue
        

    if opcao == 'gerar':
        for _ in range(9):
            cpf_gerado += str(random.randint(0, 9))

    for _ in cpf_gerado:
        cpf_multiplicado += int(_) * multiplicacao
        multiplicacao -= 1

    cpf_multiplicado *= 10

    cpf_resto_divisao = cpf_multiplicado % 11

    validador = cpf_resto_divisao if cpf_resto_divisao < 10 else 0

    if opcao == 'validar':
        if str(validador) != cpf_user[9]:
            input('CPF Invalido, aperte qualquer tecla para continuar\n')
            continue
    
    cpf_gerado += str(validador)

# Verificar/Gerar Segundo digito
    multiplicacao = 11
    cpf_multiplicado = 0
    cpf_resto_divisao = 0

    for _ in cpf_gerado:
        cpf_multiplicado += int(_) * multiplicacao
        multiplicacao -= 1

    cpf_multiplicado *= 10

    cpf_resto_divisao = cpf_multiplicado % 11

    validador = cpf_resto_divisao if cpf_resto_divisao < 10 else 0

    if opcao == 'validar':
        if str(validador) != cpf_user[10]:
            input('CPF Invalido, aperte qualquer tecla para continuar\n')
        else:
            input('CPF Valido, aperte qualquer tecla para continuar\n')
        continue
    
    cpf_gerado += str(validador)

    # RTT - Recurso Tecnico temporario :)
    parte_1 = cpf_gerado[0:3]
    parte_2 = cpf_gerado[3:6]
    parte_3 = cpf_gerado[6:9]
    parte_4 = cpf_gerado[9:11]
    cpf_gerado = parte_1 + "." + parte_2 + "." + parte_3 + "-" + parte_4

    input(f'CPF gerado: {cpf_gerado}\nAperte qualquer tecla para continuar\n')