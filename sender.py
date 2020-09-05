from os import listdir

from fake_useragent import UserAgent
from requests import post, exceptions


def sender(phone: str):
	useragent = UserAgent().random

	for filename in listdir('services'):
		with open(f'services/{filename}', 'r') as file:
			text = file.read().split('\n')

			url = text[0]

			data = eval(text[1])
			
			for key in data:
				if "@PHONE@" in data[key]:
					data[key] = data[key].replace("@PHONE@", phone)

			header = {'user-agent': useragent, **eval(text[2])}

			try:
				responce = post(url, data=data, headers=header)
				print(filename, "отправлено")

			except exceptions.ConnectionError:
				print(filename, "не отправлено")
