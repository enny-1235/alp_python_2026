opcao = -1

while opcao != 0:
    print("\n=== BLACK FRIDAY ===")
    print("1 - Comprar produto")
    print("2 - Ver promoção")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor do produto: "))
        desconto = valor * 0.20
        total = valor - desconto
        print("Valor com 20% de desconto: R$", total)

    elif opcao == 2:
        print("Promoção: 20% de desconto em todos os produtos!")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida!")
