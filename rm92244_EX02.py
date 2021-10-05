print("Programação não é para os mais velhos! Jovens também podem usar.")
print("Aqui você informará suas transações que fez hoje, depois será feito uma média e exibirá os valores.")

quantidade = int(input("Quantas transações você fez hoje?: "))
transacoes = 0
contador = 1

if(quantidade <= 0):
    print("Ops, você colocou um número igual ou inferior a 0.")
    print("Programa finalizado!")
elif(quantidade >= 85):
    print("Duvido que você tenha feito tantas transações assim!")
    print("Programa finalizado!")
else:
    while(contador <= quantidade):
        armazenarTransacoes = float(input("Quantos reais você gastou nessa transação?: "))
        if(armazenarTransacoes <= 0):
            print("Você está fazendo transações, não um depósito na sua conta! Digite o valor correto.")
        else:
            transacoes = transacoes + armazenarTransacoes
            contador = contador + 1
    media = transacoes / quantidade
    print("Você gastou R${}".format(transacoes) + " hoje!")
    print("E também, em média, gastou R${}".format(media) + " por cada transação.")
