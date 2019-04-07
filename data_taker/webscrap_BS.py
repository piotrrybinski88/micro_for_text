'''
web scraping using BeatifulSoup
'''
import requests
from bs4 import BeautifulSoup
import csv
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'yt_link'])


for article in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    # take source atrribute from dict

    try:
        vid_source = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_source.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)

    except Exception as e:
        yt_link = None

    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()


