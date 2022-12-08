import time

import requests
from prometheus_client import Enum, Gauge, Info, start_http_server

import sonarqube
from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

def get_stat(metrics):
    stats = []
    for metric in metrics:
        if metric['type'] in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC', 'RATING', 'WORK_DUR']:
            g = Gauge(metric['key'], metric['name'], ['project_key', 'domain'])
        elif metric['type'] == 'LEVEL':
            g = Enum(metric['key'], metric['name'], ['project_key', 'domain'], states=['ERROR', 'OK'])
        elif metric['type'] in ['STRING', 'DATA', 'DISTRIB']:
            g = Info(metric['key'], metric['name'], ['project_key', 'domain'])
        stats.append({'stat':g, 'metric':metric})
    return stats

def map_value_type(metric_type, value):
    if metric_type in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC', 'RATING', 'WORK_DUR']:
        return float(value)
    # elif metric_type == 'BOOL':
    #     return bool(value)
    elif metric_type in ['STRING', 'DATA', 'LEVEL', 'DISTRIB']:
        return str(value)
    else:
        return value

def gen_metrics(stats):
    g = stats['stat']
    metric = stats['metric']
    projects = list(sonar.projects.search_projects())
    for p in projects:
        component = sonar.measures.get_component_with_specified_measures(component=p['key'], fields="metrics", metricKeys=metric['key'])
        measures = component['component']['measures']
        value = 0
        if len(measures) > 0:
            if 'value' in measures[0]:
                try:
                    value = map_value_type(metric['type'], measures[0]['value'])
                except (KeyError, IndexError, NameError) as error:
                    value = -1
                    raise error
            elif 'periods' in measures[0]:
                try:
                    value = map_value_type(metric['type'], measures[0]['periods'][0]['value'])
                except (KeyError, IndexError, NameError) as error:
                    value = -1
                    raise error
        if metric['type'] in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC']:
            g.labels(
                project_key=p['key'], 
                domain=metric['domain'],
            ).set(value)
        # elif metric['type'] == 'LEVEL':
        #     g.labels(
        #         project_key=p['key'], 
        #         domain=metric['domain'],
        #     ).state(value)
        # elif metric['type'] in ['STRING', 'DATA', 'DISTRIB']:
        #     g.labels(
        #         project_key=p['key'], 
        #         domain=metric['domain'],
        #     ).info(str(value))

def main():
    metrics = list(sonar.metrics.search_metrics())
    stats = get_stat(metrics)
    start_http_server(8198)
    while True:
        for s in stats:
            gen_metrics(s)
        time.sleep(5)

if __name__ == "__main__":
    main()


