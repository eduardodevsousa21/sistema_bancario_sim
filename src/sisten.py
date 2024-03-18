menu = '''

[d] Depositar
[s] sacar
[e] extrato
[q] sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)
    
    if opcao == 'd':
        valor = float(input('informe o valor do deposito: '))
        
        if valor > 0:
            saldo += valor 
            extrato += f'Deposito: R$ {valor:.2f}\n'
            
        else:
            print('operação falhou, o valor informado é invalido')
            
    elif opcao == 's':
        valor =  float(input ('Informe o valor do saque'))
        
        excedeu_saque = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >=  LIMITE_SAQUES
        
        if excedeu_saque:
            print('operação falhou voce não tem saldo suficiente')
        elif excedeu_limite:
            print('operação falhou valor de saques excedido')
            
        elif excedeu_saques:
            print('operação falhou numero de saques excedido')
            
        elif valor > 0:
            saldo  -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saques += 1
            
        else: 
            print('operação falhou! o valor informado é invalido')
            
    elif opcao == 'e':
        print('\n ================= EXTRATO ================')
        print('Não forma realizadas momvimentações.' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('=============================================')
    
    elif opcao == 'q':
        break
    
    else:
        print('Operação inválida! Tente novamente')