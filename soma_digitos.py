num = int(input("Escreva o número para ser somado: "))
soma = 0

while num > 0:
	resto = num % 10
	num = num // 10

	soma = soma + resto

print(soma)
