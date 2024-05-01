clientes = []
contas = []

def menu(): # FUNÇÃO MENU

    menu = '''

    ===========================
    |           Menu          |
    ===========================

    [1] Cadastro de Cliente
    [2] Cadastro de Conta
    [3] Listar Contas
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [0] Sair

    Digite uma opção: '''

    return int(input(menu))

def filtrar_cliente(cpf, clientes): # FUNÇÃO PARA FILTRAR CLIENTES
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def cadastro_cliente(clientes): # FUNÇÃO CADASTRO CLIENTE
    print('===========================')
    print('|   Cadastro de Cliente   |')
    print('===========================')
    cpf = input('Digite o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Esse usuário já foi cadastrado anteriormente")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente adicionado com sucesso!")

def cadastro_conta(agencia, numero_conta, clientes): # FUNÇÃO CADASTRO CONTA
    print('===========================')
    print('|    Cadastro de Conta    |')
    print('===========================')
    cpf = input('Digite o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("CPF não cadastrado. Favor cadastrar o cliente primeiro.")

def listar_contas(contas): # FUNÇÃO LISTAR CONTAS
    for conta in contas:
        registro = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """

        print(registro)


def depositar(saldo, valor, extrato, /): # FUNÇÃO DEPOSITAR
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito de R$ {valor:.2f}"
        print(f'Depósito de R$ {valor:.2f} efetuado com sucesso.\nSaldo atual R$ {saldo:.2f}')
    else:
        print('Valor inválido. Não foi possível efetuar o depósito')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # FUNÇÃO SACAR
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente.")
    
    elif excedeu_limite:
        print("Valor do saque excedeu o limite")

    elif excedeu_saques:
        print("Número máximo de saques excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque de R$ {valor:.2f}"
        print(f'Saque de R$ {valor:.2f} efetuado com sucesso.\nSaldo atual R$ {saldo:.2f}')
        numero_saques += 1
    
    else:
        print("Valor inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): # FUNÇÃO EXTRATO
    print("extrato")

    print('===========================')
    print('|         Extrato         |')
    print('===========================')
    if extrato == "":
        print("Não houve movimentações.")
        print()
        print(f'Saldo atual: R$ {saldo:.2f}')
    else:
        print(extrato)
        print()
        print(f'Saldo atual: R$ {saldo:.2f}')

def main(): # FUNÇÃO PRINCIPAL (MAIN)

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            cadastro_cliente(clientes)
        
        elif opcao == 2:
            numero_conta = len(contas) + 1
            conta = cadastro_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
        
        elif opcao == 3:
             listar_contas(contas)
        
        elif opcao == 4:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 5:
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == 6:
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 0:
            print('Obrigado por utilizar o nosso sistema')
            break
        
        else:
            print('Opção inválida. Selecione uma opção válida.')

main() # CHAMANDO FUNÇÃO MAIN