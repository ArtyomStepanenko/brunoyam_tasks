import json

def login_function(login, passwd):
	with open('data.json', 'r') as f:
		data = json.load(f)
	if login not in data.keys() or passwd != data[login]:
		print('Некорректный логин или пароль')
	else:
		print('Успешный вход')

log = input('Введите логин: ')
passwd = input('Введите пароль: ')

login_function(log, passwd)