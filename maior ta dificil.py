x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if y > x:
	z = y % x
	if z == 0:
		print("multiplo")
	else:
		print("Não multiplo")
else:
	z = x % y
	if z == 0:
		print("Multiplo")
	else:
		print("Não multiplo")