from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from requests_html import HTML
from pathlib import Path
from typing import List


def simple_get(url: str):
    """
    Retrun text if the content-type is HTML, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as response:
            if is_good_response(response):
                return response.content
            else:
                return None

    except RequestException as e:
        log_error(f'Error during requests to {url} : {str(e)}')
    return None


def is_good_response(response):
    '''
    Returns True if response seems to be HTML, False otherwise
    '''
    content_type = response.headers['Content-type'].lower()
    return (response.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    '''print error or save
    '''
    print(e)


def prepare_html_from_url_bs(url: str):
    raw_html = simple_get(url)
    if raw_html is None:
        raise Exception(f'your url are incorrect {url}')
    html = BeautifulSoup(raw_html, 'html.parser')
    return html


def prepare_html_from_url_req(url: str) -> List:
    raw_html = simple_get(url)
    if raw_html is None:
        raise Exception(f'your url are incorrect {url}')
    html = HTML(html=raw_html)
    return html


def take_text_from_url_bs(url: str) -> List:
    '''take text from website wiht BeatifulSoup library
    '''
    html = prepare_html_from_url_bs(url)
    return [p.text for p in html.select('p')]


def take_images_links_to_list(url: str) -> List:
    '''Prepare list of all images form website
       parameters:
           url - website url from which you want take likns to images
    '''
    html = prepare_html_from_url_req(url)
    matches = html.find('img')
    links = [match.attrs['src'] for match in matches]
    return links


def build_path(
    path: str,
    new_directory: str
) -> str:
    '''build new path to download files
    Parameters:
        new_directory - make new directory to download images from site
        path - choose path where you want to build new directory
    '''
    try:
        new_path = f"{path}{new_directory}"
    except Exception as e:
        log_error(e)

    return new_path


def download_jpg(
    link: str,
    path: str,
    num: int
):

    '''download image from link to path
    link - link with image
    path - path where you want to build new directory to
           downloads images eg. 'C:/Users/download/'
    num - to distinct files
    returns - save image as
    '''

    path_to_save = f"{path}/image{num}.jpg"
    try:
        r = get(link)
        if r.status_code == 200:
            with open(path_to_save, 'wb') as f:
                f.write(r.content)
    except Exception as e:
        print(e)


def download_all_images(
    url: str,
    new_directory: str,
    path: str
):
    '''Download all images from list with links to specific directory
    Parameters:
        list_of_links - list of links
        new_directory - make new directory to download images from site
        path - choose path where you want to build new directory
    '''
    # build new_path from your path and new_directory to save images
    new_path = build_path(path, new_directory)
    # prepare list with links to download
    list_of_links = take_images_links_to_list(url)
    # build new directory
    make_directory_to_save_files(new_path)
    num = 1
    for link in list_of_links:
        download_jpg(link, new_path, num)
        num += 1
    return f'download done check directroy {new_path}'


def make_directory_to_save_files(directory: str):
    '''Parameters:
        directory - choose name of your directory
    '''
    p = Path(f'{directory}')
    p.mkdir(exist_ok=True)


def download_text(
    url: str,
    new_directory: str,
    path: str
):
    ''' Download text from url
    Parameters:
        url - website from which you wnt to download text
        new_directory - make new directory to download images from site
        path - choose path where you want to build new directory
    '''
    text = prepare_text_to_download(url)
    new_path = build_path(
        path=path,
        new_directory=new_directory
    )

    make_directory_to_save_files(new_path)

    path_to_save = f"{new_path}/text_from_web.txt"

    with open(path_to_save, 'wt', encoding='utf-8') as f:
        f.write(text)

    return f'text downloaded check {new_path}'


def prepare_text_to_download(
    url: str
) -> str:
    '''replace all unncecessary '\n' with ' ' and then remove ''
    to make text more readability
    url - url to website from which you want to take text
    '''
    list_of_string = take_text_from_url_bs(url)
    text_to_download = list(filter(lambda a: a != '', list_of_string))
    # list to string to easier downloads
    return (' ').join(text_to_download)
