x = float(input('Введите значение x: '))
p = float(input('Введите значение p: '))
y = float(input('Введите значение y: '))
n = 0

while x < y:
	x = round(x * (100 + p) / 100)
	n += 1

print(n)