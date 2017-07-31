import requests
url = 'http://172.16.0.30:8090/httpclient.html'
values = {'username':'h2016034',
			'password': 'Sh@@rawy92'}
r = requests.post(url,data=values)
print (r.content)