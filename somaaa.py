num = int(input("Escreva o número para ser somado: "))
soma = 0

while num >= 10:
	resto = num % 10
	num // 10

	soma = soma + resto

print(soma)
