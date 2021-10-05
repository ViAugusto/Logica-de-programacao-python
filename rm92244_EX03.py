print("Vamos ver se você é bom de chutes. Digite um número aleatório, temos um padrão feito por hackers e não acho que você acertará.")

palpite = int(input("Qual seu palpite?: "))
ultimo=1
penultimo=1
fibonacci = 100
termo = 0




if (palpite==1):
    print("Acertou!!")
else:
    contador = 3
    while (contador < fibonacci):
        if(palpite == termo):
            print("Acertou!!")
            break
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        contador = contador + 1
    if(palpite != termo):
        print("Errou!")
