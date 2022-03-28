def area(a,b,c):
	p = (a + b + c) / 2
	S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
	return(S)

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
print(area(a,b,c))