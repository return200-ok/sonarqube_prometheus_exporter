import time

import requests
from prometheus_client import Gauge, Info, start_http_server

from sonarqube import SonarQubeClient

sonarqube_server = "http://192.168.3.101:9001"
sonarqube_token = "squ_af1e521e19aef5c5de1cb6df89adf3cbb3a9759e"
sonar = SonarQubeClient(sonarqube_url=sonarqube_server, token=sonarqube_token)

event = Info('event', 'Description of info')
bugs = Gauge('bugs', 'BUG_TOTAL', ['project_key'])

complexity = "complexity, cognitive_complexity, "
duplications = "duplicated_blocks, duplicated_files, duplicated_lines, duplicated_lines_density, "
new_issues = "new_violations, new_blocker_violations, new_critical_violations, new_major_violations, new_minor_violations, new_info_violations, "
issues = "violations, blocker_violations, critical_violations, major_violations, minor_violations, info_violations, "
status_issue = "false_positive_issues, open_issues, confirmed_issues, reopened_issues, "
maintainability = "code_smells, new_code_smells, sqale_rating, sqale_index, new_technical_debt, sqale_debt_ratio, new_sqale_debt_ratio, "
quality_gates = "alert_status, quality_gate_details, "
reliability = "bugs, new_bugs, reliability_rating, reliability_remediation_effort, new_reliability_remediation_effort, "
security = "vulnerabilities, new_vulnerabilities, security_rating, security_remediation_effort, new_security_remediation_effort, security_hotspots, new_security_hotspots, security_review_rating, new_security_review_rating, security_hotspots_reviewed, "
size = "classes, comment_lines, comment_lines_density, directories, files, lines, ncloc, ncloc_language_distribution, functions, projects, statements, "
test = "branch_coverage, new_branch_coverage, coverage, new_coverage, line_coverage, new_line_coverage, lines_to_cover, new_lines_to_cover, skipped_tests, uncovered_conditions, new_uncovered_conditions, uncovered_lines, new_uncovered_lines, tests, test_execution_time, test_errors, test_failures, test_success_density"
metrics = complexity + duplications + new_issues + issues + status_issue + maintainability + quality_gates + reliability + security + size + test
# print(metrics)
def create_metrics():
    projects = list(sonar.projects.search_projects())
    for i in projects:
        # try:
        component = sonar.measures.get_component_with_specified_measures(component=i['key'], branch="master", fields="classes", metricKeys=metrics)
        # except NotFoundError:
        #     print('metrics not found')
        print(component)

# def main():
#     start_http_server(8198)
#     while True:
#         create_metrics()
#         time.sleep(60)

# main()
create_metrics()