import requests

url = 'http://jadwalsholatimsak.info/monthly.php?id=193'

panggil_url = requests.get(url)

minta_url = panggil_url.text