import time

import requests
from prometheus_client import Gauge, Info, start_http_server

import sonarqube
from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

stat_gauge = Gauge('name', 'description', ['project_key', 'domain'])

def metric_types(metric_type, value):
    if metric_type in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC']:
        return float(value)
    elif metric_type == 'BOOL':
        return bool(value)
    elif metric_type in ['STRING', 'DATA', 'LEVEL', 'DISTRIB', 'RATING', 'WORK_DUR']:
        return str(value)
    else:
        return value

# def get_list_projects(server, token):
#     sonar = SonarQubeClient(sonarqube_url=server, token=token)
#     return list(sonar.projects.search_projects())

# def get_list_metrics(server, token):
#     sonar = SonarQubeClient(sonarqube_url=server, token=token)
#     return list(sonar.metrics.search_metrics())

# def get_stat():
#     metrics = get_list_metrics(sonarqube_server, sonarqube_token)
#     for i in metrics:
        
# _metric_init
def create_metrics():
    projects = list(sonar.projects.search_projects())
    metrics = list(sonar.metrics.search_metrics())
    for m in metrics:
        # stat_gauge = Gauge(m['key'], m['name'], ['project_key', 'domain'])
        for p in projects:
            component = sonar.measures.get_component_with_specified_measures(component=p['key'], fields="metrics", metricKeys=m['key'])
            measures = component['component']['measures']
            value = 0
            if len(measures) > 0:
                if 'value' in measures[0]:
                    try:
                        value = metric_types(m['type'], measures[0]['value'])
                    except (KeyError, IndexError, NameError) as error:
                        value = -1
                        raise error
                elif 'periods' in measures[0]:
                    try:
                        value = metric_types(m['type'], measures[0]['periods'][0]['value'])
                    except (KeyError, IndexError, NameError) as error:
                        value = -1
                        raise error
            if m['type'] in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC']:
                stat_gauge.labels(
                    project_key=p['key'], 
                    domain=m['domain'],
                ).set(value)

def main():
    start_http_server(8198)
    while True:
        create_metrics()
        time.sleep(5)

main()

# create_metrics()