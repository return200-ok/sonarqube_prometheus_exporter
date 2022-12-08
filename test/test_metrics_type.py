from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

metrics = list(sonar.metrics.search_metrics())

SONAR_TYPE = ['INT', 'FLOAT', 'PERCENT', 'MILLISEC', 'BOOL', 'STRING', 'DATA', 'LEVEL', 'DISTRIB', 'RATING', 'WORK_DUR']

INT = []
FLOAT = []
PERCENT = []
MILLISEC = []
BOOL = []
STRING = []
DATA = []
LEVEL = []
DISTRIB = []
RATING = []
WORK_DUR = []

for i in metrics:
    if i['type'] == 'INT':
        INT.append(i['key'])
    elif i['type'] == 'FLOAT':
        FLOAT.append(i['key'])
    elif i['type'] == 'PERCENT':
        PERCENT.append(i['key'])
    elif i['type'] == 'MILLISEC':
        MILLISEC.append(i['key'])
    elif i['type'] == 'BOOL':
        BOOL.append(i['key'])
    elif i['type'] == 'STRING':
        STRING.append(i['key'])
    elif i['type'] == 'DATA':
        DATA.append(i['key'])
    elif i['type'] == 'LEVEL':
        LEVEL.append(i['key'])
    elif i['type'] == 'DISTRIB':
        DISTRIB.append(i['key'])
    elif i['type'] == 'RATING':
        RATING.append(i['key'])
    elif i['type'] == 'WORK_DUR':
        WORK_DUR.append(i['key'])

print(LEVEL)