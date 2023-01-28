# It's importing the libraries that we need to use in this script.
import json
import logging
import re
import sys
from datetime import datetime

import pandas as pd
import requests
import rfc3339


def get_date_string(date_object):
    """
    It takes a date object and returns a string in RFC 3339 format
    
    :param date_object: A datetime object
    :return: A string in RFC 3339 format.
    """
    return rfc3339.rfc3339(date_object)

# Configuring the logging handler.
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
fileName = get_date_string(datetime.now())+'sonarqube_exporter'
logPath = 'logs'
fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)

# To avoid duplicated logs.
if (rootLogger.hasHandlers()):
    rootLogger.handlers.clear()
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger()

# Convert sr to json
def sr_to_json(series):
    """
    It takes a pandas series, converts it to a json object, and returns the json object
    
    :param series: the series you want to convert to json
    :return: A dictionary with the keys being the unique values in the series and the values being the
    counts of those values.
    """
    sr = pd.Series(series)
    fre = sr.value_counts()
    d = fre.to_json()
    j_data = json.loads(d)
    return j_data

def get_json(element, json_data):
    """
    If the element is in the json_data, return the value of that element, otherwise return 0
    
    :param element: The element in the JSON file that you want to extract
    :param json_data: The JSON data that we're going to be working with
    :return: The value of the key in the json_data dictionary.
    """
    if element in json_data:
        return json_data[element]
    else:
        return 0

def get_data(url, token):
# Getting the data from the url and converting it to JSON.
  session = requests.Session()
  session.auth = token, ''
  call = getattr(session, 'get')
  res = call(url)
  data = json.loads(res.content)
  return data

def convert(string):
    """
    It takes a string, finds the number and unit, and returns the number of bytes
    
    :param string: The string to be converted
    :return: The number of bytes in the string.
    """
    value = re.search(r'([0-9]+)', string)
    unit = re.search(r'([A-Z]?B)', string)

    num = int(value.group())
    unit = unit.group()
    if unit == 'B':
        return num
    num *= 1024

    if unit == 'KB':
        return num
    num *= 1024

    if unit == 'MB':
        return num
    num *= 1024

    if unit == 'GB':
        return num
    num *= 1024

    if unit == 'TB':
        return num
        