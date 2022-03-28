x = int(input('Введите целое число: '))
res = 0

while x > 0:
	digit = x % 10
	res += digit
	x = x // 10

print(res)