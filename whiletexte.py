seq = int(input("Digite a sequência de números a ser multiplicada: "))

p = 1
i = 0

while i < seq:
	valor = int(input("Digite um valor: "))
	p = p * valor
	i = i + 1

print(p)
