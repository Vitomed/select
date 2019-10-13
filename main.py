from flask import Flask
import requests
import functions

# app = Flask(__name__)

"""
1. Прием Сообщений
2. Отсылка Сообщений
"""

URL = 'https://api.telegram.org/bot703365642:AAHdmF8_VWdOyrk4ODQYDRpieiUgunKPobI/'

# '703365642:AAHdmF8_VWdOyrk4ODQYDRpieiUgunKPobI'

def main():
    r = requests.get(URL + 'getMe/')
    print(r.json())



if __name__ == "__main__":
    main()