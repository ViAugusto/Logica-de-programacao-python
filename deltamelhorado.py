def perg():
        return float(input("Digite um valor: "))
               
a = perg()
b = perg()
c = perg()

def delta(a, b, c):
	return ( b ** 2 ) - ( 4 * a * c)

delta = delta(a, b, c)

if delta >1:
	def x1(a, b, c, delta):
		return (-b + delta ** ( 1 / 2 )) / ( 2 * a)
	print("x1 é igual a ", x1)

	def x2(a, b, c, delta):
		return (-b - delta ** ( 1 / 2 )) / ( 2 * a)
	print("x2 é igual a ", x2)

elif delta == 0:
	def x1(a, b, c, delta):
		return (-b + delta ** ( 1 / 2 )) / ( 2 * a)
	print("x1 é igual a ", x1)

else:
	print("Sem raízes reais")

x1 = x1(a, b, c, delta)
x2 = x2(a, b, c, delta)

print("x1 é igual a ", x1)
print("x2 é igual a ", x2)
