import requests


# do wszystkiego testy
def check_status_code(request_from_curl):
    code_status = request_from_curl.status_code
    if code_status == 200:
        return 'code status 200, connection ok'


def text_from_website(url: str):
    '''Funkcja do pobierania stony z urla
    '''
    website = requests.get(url)
    check_status_code(website)
    return website.text


# funkcja do przerobienia
def write_file(path):
    '''
    path - can be 'C:\\Users\\piotr.rybinski.1\\microservice_from_web\\micro_for_text\\text_form_website.txt'
    '''
    with open(
        path,
        'a'
    ) as a_writer:
        a_writer.write('\n it is going right')
    return 'File saved'
