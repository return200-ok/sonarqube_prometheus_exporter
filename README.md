# Sonarqube Exporter
`Sonarqube Exporter` is a exporter to get metrics of Sonarqube server 

## List metrics
stat_rule Frequency of rule
```# HELP stat_rule Frequency of rule
# TYPE stat_rule gauge
stat_rule{project_key="bac",rule="java:S115"} 34.0
stat_rule{project_key="bac",rule="java:S1124"} 20.0
stat_rule{project_key="bac",rule="java:S1128"} 20.0
stat_rule{project_key="bac",rule="java:S1659"} 12.0
stat_rule{project_key="bac",rule="java:S1118"} 11.0
stat_rule{project_key="bac",rule="java:S116"} 9.0
stat_rule{project_key="bac",rule="common-java:DuplicatedBlocks"} 7.0
stat_rule{project_key="bac",rule="java:S125"} 7.0
stat_rule{project_key="bac",rule="java:S1905"} 7.0
stat_rule{project_key="bac",rule="java:S101"} 6.0
stat_rule{project_key="bac",rule="java:S1186"} 5.0
```

new_technical_debt Added Technical Debt
```# HELP new_technical_debt Added Technical Debt
# TYPE new_technical_debt gauge
new_technical_debt{domain="Maintainability",project_key="php-xss"} 0.0
```

blocker_violations Blocker Issues
```# HELP blocker_violations Blocker Issues
# TYPE blocker_violations gauge
blocker_violations{domain="Issues",project_key="bac"} 10.0
```

bugs Bugs
```# HELP bugs Bugs
# TYPE bugs gauge
bugs{domain="Reliability",project_key="bac"} 5.0
```

classes Classes
```# HELP classes Classes
# TYPE classes gauge
classes{domain="Size",project_key="bac"} 90.0
```

code_smells Code Smells
```# HELP code_smells Code Smells
# TYPE code_smells gauge
code_smells{domain="Maintainability",project_key="bac"} 190.0
```

cognitive_complexity Cognitive Complexity
```# HELP cognitive_complexity Cognitive Complexity
# TYPE cognitive_complexity gauge
cognitive_complexity{domain="Complexity",project_key="bac"} 403.0
```

comment_lines Comment Lines
```# HELP comment_lines Comment Lines
# TYPE comment_lines gauge
comment_lines{domain="Size",project_key="bac"} 380.0
```

comment_lines_density Comments (%)
```# HELP comment_lines_density Comments (%)
# TYPE comment_lines_density gauge
comment_lines_density{domain="Size",project_key="bac"} 8.0
```

class_complexity Complexity / Class
```# HELP class_complexity Complexity / Class
# TYPE class_complexity gauge
```

file_complexity Complexity / File
```# HELP file_complexity Complexity / File
# TYPE file_complexity gauge
file_complexity{domain="Complexity",project_key="bac"} 5.8
```

function_complexity Complexity / Function
```# HELP function_complexity Complexity / Function
# TYPE function_complexity gauge
```

complexity_in_classes Complexity in Classes
```# HELP complexity_in_classes Complexity in Classes
# TYPE complexity_in_classes gauge
```

complexity_in_functions Complexity in Functions
```# HELP complexity_in_functions Complexity in Functions
# TYPE complexity_in_functions gauge
```

branch_coverage Condition Coverage
```# HELP branch_coverage Condition Coverage
# TYPE branch_coverage gauge
```

new_branch_coverage Condition Coverage on New Code
```# HELP new_branch_coverage Condition Coverage on New Code
# TYPE new_branch_coverage gauge
```

conditions_to_cover Conditions to Cover
```# HELP conditions_to_cover Conditions to Cover
# TYPE conditions_to_cover gauge
```

new_conditions_to_cover Conditions to Cover on New Code
```# HELP new_conditions_to_cover Conditions to Cover on New Code
# TYPE new_conditions_to_cover gauge
new_conditions_to_cover{domain="Coverage",project_key="php-xss"} 0.0
```

confirmed_issues Confirmed Issues
```# HELP confirmed_issues Confirmed Issues
# TYPE confirmed_issues gauge
confirmed_issues{domain="Issues",project_key="bac"} 1.0
```

coverage Coverage
```# HELP coverage Coverage
# TYPE coverage gauge
coverage{domain="Coverage",project_key="bac"} 0.0
```

new_coverage Coverage on New Code
```# HELP new_coverage Coverage on New Code
# TYPE new_coverage gauge
new_coverage{domain="Coverage",project_key="php-xss"} 0.0
```

critical_violations Critical Issues
```# HELP critical_violations Critical Issues
# TYPE critical_violations gauge
critical_violations{domain="Issues",project_key="bac"} 46.0
```

complexity Cyclomatic Complexity
```# HELP complexity Cyclomatic Complexity
# TYPE complexity gauge
complexity{domain="Complexity",project_key="bac"} 485.0
```

last_commit_date Date of Last Commit
```# HELP last_commit_date Date of Last Commit
# TYPE last_commit_date gauge
last_commit_date{domain="SCM",project_key="bac"} 1.65831011e+012
```

new_development_cost Development Cost on New Code
```# HELP new_development_cost Development Cost on New Code
# TYPE new_development_cost gauge
new_development_cost{domain="Maintainability",project_key="php-xss"} 30.0
```

directories Directories
```# HELP directories Directories
# TYPE directories gauge
```

duplicated_blocks Duplicated Blocks
```# HELP duplicated_blocks Duplicated Blocks
# TYPE duplicated_blocks gauge
duplicated_blocks{domain="Duplications",project_key="bac"} 8.0
```

new_duplicated_blocks Duplicated Blocks on New Code
```# HELP new_duplicated_blocks Duplicated Blocks on New Code
# TYPE new_duplicated_blocks gauge
new_duplicated_blocks{domain="Duplications",project_key="php-xss"} 0.0
```

duplicated_files Duplicated Files
```# HELP duplicated_files Duplicated Files
# TYPE duplicated_files gauge
duplicated_files{domain="Duplications",project_key="bac"} 7.0
```

duplicated_lines Duplicated Lines
```# HELP duplicated_lines Duplicated Lines
# TYPE duplicated_lines gauge
duplicated_lines{domain="Duplications",project_key="bac"} 99.0
```

duplicated_lines_density Duplicated Lines (%)
```# HELP duplicated_lines_density Duplicated Lines (%)
# TYPE duplicated_lines_density gauge
duplicated_lines_density{domain="Duplications",project_key="bac"} 1.8
```

new_duplicated_lines_density Duplicated Lines (%) on New Code
```# HELP new_duplicated_lines_density Duplicated Lines (%) on New Code
# TYPE new_duplicated_lines_density gauge
new_duplicated_lines_density{domain="Duplications",project_key="php-xss"} 0.0
```

new_duplicated_lines Duplicated Lines on New Code
```# HELP new_duplicated_lines Duplicated Lines on New Code
# TYPE new_duplicated_lines gauge
new_duplicated_lines{domain="Duplications",project_key="php-xss"} 0.0
```

effort_to_reach_maintainability_rating_a Effort to Reach Maintainability Rating A
```# HELP effort_to_reach_maintainability_rating_a Effort to Reach Maintainability Rating A
# TYPE effort_to_reach_maintainability_rating_a gauge
effort_to_reach_maintainability_rating_a{domain="Maintainability",project_key="bac"} 0.0
```

false_positive_issues False Positive Issues
```# HELP false_positive_issues False Positive Issues
# TYPE false_positive_issues gauge
false_positive_issues{domain="Issues",project_key="bac"} 4.0
```

files Files
```# HELP files Files
# TYPE files gauge
files{domain="Size",project_key="bac"} 85.0
```

functions Functions
```# HELP functions Functions
# TYPE functions gauge
functions{domain="Size",project_key="bac"} 255.0
```

generated_lines Generated Lines
```# HELP generated_lines Generated Lines
# TYPE generated_lines gauge
```

generated_ncloc Generated Lines of Code
```# HELP generated_ncloc Generated Lines of Code
# TYPE generated_ncloc gauge
```

info_violations Info Issues
```# HELP info_violations Info Issues
# TYPE info_violations gauge
info_violations{domain="Issues",project_key="bac"} 0.0
```

violations Issues
```# HELP violations Issues
# TYPE violations gauge
violations{domain="Issues",project_key="bac"} 199.0
```

line_coverage Line Coverage
```# HELP line_coverage Line Coverage
# TYPE line_coverage gauge
line_coverage{domain="Coverage",project_key="bac"} 0.0
```

new_line_coverage Line Coverage on New Code
```# HELP new_line_coverage Line Coverage on New Code
# TYPE new_line_coverage gauge
new_line_coverage{domain="Coverage",project_key="php-xss"} 0.0
```

lines Lines
```# HELP lines Lines
# TYPE lines gauge
lines{domain="Size",project_key="bac"} 5641.0
```

ncloc Lines of Code
```# HELP ncloc Lines of Code
# TYPE ncloc gauge
ncloc{domain="Size",project_key="bac"} 4383.0
```

lines_to_cover Lines to Cover
```# HELP lines_to_cover Lines to Cover
# TYPE lines_to_cover gauge
lines_to_cover{domain="Coverage",project_key="bac"} 1529.0
```

new_lines_to_cover Lines to Cover on New Code
```# HELP new_lines_to_cover Lines to Cover on New Code
# TYPE new_lines_to_cover gauge
new_lines_to_cover{domain="Coverage",project_key="php-xss"} 1.0
```

sqale_rating Maintainability Rating
```# HELP sqale_rating Maintainability Rating
# TYPE sqale_rating gauge
sqale_rating{domain="Maintainability",project_key="bac"} 1.0
```

new_maintainability_rating Maintainability Rating on New Code
```# HELP new_maintainability_rating Maintainability Rating on New Code
# TYPE new_maintainability_rating gauge
new_maintainability_rating{domain="Maintainability",project_key="php-xss"} 1.0
```

major_violations Major Issues
```# HELP major_violations Major Issues
# TYPE major_violations gauge
major_violations{domain="Issues",project_key="bac"} 54.0
```

minor_violations Minor Issues
```# HELP minor_violations Minor Issues
# TYPE minor_violations gauge
minor_violations{domain="Issues",project_key="bac"} 89.0
```

new_blocker_violations New Blocker Issues
```# HELP new_blocker_violations New Blocker Issues
# TYPE new_blocker_violations gauge
new_blocker_violations{domain="Issues",project_key="php-xss"} 0.0
```

new_bugs New Bugs
```# HELP new_bugs New Bugs
# TYPE new_bugs gauge
new_bugs{domain="Reliability",project_key="php-xss"} 0.0
```

new_code_smells New Code Smells
```# HELP new_code_smells New Code Smells
# TYPE new_code_smells gauge
new_code_smells{domain="Maintainability",project_key="php-xss"} 0.0
```

new_critical_violations New Critical Issues
```# HELP new_critical_violations New Critical Issues
# TYPE new_critical_violations gauge
new_critical_violations{domain="Issues",project_key="php-xss"} 0.0
```

new_info_violations New Info Issues
```# HELP new_info_violations New Info Issues
# TYPE new_info_violations gauge
new_info_violations{domain="Issues",project_key="php-xss"} 0.0
```

new_violations New Issues
```# HELP new_violations New Issues
# TYPE new_violations gauge
new_violations{domain="Issues",project_key="php-xss"} 0.0
```

new_lines New Lines
```# HELP new_lines New Lines
# TYPE new_lines gauge
new_lines{domain="Size",project_key="php-xss"} 1.0
```

new_major_violations New Major Issues
```# HELP new_major_violations New Major Issues
# TYPE new_major_violations gauge
new_major_violations{domain="Issues",project_key="php-xss"} 0.0
```

new_minor_violations New Minor Issues
```# HELP new_minor_violations New Minor Issues
# TYPE new_minor_violations gauge
new_minor_violations{domain="Issues",project_key="php-xss"} 0.0
```

new_security_hotspots New Security Hotspots
```# HELP new_security_hotspots New Security Hotspots
# TYPE new_security_hotspots gauge
new_security_hotspots{domain="SecurityReview",project_key="php-xss"} 1.0
```

new_vulnerabilities New Vulnerabilities
```# HELP new_vulnerabilities New Vulnerabilities
# TYPE new_vulnerabilities gauge
new_vulnerabilities{domain="Security",project_key="php-xss"} 0.0
```

unanalyzed_c Number of unanalyzed c files
```# HELP unanalyzed_c Number of unanalyzed c files
# TYPE unanalyzed_c gauge
```

unanalyzed_cpp Number of unanalyzed c++ files
```# HELP unanalyzed_cpp Number of unanalyzed c++ files
# TYPE unanalyzed_cpp gauge
```

open_issues Open Issues
```# HELP open_issues Open Issues
# TYPE open_issues gauge
open_issues{domain="Issues",project_key="bac"} 198.0
```

projects Project branches
```# HELP projects Project branches
# TYPE projects gauge
```

public_api Public API
```# HELP public_api Public API
# TYPE public_api gauge
```

public_documented_api_density Public Documented API (%)
```# HELP public_documented_api_density Public Documented API (%)
# TYPE public_documented_api_density gauge
```

public_undocumented_api Public Undocumented API
```# HELP public_undocumented_api Public Undocumented API
# TYPE public_undocumented_api gauge
```

alert_status Quality Gate Status
```# HELP alert_status Quality Gate Status
# TYPE alert_status gauge
alert_status{alert_status="ERROR",domain="Releasability",project_key="bac"} 1.0
```

reliability_rating Reliability Rating
```# HELP reliability_rating Reliability Rating
# TYPE reliability_rating gauge
reliability_rating{domain="Reliability",project_key="bac"} 3.0
```

new_reliability_rating Reliability Rating on New Code
```# HELP new_reliability_rating Reliability Rating on New Code
# TYPE new_reliability_rating gauge
new_reliability_rating{domain="Reliability",project_key="php-xss"} 1.0
```

reliability_remediation_effort Reliability Remediation Effort
```# HELP reliability_remediation_effort Reliability Remediation Effort
# TYPE reliability_remediation_effort gauge
reliability_remediation_effort{domain="Reliability",project_key="xss-checker-1"} 2.0
```

new_reliability_remediation_effort Reliability Remediation Effort on New Code
```# HELP new_reliability_remediation_effort Reliability Remediation Effort on New Code
# TYPE new_reliability_remediation_effort gauge
new_reliability_remediation_effort{domain="Reliability",project_key="php-xss"} 0.0
```

reopened_issues Reopened Issues
```# HELP reopened_issues Reopened Issues
# TYPE reopened_issues gauge
reopened_issues{domain="Issues",project_key="bac"} 0.0
```

security_hotspots Security Hotspots
```# HELP security_hotspots Security Hotspots
# TYPE security_hotspots gauge
security_hotspots{domain="SecurityReview",project_key="bac"} 6.0
```

security_hotspots_reviewed Security Hotspots Reviewed
```# HELP security_hotspots_reviewed Security Hotspots Reviewed
# TYPE security_hotspots_reviewed gauge
security_hotspots_reviewed{domain="SecurityReview",project_key="bac"} 0.0
```

new_security_hotspots_reviewed Security Hotspots Reviewed on New Code
```# HELP new_security_hotspots_reviewed Security Hotspots Reviewed on New Code
# TYPE new_security_hotspots_reviewed gauge
new_security_hotspots_reviewed{domain="SecurityReview",project_key="php-xss"} 0.0
```

security_rating Security Rating
```# HELP security_rating Security Rating
# TYPE security_rating gauge
security_rating{domain="Security",project_key="bac"} 4.0
```

new_security_rating Security Rating on New Code
```# HELP new_security_rating Security Rating on New Code
# TYPE new_security_rating gauge
new_security_rating{domain="Security",project_key="php-xss"} 1.0
```

security_remediation_effort Security Remediation Effort
```# HELP security_remediation_effort Security Remediation Effort
# TYPE security_remediation_effort gauge
security_remediation_effort{domain="Security",project_key="bac"} 17.0
```

new_security_remediation_effort Security Remediation Effort on New Code
```# HELP new_security_remediation_effort Security Remediation Effort on New Code
# TYPE new_security_remediation_effort gauge
new_security_remediation_effort{domain="Security",project_key="php-xss"} 0.0
```

security_review_rating Security Review Rating
```# HELP security_review_rating Security Review Rating
# TYPE security_review_rating gauge
security_review_rating{domain="SecurityReview",project_key="bac"} 5.0
```

new_security_review_rating Security Review Rating on New Code
```# HELP new_security_review_rating Security Review Rating on New Code
# TYPE new_security_review_rating gauge
new_security_review_rating{domain="SecurityReview",project_key="php-xss"} 5.0
```

security_hotspots_reviewed_status Security Review Reviewed Status
```# HELP security_hotspots_reviewed_status Security Review Reviewed Status
# TYPE security_hotspots_reviewed_status gauge
security_hotspots_reviewed_status{domain="SecurityReview",project_key="bac"} 0.0
```

new_security_hotspots_reviewed_status Security Review Reviewed Status on New Code
```# HELP new_security_hotspots_reviewed_status Security Review Reviewed Status on New Code
# TYPE new_security_hotspots_reviewed_status gauge
new_security_hotspots_reviewed_status{domain="SecurityReview",project_key="php-xss"} 0.0
```

security_hotspots_to_review_status Security Review To Review Status
```# HELP security_hotspots_to_review_status Security Review To Review Status
# TYPE security_hotspots_to_review_status gauge
security_hotspots_to_review_status{domain="SecurityReview",project_key="bac"} 6.0
```

new_security_hotspots_to_review_status Security Review To Review Status on New Code
```# HELP new_security_hotspots_to_review_status Security Review To Review Status on New Code
# TYPE new_security_hotspots_to_review_status gauge
new_security_hotspots_to_review_status{domain="SecurityReview",project_key="php-xss"} 1.0
```

skipped_tests Skipped Unit Tests
```# HELP skipped_tests Skipped Unit Tests
# TYPE skipped_tests gauge
skipped_tests{domain="Coverage",project_key="unittest"} 3.0
```

statements Statements
```# HELP statements Statements
# TYPE statements gauge
statements{domain="Size",project_key="bac"} 1247.0
```

sqale_index Technical Debt
```# HELP sqale_index Technical Debt
# TYPE sqale_index gauge
sqale_index{domain="Maintainability",project_key="bac"} 990.0
```

sqale_debt_ratio Technical Debt Ratio
```# HELP sqale_debt_ratio Technical Debt Ratio
# TYPE sqale_debt_ratio gauge
sqale_debt_ratio{domain="Maintainability",project_key="bac"} 0.8
```

new_sqale_debt_ratio Technical Debt Ratio on New Code
```# HELP new_sqale_debt_ratio Technical Debt Ratio on New Code
# TYPE new_sqale_debt_ratio gauge
new_sqale_debt_ratio{domain="Maintainability",project_key="php-xss"} 0.0
```

uncovered_conditions Uncovered Conditions
```# HELP uncovered_conditions Uncovered Conditions
# TYPE uncovered_conditions gauge
```

new_uncovered_conditions Uncovered Conditions on New Code
```# HELP new_uncovered_conditions Uncovered Conditions on New Code
# TYPE new_uncovered_conditions gauge
new_uncovered_conditions{domain="Coverage",project_key="php-xss"} 0.0
```

uncovered_lines Uncovered Lines
```# HELP uncovered_lines Uncovered Lines
# TYPE uncovered_lines gauge
uncovered_lines{domain="Coverage",project_key="bac"} 1529.0
```

new_uncovered_lines Uncovered Lines on New Code
```# HELP new_uncovered_lines Uncovered Lines on New Code
# TYPE new_uncovered_lines gauge
new_uncovered_lines{domain="Coverage",project_key="php-xss"} 1.0
```

test_execution_time Unit Test Duration
```# HELP test_execution_time Unit Test Duration
# TYPE test_execution_time gauge
test_execution_time{domain="Coverage",project_key="unittest"} 2.0
```

test_errors Unit Test Errors
```# HELP test_errors Unit Test Errors
# TYPE test_errors gauge
test_errors{domain="Coverage",project_key="unittest"} 0.0
```

test_failures Unit Test Failures
```# HELP test_failures Unit Test Failures
# TYPE test_failures gauge
test_failures{domain="Coverage",project_key="unittest"} 0.0
```

tests Unit Tests
```# HELP tests Unit Tests
# TYPE tests gauge
tests{domain="Coverage",project_key="unittest"} 4.0
```

test_success_density Unit Test Success (%)
```# HELP test_success_density Unit Test Success (%)
# TYPE test_success_density gauge
test_success_density{domain="Coverage",project_key="unittest"} 100.0
```

vulnerabilities Vulnerabilities
```# HELP vulnerabilities Vulnerabilities
# TYPE vulnerabilities gauge
vulnerabilities{domain="Security",project_key="bac"} 4.0
```

wont_fix_issues Won't Fix Issues
```# HELP wont_fix_issues Won't Fix Issues
# TYPE wont_fix_issues gauge
wont_fix_issues{domain="Issues",project_key="bac"} 3.0
```




# Use

## Build & test

To build and test the project locally simply run the following commands.

```bash
$ make
$ make test
```

## Run

A [docker-compose](https://docs.docker.com/compose/) configuration is included in this repository to make getting started with the project as simple as possible. To use it, follow the following steps.

### Define your environment

Using the sample environment as a base, 

```bash
$ cp config/sample.env config/production.env
$ vim config/production.env
```

### Run with `docker compose`

To run with your newly configured environment, execute the following.

```bash
$ PDK_ENV=$(pwd)/config/production.env PDK_PROJECTS_CONFIG=$(pwd)/config/projects.json ./compose-ctl up
```

### Viewing metrics with Grafana

By default, a grafana instance preloaded with templated dashboards will be started. Use your browser to view [http://localhost:3000](http://localhost:3000). The default username is `admin` and default password is `admin`. The dasboards are then accessible under the 'Home' tab.

### Templated Grafana dashboards

The files under `dashboards/*.json` contain a grafana dashboards described below.

#### `Sonarqube Exporter` dashboard

The `Sonarqube Exporter` dashboard presents all metrics in detail and is meant for finer-grained analytics. See an image of the dasboard with data below.

![overview!](https://github.com/return200-ok/sonarqube_prometheus_exporter/blob/main/assets/sonarqube_exporter.png?raw=true)


# Contribute!

If you want to contribute to the project, do it

# Copyright

GNU General Public License v3.0
