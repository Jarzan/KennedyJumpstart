import os
import shutil

import requests


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    #
    data = get_data_from_url(url)
    #  Save the cat image to a folder:
    save_image(folder, name, data)


def get_data_from_url(url):
    """Let's use Requests package from PyPi to download
    the data from this url"""
    response = requests.get(url, stream=True)
    #  raw=binary stream of data that we want to work with:
    return response.raw


def save_image(folder, name, data):
    # This gives a fetched cat pic-file a name and puts it into folder we defined:
    file_name = os.path.join(folder, name + '.jpg')
    #  web site file stream is fetched with open()-command
    # 'wb' as write binary. read is default for open()-method.
    #  shell util-module with copyfileobj() can copy this data stream(data) to that data stream(fout).
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
