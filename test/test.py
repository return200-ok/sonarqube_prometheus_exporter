# from sonarqube import SonarQubeClient

# sonarqube_server = "http://192.168.3.101:9001"
# sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
# sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

# metrics = list(sonar.metrics.search_metrics())
# # task = sonar.get_list_tasks()
# # print(task)

# project_analyses_and_events = list(sonar.project_analyses.search_project_analyses_and_events(project="bac"))
# print(project_analyses_and_events)



# import configparser
# import os
# import sys
# import time

# from prometheus_client import start_http_server
# from prometheus_client.core import REGISTRY, GaugeMetricFamily
# import prometheus_client as prom
# prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
# prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
# prom.REGISTRY.unregister(prom.GC_COLLECTOR)

# g = prom.Gauge("test", "test")

# # Total groups
# metric = GaugeMetricFamily(
#     'sonar_groups_total',
#     'Total groups in Sonar',
#     labels=None
# )
# start_http_server(9119)
# while True:
#     metric.add_metric(
#         labels=[],
#         value='8'
#     )
#     time.sleep(1)

