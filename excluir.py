n = int(input("Digite um número grande: "))
adjacente = False 
posterior = 0
n = n // 10
anterior = n % 10

while n > 0 and not adjacente:
	atual = n % 10
	if atual == anterior:
		adjacente = True
	else:
		posterior += 1
	anterior = atual
	n = n // 10
		
if adjacente:
	print("Deu certo")
else:
	print("Deu b.o")
