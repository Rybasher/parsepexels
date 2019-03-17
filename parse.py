import os, urllib, webbrowser
import requests
from bs4 import BeautifulSoup
import pathlib
import csv
from datetime import datetime
from multiprocessing import Pool
#
# urls = [
#     'https://images.pexels.com/photos/772662/pexels-photo-772662.jpeg',
#     'https://images.pexels.com/photos/1994904/pexels-photo-1994904.jpeg',
#     'https://images.pexels.com/photos/1983772/pexels-photo-1983772.jpeg'
# ]


urls = []


def get_html(url):
    r = requests.get(url, stream=True)
    return r


def get_img_data(html):
    soup = BeautifulSoup(html.text, 'lxml')
    imgs = soup.find('div', class_='photos').find_all('img', class_='photo-item__img')
    for img in imgs:
        some = img.get('src')
        urls.append(some)


def get_name(url):
    name = url.split('/')[-1].split('?')[0]
    folder = name.split('-')[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    return path + '/' + name
    # name = url.split('/')[-1]
    # folder = name.split('-')[0]
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # path = os.path.abspath(folder)
    # return path + '/' + name


def save_image(name, file_object):
    with open(name, 'wb') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


def main():
    url = 'https://www.pexels.com/'
    get_img_data(get_html(url))
    print(len(urls))
    print(urls)

    with Pool(30):
        for i in urls:
            print(get_name(i).split('-')[0])
            # path = pathlib.Path(i)
            # save_image(get_name(i), get_html(i))
            # # print(path)


if __name__ == "__main__":
    main()
