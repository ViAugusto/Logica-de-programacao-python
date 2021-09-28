print("Esse programa será para armazenar a quantidade de votos em cada semana.")
print("Assim sendo, digite a quantidade de votos para cada dia.")
print("")

segunda = int(input("Digite a quantidade de votos para segunda-feira: "))
terca = int(input("Digite a quantidade de votos para terça-feira: "))
quarta = int(input("Digite a quantidade de votos para quarta-feira: "))
quinta = int(input("Digite a quantidade de votos para quinta-feira: "))
sexta = int(input("Digite a quantidade de votos para sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda teve {}".format(segunda) + " e foi a vencedora!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça teve {}".format(terca) + " e foi a vencedora!")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta teve {}".format(quarta) + " e foi a vencedora!")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta teve {}".format(quinta) + " e foi a vencedora!")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Sexta teve {}".format(sexta) + " e foi a vencedora!")
