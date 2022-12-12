import json
import logging
import sys
from datetime import datetime, timedelta

import pandas as pd
import rfc3339

'''
Config logging handler
'''
def get_date_string(date_object):
  return rfc3339.rfc3339(date_object)

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
fileName = get_date_string(datetime.now())+'_gitlab_collecter'
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