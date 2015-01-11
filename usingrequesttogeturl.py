import requests

url = 'http://topblogcoder.com'
html = requests.get(url)
print(html.content)