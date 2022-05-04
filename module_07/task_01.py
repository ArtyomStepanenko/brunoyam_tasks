import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
from datetime import datetime

page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
exchange_rate_table = soup.find('table', {'class': 'mfd-table mfd-currency-table'})
rows = exchange_rate_table.find_all('tr')
dates = []
prices = []

for row in rows:
	columns = row.find_all('td')
	if len(columns) > 0:
		dates.append(datetime.strptime(columns[0].text[2:], '%d.%m.%Y'))
		prices.append(float(columns[1].text))

pyplot.plot(dates, prices)
pyplot.show()