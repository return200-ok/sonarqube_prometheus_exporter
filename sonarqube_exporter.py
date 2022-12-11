import json
import time

import pandas as pd
from prometheus_client import Enum, Gauge, Info, start_http_server

from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

def get_stat(metrics):
    stats = []
    for metric in metrics:
        if metric['type'] in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC', 'RATING', 'WORK_DUR']:
            g = Gauge(metric['key'], metric['name'], ['project_key', 'domain'])
        elif metric['key'] == 'alert_status':
            g = Enum(metric['key'], metric['name'], ['project_key', 'domain'], states=['ERROR', 'OK'])
        else:
            print('metrics is not supported')
        stats.append({'stat':g, 'metric':metric})
    return stats

def gen_metrics(stats):
    g = stats['stat']
    metric = stats['metric']
    projects = list(sonar.projects.search_projects())
    for p in projects:
        component = sonar.measures.get_component_with_specified_measures(component=p['key'], fields="metrics", metricKeys=metric['key'])
        measures = component['component']['measures']
        global value
        if len(measures) > 0:
            if 'value' in measures[0]:
                try:
                    value = measures[0]['value']
                except (KeyError, IndexError, NameError) as error:
                    print(error)
                    raise error
            elif 'periods' in measures[0]:
                try:
                    value = measures[0]['periods'][0]['value']
                except (KeyError, IndexError, NameError) as error:
                    print(error)
                    raise error
            if metric['type'] in ['INT', 'FLOAT', 'PERCENT', 'MILLISEC', 'RATING', 'WORK_DUR']:
                g.labels(
                    project_key=p['key'], 
                    domain=metric['domain'],
                ).set(value)
            elif metric['key'] == 'alert_status':
                g.labels(
                    project_key=p['key'], 
                    domain=metric['domain'],
                ).state(value)
            else:
                print('metrics is not supported')

stat_rule = Gauge('stat_rule', 'Frequency of rule', ['project_key', 'rule'])
def get_rule():
    projects = list(sonar.projects.search_projects())
    for p in projects:
        issues1 = list(sonar.issues.search_issues(componentKeys=p['key']))
        rules = []
        for i in issues1:
            rules.append(i['rule'])
        sr = pd.Series(rules)
        fre = sr.value_counts()
        d = fre.to_json()
        j_data = json.loads(d)

        for key, value in j_data.items():
            stat_rule.labels(
                project_key=p['key'], 
                rule=key,
            ).set(value)

def main():
    metrics = list(sonar.metrics.search_metrics())
    stats = get_stat(metrics)
    start_http_server(8198)
    while True:
        get_rule()
        for s in stats:
            gen_metrics(s)
        time.sleep(60)

if __name__ == "__main__":
    main()

    


