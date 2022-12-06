import time

import requests
from prometheus_client import Gauge, Info, start_http_server

from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

event = Info('event', 'Description of info')
bugs = Gauge('bugs', 'BUG_TOTAL', ['project_key'])

def create_metrics():
    projects = list(sonar.projects.search_projects())
    for i in projects:
        component = sonar.measures.get_component_with_specified_measures(component=i['key'], branch="master", fields="metrics", metricKeys="bugs")
        try:
            value = component['component']['measures'][0]['value']
        except IndexError:
            value = -1
        bugs.labels(i['key']).set(value)

def main():
    start_http_server(8198)
    while True:
        create_metrics()
        time.sleep(60)

main()