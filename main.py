import os
import time

import prometheus_client as prom
from lib.analysis_metrics import (common_metrics, event_metrics, get_stat,
                                  rule_metrics)
from lib.system_metrics import system_metric
from prometheus_client import start_http_server
from sonarqube import SonarQubeClient

# Set the default value of the environment variable.
sonarqube_server = os.environ.get('SONARQUBE_SERVER', 'http://192.168.3.101:9001')
sonarqube_token = os.environ.get('SONARQUBE_TOKEN', 'squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e')

exporter_listen_host = os.environ.get('EXPORTER_LISTEN_HOST', '0.0.0.0')
exporter_listen_port = os.environ.get('EXPORTER_LISTEN_PORT', 8198)


def schedule(minutes, task):
# A function that will run the task every minute.
    while True:
        try:
            tic = time.time()
            task()
            duration = time.time() - tic
            sleep_time = max(60 * minutes - int(duration), 1)
            print("Sleeping %d seconds" % sleep_time)
            time.sleep(max(sleep_time, 0))
        except (KeyboardInterrupt, SystemExit) as e:
            raise e
        except Exception as e:
            print(e)

def exporter_start():

# Printing the server address and port.
    print('Starting server http://{}:{}/metrics'.format(
    exporter_listen_host, exporter_listen_port))

# Unregistering the default collectors from the registry.
    prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
    prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
    prom.REGISTRY.unregister(prom.GC_COLLECTOR)

    sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)
    projects = list(sonar.projects.search_projects())
    metrics = list(sonar.metrics.search_metrics())
    list_stat = get_stat(metrics)
    def metrics_task():
        """
        A function that is used to collect metrics from SonarQube.
        """
        system_metric(sonarqube_server, sonarqube_token)
        for stats in list_stat:
            common_metrics(projects, sonar, stats)
        rule_metrics(projects, sonar)
        event_metrics(projects, sonar)
    try:
        start_http_server(exporter_listen_port, addr=exporter_listen_host)
        schedule(minutes=1, task=metrics_task)
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)

if __name__ == "__main__":
    exporter_start()


    


