import requests
import sqlite3
import gzip
import json
import re
import os
import collections
import datetime


def get_appkey():

	with open('app.id', 'r') as f:
		return f.readlines()[1].strip()


def get_cities():

	if os.path.exists('city.list.json.gz'):
		print('city.list.json.gz is already uploaded')
	else:
		req = requests.get('http://bulk.openweathermap.org/sample/city.list.json.gz')
		with open('city.list.json.gz', 'wb') as f:
			f.write(req.content)
	with gzip.open('city.list.json.gz', 'rb') as f:
		data_binary = f.read()
	data = json.loads(data_binary.decode('utf-8'))
	return data


City_weather = collections.namedtuple("City_weather", "id_city, "
										"city_name, date_today, temperature, id_weather, country_code")


def get_cities_weather(cities, country='RU', cities_data=get_cities()):

	cities_ids = ''
	cities_names = []
	for city in cities:
		for line in cities_data:
			if line['name'] == city and line['country'] == country:
				cities_ids += str(line['id']) + ','
				cities_names.append(city)

	cities_ids = cities_ids[:-1]

	pattern = \
		"""http://api.openweathermap.org/data/2.5/group?id={cities_ids}&units=metric&appid={appkey}"""

	content = requests.get(pattern.format(cities_ids=cities_ids, appkey=get_appkey())).content

	try:
		content = json.loads(content.decode('utf-8'))['list']
	except KeyError as e:
		print(json.loads(content.decode('utf-8')).items())
		raise e

	def convertT(x):
		return x - 273.15 if x > 200 else x

	# fill data structure
	cities_ids = list(map(int, cities_ids.split(',')))
	list_ = []
	for i, rec in enumerate(content):
		list_.append(
			City_weather(cities_ids[i], cities_names[i], datetime.date.today(), convertT (rec['main']['temp']),
						rec['weather'][0]['id'], rec['sys']['country'])
		)
	return list_


class Weather:
	def __init__(self):
		self.db = 'weather.db'
		self.cities_data = get_cities()
		self._cities = set(i['name'] for i in self.cities_data)
		self._country_codes = set(i['country'] for i in self.cities_data)

		if not os.path.exists('weather.db'):
			with sqlite3.connect(self.db) as conn:
				cursor = conn.cursor()
				cursor.execute("""CREATE TABLE weather(
                        id_city     INTEGER PRIMARY KEY,
                        city_name   VARCHAR(255),
                        date_today  date,
                        temperature INTEGER,
                        id_weather  INTEGER, 
                        country_code text);""")

	def show_countries_cities(self, text):
		count = 30
		i = 0
		print('Countries:')
		for c_code in self._country_codes:
			if re.match(text, c_code):
				print(c_code)
				i += 1
				if i > count:
					break

		i = 0
		print('Cities: ')
		for city in self._cities:
			if re.match(text, city):
				print(city)
				i += 1
				if i > count:
					break

	def get_cities_weather(self):
		country = input("Input country code (like: RU) -> ")
		cities_list = input("Input cities list (like: Novinki Moscow etc.) -> ")
		cities_list = cities_list.split ()

		if country not in self._country_codes:
			print('No such country code')

		print("-> updating database ...")
		for city in cities_list:
			data = self.get_data(city, country)
			if data:
				for city in data:
					if city.date_today == \
							datetime.datetime.today().strftime('%Y-%m-%d'):
						print('Found in database: ')
						print(city)
					else:
						# upload data, show and update
						print('-> updating existing records ...')
						cities_weather = get_cities_weather([city, ], country, self.cities_data)
						print("Weather info:")
						for cw in cities_weather:
							print(cw)
							with sqlite3.connect(self.db) as conn:
								cursor = conn.cursor()
								cursor.execute("""
									UPDATE weather 
									SET temperature=?,
                                        date_today=?
                                    WHERE id_city=?""", (cw.temperature,
										  datetime.datetime.today(),
										  cw.id_city)
												)
						break

			else:
				print('-> adding new data ...')
				with sqlite3.connect(self.db) as conn:
					cursor = conn.cursor()
					cities_weather = get_cities_weather([city, ], country, self.cities_data)
					print("Weather info:")
					for cw in cities_weather:
						if cw.country_code != country:
							continue
						print(cw)
						cursor.execute ("""
                            INSERT INTO weather
                            VALUES ('{id_city}',
                                    '{city_name}',
                                    '{date_today}',
                                    '{temperature}',
                                    '{id_weather}',
                                    '{country_code}'
                                    );
                        """.format(**cw._asdict()))

		print("-> update complete.")

	def get_data(self, cityname, country_code='RU'):

		with sqlite3.connect(self.db) as conn:
			cur = conn.cursor()
			sql = "SELECT * FROM weather WHERE city_name=? AND country_code=?"
			cur.execute(sql, (cityname, country_code))
			results = cur.fetchall()

		output = []
		for line in results:
			output.append(City_weather (*line))
		return output
