menu = """

[d] Depoistar
[s] sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

while True:

    opcao = input(menu)

    # Depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósto: ${valor:.2f}/n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    # Saque
    elif opcao =="s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        if excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        if excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: ${valor:.2f}/n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido")

    # Extrato
    elif opcao == "e":
        print("\n============== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("============================================")

    # Sair
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

