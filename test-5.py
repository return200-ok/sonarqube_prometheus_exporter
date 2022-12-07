import time

import requests
from prometheus_client import Gauge, start_http_server

name = ['influx', 'grafana', 'python']

def get_stat(name):
    stats = []
    for i in name:
        stat = Gauge(i, 'document')
        stats.append(stat)
    return stats

def get_server_info(stat):
        stat.inc()

def main():
    start_http_server(8192)
    for i in name:
        i = Gauge(i, 'All players in 3 servers')
        print(i)
        
        # get_server_info(i)
            # break
        # time.sleep(5)

# main()
# print(get_stat(name))
list_metrics = get_stat(name)
# print(list_metrics)
start_http_server(8192)
while True:
    for i in list_metrics:
        get_server_info(i)
        # print(i)