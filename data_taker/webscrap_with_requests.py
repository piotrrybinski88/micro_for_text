from requests_html import HTML, HTMLSession

# list of arcticles
url = 'http://coreyms.com'

session = HTMLSession()

r = session.get(url)

articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    summary = article.find('.entry-content p', first=True).text
    try:
        vid_source = article.find('iframe', first=True).attrs['src']
        vid_id = vid_source.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)

    except Exception as e:
        yt_link = None

print(article.html)

'''
session = HTMLSession()

r = session.get(url)
# links from website
for link in r.html.links.absolute_links:
    print(link)
'''

match = html.find('#footer', first=True)
