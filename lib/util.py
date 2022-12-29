import json
import logging
import re
import sys
from datetime import datetime

import pandas as pd
import requests
import rfc3339

'''
Config logging handler
'''
def get_date_string(date_object):
  return rfc3339.rfc3339(date_object)

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
fileName = get_date_string(datetime.now())+'sonarqube_exporter'
logPath = 'logs'
fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)

'''
    Avoid duplicated logs
'''
if (rootLogger.hasHandlers()):
    rootLogger.handlers.clear()
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger()

def sr_to_json(series):
    sr = pd.Series(series)
    fre = sr.value_counts()
    d = fre.to_json()
    j_data = json.loads(d)
    return j_data

def get_json(element, json_data):
  if element in json_data:
    return json_data[element]
  else:
    return 0

#Get data from url and convert to JSON
def get_data(url, token):
  session = requests.Session()
  session.auth = token, ''
  call = getattr(session, 'get')
  res = call(url)
  data = json.loads(res.content)
  return data

def convert(string):
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