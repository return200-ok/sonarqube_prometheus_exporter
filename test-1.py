import time

import requests
from prometheus_client import Gauge, Info, start_http_server

import sonarqube
from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

event = Info('event', 'Description of info')
bugs = Gauge('bugs', 'BUG_TOTAL', ['project_key'])


metrics = ['bugs', 'covered_conditions_by_line']
def create_metrics():
    projects = list(sonar.projects.search_projects())
    for i in projects:
        for m in metrics:
            try:
                component = sonar.measures.get_component_with_specified_measures(component=i['key'], branch="master", fields="classes", metricKeys=m)
            except sonarqube.utils.exceptions.NotFoundError:
                print('metrics not found')
            
            print(component)

# def main():
#     start_http_server(8198)
#     while True:
#         create_metrics()
#         time.sleep(60)

# main()
create_metrics()