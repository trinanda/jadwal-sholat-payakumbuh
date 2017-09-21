import bs4
from data.data_url import minta_url


panggil_bs4 = bs4.BeautifulSoup(minta_url, 'html.parser')

cari = panggil_bs4.find_all('tr','table_highlight')



