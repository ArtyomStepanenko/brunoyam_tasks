n1 = int(input('Введите первое целое число: '))
n2 = int(input('Введите второе целое число: '))
n3 = int(input('Введите третье целое число: '))

if (n1 == n2) and (n2 == n3):
	print(3)
elif (n1 == n2) or (n2 == n3) or (n1 == n3):
	print(2)
else:
	print(0)