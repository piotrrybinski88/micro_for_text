__version__ = '0.0.1'
import unittest
from parameterized import parameterized_class
import requests
import os


def build_request_only_url(
    url: str,
    web_url: str,
):
    """Build request for integration tests
    parameters:
        url - port:host to connect with API
        web_url - url website to scrap
    """

    result = requests.get(
            f"{url}/taker?url={web_url}"
        )
    return result


def build_request_to_download(
    url: str,
    web_url: str,
    directory: str,
    path: str
):

    result = requests.get(
            f"{url}/taker/save?url={web_url}&path={path}&directory={directory}"
        )
    return result


arg_url_only = {
    'url_hostport': os.getenv('LOCALHOST_URL'),
    'web_url': 'https://conda.io/projects/conda/en/latest/user-guide/tasks/'
    'manage-environments.html#id5',
}

arg_download = {
    'path': 'C:/Users/piotr.rybinski.1/obrazy_z_internet/',
    'directory': 'realpython1'
}


@parameterized_class([
    {"request": build_request_only_url(
        **arg_url_only)},
    {"request": build_request_to_download(
        **arg_url_only,
        **arg_download
        )}
    ])
class TestMicroservice(unittest.TestCase):

    def test_chart_status_code(self):
        check_status_code = self.request.status_code

        self.assertEqual(check_status_code, 200)

    def test_request_time(self):
        request_time = self.request.elapsed.total_seconds()
        self.assertTrue(request_time < 2)


if __name__ == "__main__":

    unittest.main()
