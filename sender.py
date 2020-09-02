from fake_useragent import UserAgent
from requests import post, exceptions


def sender(phone: str):
	with open('servises/uklon.txt', 'r') as file:
		text = file.read().split('\n')

		url = text[0]

		data = eval(text[1])
		
		for key in data:
			if data[key] == "@PHONE@":
				data[key] = phone

		header = {'user-agent': UserAgent().random, **eval(text[2])}

		try:
			post(url, data=data, headers=header)

		except exceptions.ConnectionError:
			print("ConnectionError")
