import json

import pandas as pd
from prometheus_client import Enum, Gauge, Info, start_http_server

from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

metrics = list(sonar.metrics.search_metrics())
rule_repositories = sonar.rules.get_rule_repositories()
# issues1 = list(sonar.issues.search_issues(componentKeys="bac"))
# rules = []
# for i in issues1:
#     # print(i['rule'])
#     rules.append(i['rule'])

# # importing pandas as pd
# import pandas as pd

# # creating the Series
# sr = pd.Series(rules)

# # finding the unique count
# fre = sr.value_counts()

# d = fre.to_json()

# j = json.loads(d)

# print(type(j))

# for key, value in j.items():
#     print(key, value)

stat_rule = Gauge('stat_rule', 'Frequency of rule', ['project_key', 'rule'])
def get_rule():
    projects = list(sonar.projects.search_projects())
    for p in projects:
        issues1 = list(sonar.issues.search_issues(componentKeys=p['key']))
        rules = []
        for i in issues1:
            rules.append(i['rule'])
        print(rules)
        sr = pd.Series(rules)
        fre = sr.value_counts()
        d = fre.to_json()
        j_data = json.loads(d)

        for key, value in j_data.items():
            print(key, value)
            # stat_rule.labels(
            #     project_key=p['key'], 
            #     rule=key,
            # ).state(value)
get_rule()