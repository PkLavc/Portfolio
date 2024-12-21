import random


while exit:
    opcao = 0 # Opcao 1 para Validar | Opcao 2 para Gerar 
    cpf_gerado = ''

    user = input('\tOque deseja?\n[V]alidar CPF\n[G]erar CPF\n[S]air\n').lower()
    if user[0] == 'v':
        user = input('Digite o CPF:\n')
        opcao = 1
    elif user[0] == 'g':
        opcao = 2
    elif user[0] == 's':
        break
    else:
        print('Opcao invalida')
        continue
    
    if opcao == 1:

        for formatar in user:
            if formatar in '0123456789':
                cpf_gerado += formatar
        if len(cpf_gerado) != 11:
            print('CPF Invalido')
            continue
    if opcao == 2:
        for _ in range(9):
            cpf_gerado += str(random.randint(0, 9))