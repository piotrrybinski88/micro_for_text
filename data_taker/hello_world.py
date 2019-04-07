from flask import Flask
from flask import request
# import requests as rs

take_data_from_website = Flask(__name__)


@take_data_from_website.route(
    '/url',
    methods=['GET']
)
def take_from_website():
    return "hello World"

if __name__ == '__main__':
    take_data_from_website.run(debug=False)
