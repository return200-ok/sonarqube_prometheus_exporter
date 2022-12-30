from lib.util import get_json, sr_to_json
from prometheus_client import Enum, Gauge, Info


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
    
def get_value(measures):
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
    return value

def common_metrics(sonar, stats):
    g = stats['stat']
    metric = stats['metric']
    projects = list(sonar.projects.search_projects())
    for p in projects:
        component = sonar.measures.get_component_with_specified_measures(component=p['key'], fields="metrics", metricKeys=metric['key'])
        measures = component['component']['measures']
        global value
        if len(measures) > 0:
            value = get_value(measures)
            # if 'value' in measures[0]:
            #     try:
            #         value = measures[0]['value']
            #     except (KeyError, IndexError, NameError) as error:
            #         print(error)
            #         raise error
            # elif 'periods' in measures[0]:
            #     try:
            #         value = measures[0]['periods'][0]['value']
            #     except (KeyError, IndexError, NameError) as error:
            #         print(error)
            #         raise error
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
def rule_metrics(sonar):
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

stat_event = Info('project_analyses_and_events', 'Description of project analyses', ['project_key'])
def event_metrics(sonar):
    projects = list(sonar.projects.search_projects())
    for p in projects:
        project_analyses_and_events = list(sonar.project_analyses.search_project_analyses_and_events(project=p['key']))
        for event in project_analyses_and_events:
            event_id = get_json("key", event)
            date = get_json("date", event)
            project_version = get_json("projectVersion", event)     
            value = {'event_id': event_id, 'date': date, 'project_version': project_version}   
            stat_event.labels(
                project_key=p['key'], 
            ).info(value)



    


