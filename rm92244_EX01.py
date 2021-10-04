print("Seja bem vindo ao HealthTrack - Calorias!")
print("Aqui você informará a quantidade de alimentos que você comeu, informando depois a quantidade de cada um.")

quantidade = int(input("Quantos alimentos você comeu hoje?: "))
calorias = 0
contador = 1

if(quantidade <= 0):
    print("Ops, você colocou um número igual ou inferior a 0.")
    print("Programa finalizado!")
elif(quantidade >= 100):
    print("Dificilmente alguém vai comer tantas coisas assim!")
    print("Programa finalizado!")
else:
    while(contador <= quantidade):
        coleta = int(input("Quantas calorias você ingeriu com esse alimento?: "))
        if(coleta <= 0):
            print("Não tem como um alimento ter valor nulo ou negativo, digite o valor correto.")
        else:
            calorias = calorias + coleta
            contador = contador + 1
        
    print("Você ingeriu {}".format(calorias) + " calorias hoje!")
