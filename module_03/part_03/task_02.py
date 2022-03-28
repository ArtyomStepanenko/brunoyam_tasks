s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

def word_5(s):
	res = []
	words = s.split()
	for word in words:
		if word.isalpha() == False:
			word_update = ''
			for i in word:
				if i.isalpha():
					word_update += i
			word = word_update
			if word != '' and len(word) < 5:
					res.append(word)
		elif len(word) < 5:
			res.append(word)
	print(res)

word_5(s)