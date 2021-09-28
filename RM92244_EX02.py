print("Seja bem vindo a Produção Multimídia da FIAP ON!!")
print("---------------------------")
print("Temos 4 tipos de assinturas para você, querido cliente, e elas são:")
print("---------------------------")
print("Nível Basic, com 30% de faturamento. Para selecionar ela digite 'B' ")
print("Nível Silver, com 20% de faturamento. Para selecionar ela digite 'S' ")
print("Nível Gold, com 10% de faturamento. Para selecionar ela digite 'G' ")
print("Nível Platinum, com 5% de faturamento. Para selecionar ela digite 'P' ")
print("---------------------------")


assinatura = input("Digite o tipo de assinatura: ")
faturamento = float(input("Digite quanto você faturou em um ano: "))

if (assinatura == 'B'):
    bonus = faturamento * 0.3
    print("Você terá de pagar R${}!".format(bonus) + " de bônus como cliente Basic.")
elif (assinatura == 'S'):
    bonus = faturamento * 0.2
    print("Você terá de pagar R${}!".format(bonus) + " de bônus como cliente Silver.")
elif (assinatura == 'G'):
    bonus = faturamento * 0.1
    print("Você terá de pagar R${}!".format(bonus) + " de bônus como cliente Gold.")
elif (assinatura == 'P'):
    bonus = faturamento * 0.05
    print("Você terá de pagar R${}!".format(bonus) + " de bônus como cliente Platinum.")
else:
    print("Ops, opção inválida.")
