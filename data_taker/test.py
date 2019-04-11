import unittest
import web_scrap as ws
from requests import get
from parameterized import parameterized_class
import os.path
import os

url_valid = 'https://realpython.com/courses/running-python-scripts/'
url_invalid = 'https://realpython.com/courses/running-p'
path = 'C:\\Users\\piotr.rybinski.1\\microservice_from_web'
file_path_img = 'C:\\Users\\piotr.rybinski.1\\microservice_from_web\\'\
    'image1.jpg'
text_path = 'C:\\Users\\piotr.rybinski.1\\microservice_from_web\\test_text\\'\
    'text_from_web.txt'


class TestFunctions(unittest.TestCase):

    def test_invalid_url(self):
        content = ws.simple_get(url_invalid)
        self.assertIsNone(content)

    def test_type_simple_get(self):

        content = ws.simple_get(url_valid)
        self.assertEqual(type(content), bytes)

    def test_is_good_response(self):

        response = get(url_valid)
        content = ws.is_good_response(response)
        self.assertTrue(content)

    def test_take_text_from_url(self):

        text = ws.take_text_from_url_bs(url_valid)
        self.assertIsInstance(text[1], str)

    def test_prepare_take_images(self):

        links = ws.take_images_links_to_list(url_valid)
        self.assertIsInstance(links[1], str)

    def test_build_path(self):

        new_path = ws.build_path(
            path='C:/user/',
            new_directory='first_page')
        self.assertEqual(new_path, 'C:/user/first_page')

    def test_prepare_text_to_download(self):

        text = ws.prepare_text_to_download(url_valid)
        self.assertIsInstance(text, str)


@parameterized_class([
    {'func': ws.prepare_html_from_url_bs(url_valid)},
    {'func': ws.prepare_html_from_url_req(url_valid)}
])
class TestPrepareHtml(unittest.TestCase):

    def test_prepare_html_from_url_valid(self):

        html = self.func
        self.assertIsNotNone(html)


@parameterized_class([
    {'func': ws.download_jpg(
        link='https://files.realpython.com/media/'
        'How-to-Run-A-Python-Script_Watermarked.65fe32bf5487.jpg',
        path=path,
        num=1
        ),
     'file_path': file_path_img
     },
    {'func': ws.download_text(
        url=url_valid,
        new_directory='\\test_text',
        path=path),
     'file_path': text_path
     }
    ])
class TestTherIsFile(unittest.TestCase):

    def test_existenst_of_file(self):

        self.func
        self.assertTrue(os.path.isfile(self.file_path))
        os.remove(self.file_path)


if __name__ == "__main__":

    unittest.main()
