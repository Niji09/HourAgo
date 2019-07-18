import requests
import json
import os
import sqlite3
import schedule
import time
import datetime
from decouple import config

def deleteOldNews():
	"""
	This method delete old news content which are one month old.
	"""
	BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	db_name = os.path.join(BASE_DIR, 'db.sqlite3') 
	
	table_name = 'newsapp_top_headline'
	col_name = 'upload_date'

	del_range = 30 # in days
	del_date = (datetime.datetime.today()-datetime.timedelta(del_range)).strftime('%d-%m-%y')
	del_query = """DELETE FROM {table_name} WHERE {col_name}='{del_date}';
	""".format(table_name=table_name, col_name=col_name, del_date=del_date)

	print(del_query)

	try:
		# connect to databse
		conn = sqlite3.connect(db_name)
		cur = conn.cursor()
	except Exception as e:
		print('Connectin Exception: ', e)

	try:
		cur.execute(del_query);
	except Exception as e:
		print('Insert Exception: ', e)
	else:
		print('Delete row count :', cur.rowcount)
		print('----------------------------------')
		conn.commit()
		conn.close()

##################################################################################################

def news_score(news_dict):
	"""
	This method give scores to news based on the these category:
	1. News Source 2. Auther 3. Title(clickbait or not) 4. description(and its length)
	5. News Url 6. Image url 7. Published date 8. News Content(value of content)
	"""
	initial_score = 0

	if news_dict['source_name'] != "null" and len(news_dict['source_name']) >=1 :
		initial_score += 1 # check for credibility for later
	if news_dict['auther'] != "null" and len(news_dict['auther']) >= 1 and news_dict['auther'].isdigit() == False:
		if news_dict['auther'].upper().lower() not in news_dict['source_name'].upper().lower():
			if news_dict['auther'].isalnum() != False:
				initial_score += 1 # check for credibility for later
	if news_dict['title'] != "null":
		initial_score += 1 # check for clickbait later
	if news_dict['description'] != "null":
		if len(news_dict['description'])>= 200:
			initial_score += 1
		elif len(news_dict['description'])>=140:
			initial_score += 0.8
		elif len(news_dict['description'])>=100:
			initial_score += 0.6
		elif len(news_dict['description'])>=75:
			initial_score+= 0.5
		elif len(news_dict['description'])>=60:
			initial_score+= 0.4
		elif len(news_dict['description'])>=50:
			initial_score+= 0.3
		elif len(news_dict['description'])>=35:
			initial_score+= 0.2
	if news_dict['url'] != "null":
		initial_score += 1
	if news_dict['urlToImage'] != "null":
			initial_score += 1
	if news_dict['publishedAt'] != "null":
		initial_score +=1
	if news_dict['content'] != "null" and len(news_dict['content']) >= 1:
		initial_score +=1

	return initial_score

def json_to_db(data, category):
	"""
	This method store the news content in database.
	"""
	BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	db_name = os.path.join(BASE_DIR, 'db.sqlite3') 
	
	table_name = 'newsapp_top_headline'
	# insert query
	table_cols = """source_name, auther, title, description, url, urlToImage,
		publishedAt, content, category, initial_score, upload_date"""
	insert_query = """INSERT OR IGNORE INTO {table_name}({table_cols}) 
		VALUES(?,?,?,?,?,?,?,?,?,?,?);""".format(table_name=table_name, table_cols=table_cols)

	# count of data in json
	data_list = list()
	data_count = json.dumps(data).count('"source": {')

	# data to insert
	for i in range(data_count):
		source_name = data['articles'][i]['source']['name']
		auther = data['articles'][i]['author']
		title = data['articles'][i]['title']
		description = data['articles'][i]['description']
		url = data['articles'][i]['url']
		urlToImage = data['articles'][i]['urlToImage']
		publishedAt = data['articles'][i]['publishedAt']
		content = data['articles'][i]['content']

		news_dict = {
			'source_name':source_name,
			'auther':auther,
			'title': title,
			'description': description,
			'url': url,
			'urlToImage':urlToImage,
			'publishedAt':publishedAt,
			'content':content,
		}

		# calling method
		initial_score= news_score(news_dict)
		#print(i, initial_score)

		# upload_date
		upload_date = datetime.datetime.today().strftime('%d-%m-%y')

		# data_list
		tup = (
			source_name, auther, title, description, url, urlToImage,
			publishedAt, content, category, initial_score, upload_date
		)
		data_list.append(tup)

	try:
		# connect to databse
		conn = sqlite3.connect(db_name)
		cur = conn.cursor()
	except Exception as e:
		print('Connectin Exception: ', e)

	try:
		cur.executemany(insert_query, data_list);
	except Exception as e:
		print('Insert Exception: ', e)
	else:
		print('row count :', cur.rowcount)
		print('----------------------------------')
		conn.commit()
		conn.close()

def top_headlines():
	"""
	This method get the data from NewsApi.
	"""
	##### variables ####
	apikey = config('apikey')
	q=''
	language='en' # ar de en es fr he it nl no pt ru se ud zh
	country='in'
	category= ['general', 'business', 'entertainment', 'health', 'science', 'sports', 'technology']
	pageSize= 100 # defalut = 20, max= 100 
	page=1

	# api in url string
	#request_params = 'country={1}&category={2}&pageSize={3}&page={4}&q={5}&apiKey={0}'.format(apikey, country, category, pageSize, page, q)
	#top_headline_url_with_key = 'https://newsapi.org/v2/top-headlines?{0}'.format(request_params)
	
	# api in http header
	for cate in category:
		print('Category: ',cate)
		headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(apikey)}
		request_params = 'language={0}&country={1}&pageSize={2}&page={3}&q={4}&category={5}'.format(language, country, pageSize, page, q, cate)
		top_headline_url_without_key = 'https://newsapi.org/v2/top-headlines?{0}'.format(request_params)

		try:
			response = requests.get(top_headline_url_without_key, headers=headers)
		except Exception as e:
			print('Exception: ', e)
		else:
			data = eval(response.text.replace(':null', ":'null'"))
			if response.status_code != 200:
				print(response.status_code)
				print('Errro code: ', data['code'])
				print('Errro message: ', data['message'])
			else:
				if data['status'] == "error":
					print('Errro code: ', data['code'])
					print('Errro message: ', data['mes=headerssage'])
				else:
					print('Status:', data['status'])
					print('Total count', data['totalResults'])

					# calling function to insert data
					json_to_db(data, cate)

#######################################################################################

def json_to_newsdb(data):
	"""
	This method store the news source in database.
	"""
	BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	db_name = os.path.join(BASE_DIR, 'db.sqlite3') 
	
	table_name = 'newsapp_newssource'
	# insert query
	table_cols = "name, description, url"
	insert_query = """INSERT OR IGNORE INTO {table_name}({table_cols}) 
		VALUES(?,?,?);""".format(table_name=table_name, table_cols=table_cols)

	# count of data in json
	data_list = list()
	data_count = json.dumps(data).count('"id":')

	# data to insert
	for i in range(data_count):
		name = data['sources'][i]['name']
		description = data['sources'][i]['description']
		url = data['sources'][i]['url']

		# data_list
		tup = (name, description, url)
		data_list.append(tup)

	try:
		# connect to databse
		conn = sqlite3.connect(db_name)
		cur = conn.cursor()
	except Exception as e:
		print('Connectin Exception: ', e)

	try:
		cur.executemany(insert_query, data_list);
	except Exception as e:
		print('Insert Exception: ', e)
	else:
		print('Source count :', cur.rowcount)
		print('----------------------------------')
		conn.commit()
		conn.close()


def newsSource():
	##### variables ####
	apikey =  config('apikey')
	language='en' # ar de en es fr he it nl no pt ru se ud zh
	country='in'

	# request header
	headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(apikey)}
	request_params = 'language={0}'.format(language)
	endpoint = "https://newsapi.org/v2/sources?{0}".format(request_params)

	# requests
	try:
		response = requests.get(endpoint, headers=headers)
	except Exception as e:
		print('Exception: ', e)
	else:
		data = eval(response.text.replace(':null', ":'null'"))
		if response.status_code != 200:
			print(response.status_code)
			print('Errro code: ', data['code'])
			print('Errro message: ', data['message'])
		else:
			if data['status'] == "error":
				print('Errro code: ', data['code'])
				print('Errro message: ', data['mes=headerssage'])
			else:
				print('Status:', data['status'])
				# insert data
				json_to_newsdb(data)




#################################################################################################


top_headlines()

# run command : celery -A Project_news worker -l info