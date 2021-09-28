peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("Seu imc é {}!".format(imc))

if(imc < 16):
    print(" e você está na categoria Baixo peso Grau III")
elif((imc >=16) and (imc <= 16.99)):
    print(" e você está na categoria Baixo peso Grau II")
elif((imc >=17) and (imc <= 18.49)):
    print(" e você está na categoria Baixo peso Grau I")
elif((imc >=18.50) and (imc <= 24.99)):
    print(" e você está na categoria Peso ideal")
elif((imc >=25) and (imc <= 29.99)):
    print(" e você está na categoria Sobrepeso")
elif((imc >=30) and (imc <= 34.99)):
    print(" e você está na categoria Obesidade Grau II")
elif((imc >=35) and (imc <= 39.99)):
    print(" e você está na categoria Obesidade Grau II")
elif(imc >=40):
    print(" e você está na categoria Obesidade Grau II")
