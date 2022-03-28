import json

def register(login, passwd):
	with open('data.json', 'r') as f:
		data = json.load(f)
	if login in data.keys():
		print('Логин занят')
	else:
		data[login] = passwd
		with open('data.json', 'w') as f:
			json.dump(data, f)

log = input('Введите логин: ')
passwd = input('Введите пароль: ')

register(log, passwd)