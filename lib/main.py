import json
import time

import pandas as pd
from prometheus_client import Enum, Gauge, Info, start_http_server
from until import logger, sr_to_json

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

def common_metrics(stats):
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
        else:
            print('component doesnt have metric')

stat_rule = Gauge('stat_rule', 'Frequency of rule', ['project_key', 'rule'])
def rule_metrics():
    projects = list(sonar.projects.search_projects())
    for p in projects:
        issues1 = list(sonar.issues.search_issues(componentKeys=p['key']))
        rules = []
        for i in issues1:
            rules.append(i['rule'])
        j_data = sr_to_json(rules)

        for key, value in j_data.items():
            stat_rule.labels(
                project_key=p['key'], 
                rule=key,
            ).set(value)

def schedule(minutes, task):
    while True:
        try:
            tic = time.time()
            task()
            duration = time.time() - tic
            sleep_time = max(60 * minutes - int(duration), 1)
            logger.info("sleeping %d seconds" % sleep_time)
            time.sleep(max(sleep_time, 0))
        except (KeyboardInterrupt, SystemExit) as e:
            raise e
        except Exception as e:
            logger.exception(e)

def main():
    metrics = list(sonar.metrics.search_metrics())
    stats = get_stat(metrics)
    def metrics_task():
        rule_metrics()
        for s in stats:
            common_metrics(s)
    try:
        start_http_server(8198)
        schedule(minutes=1, task=metrics_task)
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)


if __name__ == "__main__":
    main()

    


