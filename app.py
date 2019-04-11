'''
Script which take text and images from website and save them on disk
using Python 3.7 and libraries Flask, requests, web_scrap
"
Write text and links to images from website

curl "http://localhost:5000/taaker?url='https://realpython.com/read-write-files-python/'"
'''
__version__ = '0.0.1'

from flask import Flask
from flask import request
from data_taker import web_scrap

take_data_from_website = Flask(__name__)


@take_data_from_website.route('/taker')
def take_from_website():
    '''take text and images from website, this can be use via curl
    Parameters:
        url - website url from which you want to take data
    '''
    # flask request from curl
    url = request.args.get('url')
    text = web_scrap.prepare_text_to_download(url)
    links_to_images = web_scrap.take_images_links_to_list(url)

    return f'text from web{text} \n links to images: {links_to_images}'


@take_data_from_website.route('/taker/save')
def save_all_to_disk():
    arguments = {
        'url': request.args.get('url'),
        'new_directory': request.args.get('directory'),
        'path': request.args.get('path')
    }

    dn_text = web_scrap.download_text(
        **arguments)
    dn_images = web_scrap.download_all_images(
        **arguments)
    return f'{dn_images}, {dn_text}'


if __name__ == '__main__':
    take_data_from_website.run(debug=False, host='0.0.0.0')
