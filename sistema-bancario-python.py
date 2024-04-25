menu = '''

###### MENU ######

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Digite uma opção: '''

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print('Depósito')
        deposito = (float(input('Digite o valor a ser depositado: ')))
        if deposito > 0:
            saldo += deposito
            extrato += f"\nDepósito de R$ {deposito:.2f}"
            print(f'Depósito de R$ {deposito:.2f} efetuado com sucesso.\nSaldo atual R$ {saldo:.2f}')
        else:
            print('Valor negativo. Não foi possível efetuar o depósito')

    elif opcao == 2:
        print('Saque')
        saque = float(input('Digite o valor a ser sacado: '))
        if numero_saques < 3:
            if saque > limite:
                print(f'Limite máximo por saque R$ {limite:.2f}. Favor selecionar outro valor.')
            else:
                saldo -= saque
                extrato += f"\nSaque de    R$ {saque:.2f}"
                print(f'Saque de R$ {saque:.2f} efetuado com sucesso.\nSaldo atual R$ {saldo:.2f}')
                numero_saques += 1
        else:
            print(f'Limite diário de {numero_saques} saques atingido. Tente novamente amanhã')

    elif opcao == 3:
        print('Extrato')
        print(extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == 0:
        print('Obrigado por utilizar o nosso sistema')
        break
    
    else:
        print('Opção inválida. Selecione uma opção válida.')