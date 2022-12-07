from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)
metrics = list(sonar.metrics.search_metrics())
metric_types = sonar.metrics.get_metrics_types()

# for i in metrics:
#     print(i['key'])

print(metrics[0])
# print(metric_types)