import requests
import webbrowser

file_path = '../data/reinhard-quiz.jfif'
search_url = 'http://www.google.de/searchbyimage/upload'
multi_part = {'encoded_image' : (file_path, open(file_path, 'rb')), 'image_content' : ''}
response = requests.post(search_url, files=multi_part, allow_redirects = False)
fetch_url = response.headers['Location']

webbrowser.open(fetch_url, new = 2)
