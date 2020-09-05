from os import listdir

from fake_useragent import UserAgent
from requests import post, exceptions


def sender(phone: str):
	useragent = UserAgent().random

	for filename in listdir('servises'):
		with open(f'servises/{filename}', 'r') as file:
			text = file.read().split('\n')

			url = text[0]

			data = eval(text[1])
			
			for key in data:
				if data[key] == "@PHONE@":
					data[key] = phone

			header = {'user-agent': useragent, **eval(text[2])}

			try:
				a = post(url, data=data, headers=header)
				print(filename, a.text)

			except exceptions.ConnectionError:
				print(filename, "ConnectionError")
