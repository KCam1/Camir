from bs4 import BeautifulSoup
import requests

URL = 'http://stash.compciv.org/2017/webby/pets.html'

with open('URL') as html_file:
        soup = BeautifulSoup(html_file,'lxml')

webpage = soup.find('div',class_='collapsible-content')

school = webpage.p.a.text

print(school)

# rawhtml = requests.get(URL).text
# soup = BeautifulSoup(rawhtml, 'lxml')

# links = soup.select('a')
# print(links)
# #https://www.wearecms.com/apps/pages/allschools