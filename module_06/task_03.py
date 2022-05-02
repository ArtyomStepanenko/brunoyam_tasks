import requests
import time
from threading import Thread

def get_html(link):
	response = requests.get(link)
	print(f'{link}:', len(response.text))

links = ['https://www.google.ru/', 'https://www.youtube.com/', 'https://yandex.ru/',
'https://ru.wikipedia.org', 'https://mail.ru/']

t1 = time.time()

for i in range(5):
	get_html(links[i])

print('Time For Sequential Execution: ', time.time() - t1)

threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]

t1 = time.time()

for t in threads:
	t.start()

for t in threads:
	t.join()

print('Time For Parallel Execution: ', time.time() - t1)