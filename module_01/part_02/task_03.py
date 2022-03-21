password = input('Введите пароль: ')
while len(password) <= 8 or password.islower() or password.isupper():
	print('Пароль недопустимый')
	password = input('Введите пароль: ')

print('Пароль является допустимым')