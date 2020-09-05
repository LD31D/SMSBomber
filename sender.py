from os import listdir

from fake_useragent import UserAgent
from requests import post, exceptions


def sender(phone: str):
	useragent = UserAgent().random

	for file in listdir('servises'):
		with open(f'servises/{file}', 'r') as file:
			text = file.read().split('\n')

			url = text[0]

			data = eval(text[1])
			
			for key in data:
				if data[key] == "@PHONE@":
					data[key] = phone

			header = {'user-agent': useragent, **eval(text[2])}

			try:
				post(url, data=data, headers=header)

			except exceptions.ConnectionError:
				print("ConnectionError")
