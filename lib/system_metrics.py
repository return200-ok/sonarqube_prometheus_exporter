from lib.util import convert, get_data, get_json
from prometheus_client import Gauge, Info

# Defining the metrics that will be used in the script.

health_metric = Info('health_check', 'Server health check')
web_jvm_max_memory_metric = Gauge('web_jvm_max_memory', 'Web JVM Max Memory (MB)')
web_jvm_free_memory_metric = Gauge('web_jvm_free_memory', 'Web JVM Free Memory (MB)')
web_jvm_heap_commited_metric = Gauge('web_jvm_heap_commited', 'Web JVM Heap Committed (MB)')
web_jvm_heap_init_metric = Gauge('web_jvm_heap_init', 'Web JVM Heap Init (MB)')
web_jvm_heap_max_metric = Gauge('web_jvm_heap_max', 'Web JVM Heap Max (MB)')
web_jvm_heap_used_metric = Gauge('web_jvm_heap_used', 'Web JVM Heap Used (MB)')
web_jvm_non_heap_committed_metric = Gauge('web_jvm_non_heap_committed', 'Web JVM Non Heap Committed (MB)')
web_jvm_non_heap_init_metric = Gauge('web_jvm_non_heap_init', 'Web JVM Non Heap Init (MB))')
web_jvm_non_heap_used_metric = Gauge('web_jvm_non_heap_used', 'Web JVM Non Heap Used (MB)')
web_jvm_threads_metric = Gauge('web_jvm_threads', 'Web JVM Threads')
web_pool_active_connection_metric = Gauge('web_pool_active_connection', 'Web Pool Active Connections')
web_pool_max_connection_metric = Gauge('web_pool_max_connection', 'Web Pool Max Connections')
web_pool_initial_size_metric = Gauge('web_pool_initial_size', 'Web Pool Initial Size')
web_pool_idle_connections_metric = Gauge('web_pool_idle_connections', 'Web Pool Idle Connections')
web_pool_min_idle_connections_metric = Gauge('web_pool_min_idle_connections', 'Web Pool Min Idle Connections')
web_pool_max_idle_connections_metric = Gauge('web_pool_max_idle_connections', 'Web Pool Max Idle Connections')
compute_engine_tasks_pending_metric = Gauge('compute_engine_tasks_pending', 'Compute Engine Tasks Pending')
compute_engine_tasks_inprogress_metric = Gauge('compute_engine_tasks_inprogress', 'Compute Engine Tasks In Progress')
compute_engine_tasks_error_progress_metric = Gauge('compute_engine_tasks_error_progress', 'Compute Engine Tasks Processed With Error')
compute_engine_tasks_success_progress_metric = Gauge('compute_engine_tasks_success_progress', 'Compute Engine Tasks Processed With Success')
compute_engine_tasks_progressing_time_metric = Gauge('compute_engine_tasks_progressing_time', 'Compute Engine Tasks Processing Time (ms)')
compute_engine_tasks_worker_metric = Gauge('compute_engine_tasks_worker', 'Compute Engine Tasks Worker Count')
compute_engine_jvm_state_max_memory_metric = Gauge('compute_engine_jvm_state_max_memory', 'Compute Engine Tasks Worker Count')
compute_engine_jvm_free_memory_metric = Gauge('compute_engine_jvm_free_memory', 'Compute Engine JVM Free Memory (MB)')
compute_engine_jvm_heap_commited_metric = Gauge('compute_engine_jvm_heap_commited', 'Compute Engine JVM Heap Committed (MB)')
compute_engine_jvm_heap_init_metric = Gauge('compute_engine_jvm_heap_init', 'Compute Engine JVM Heap Init (MB)')
compute_engine_jvm_heap_max_metric = Gauge('compute_engine_jvm_heap_max', 'Compute Engine JVM Heap Max (MB)')
compute_engine_jvm_heap_used_metric = Gauge('compute_engine_jvm_heap_used', 'Compute Engine JVM Heap Used (MB)')
compute_engine_jvm_non_heap_committed_metric = Gauge('compute_engine_jvm_non_heap_committed', 'Compute Engine JVM Non Heap Committed (MB)')
compute_engine_jvm_non_heap_init_metric = Gauge('compute_engine_jvm_non_heap_init', 'Compute Engine JVM Non Heap Init (MB))')
compute_engine_jvm_non_heap_used_metric = Gauge('compute_engine_jvm_non_heap_used', 'Compute Engine JVM Non Heap Used (MB)')
compute_engine_jvm_threads_metric = Gauge('compute_engine_jvm_threads', 'Compute Engine JVM Threads')
compute_engine_pool_active_connection_metric = Gauge('compute_engine_pool_active_connection', 'Compute Engine Pool Active Connections')
compute_engine_pool_max_connection_metric = Gauge('compute_engine_pool_max_connection', 'Compute Engine Pool Max Connections')
compute_engine_pool_initial_size_metric = Gauge('compute_engine_pool_initial_size', 'Compute Engine Pool Initial Size')
compute_engine_pool_idle_connections_metric = Gauge('compute_engine_pool_idle_connections', 'Compute Engine Pool Idle Connections')
compute_engine_pool_min_idle_connections_metric = Gauge('compute_engine_pool_min_idle_connections', 'Compute Engine Pool Min Idle Connections')
compute_engine_pool_max_idle_connections_metric = Gauge('compute_engine_pool_max_idle_connections', 'Compute Engine Pool Max Idle Connections')
cpu_usage_metric = Gauge('cpu_usage', 'CPU Usage (%)')
disk_available_metric = Gauge('disk_available', 'Disk Available')
store_size_metric = Gauge('store_size', 'Store Size')
translog_size_metric = Gauge('translog_size', 'Translog Size')
jvm_heap_used_metric = Gauge('jvm_heap_used', 'JVM Heap Used')
jvm_heap_max_metric = Gauge('jvm_heap_max', 'JVM Heap Max')
jvm_non_heap_used_metric = Gauge('jvm_non_heap_used', 'JVM Non Heap Used')
jvm_threads_metric = Gauge('jvm_threads', 'JVM Threads')
open_file_descriptors_metric = Gauge('open_file_descriptors', 'Open File Descriptors')
max_file_descriptors_metric = Gauge('max_file_descriptors', 'Max File Descriptors')
index_docs_metric = Gauge('index_docs', 'Index components - Docs')
sonarlint_client_metric = Gauge('sonarlint_client', 'SonarLint Connected Clients')
total_of_user_metric = Gauge('total_of_user', 'Total of user')
total_of_project_metric = Gauge('total_of_project', 'Total of project')
total_line_of_code_metric = Gauge('total_line_of_code', 'Total line of code')
total_of_plugins_metric = Gauge('total_of_plugins', 'Total of plugins')
project_count_by_language_metric = Gauge('project_count_by_language', 'Project count by language', ['language'])
ncloc_count_by_language_metric = Gauge('ncloc_count_by_language', 'Line of code count by language', ['language'])


def system_metric(sonarqube_server, sonarqube_token):
  # Getting the data from the sonarqube server and then it is getting the health of the server.
  url = sonarqube_server+"/api/system/info"
  data = get_data(url, sonarqube_token)

  health = get_json('Health', data)
  health_info = {'health': health}
  health_metric.info(health_info)

# Web JVM State
  web_jvm_state = get_json('Web JVM State', data)
  web_jvm_max_memory = get_json('Max Memory (MB)', web_jvm_state)
  web_jvm_max_memory_metric.set(web_jvm_max_memory)

  web_jvm_free_memory = get_json('Free Memory (MB)', web_jvm_state)
  web_jvm_free_memory_metric.set(web_jvm_free_memory)

  web_jvm_heap_commited = get_json('Heap Committed (MB)', web_jvm_state)
  web_jvm_heap_commited_metric.set(web_jvm_heap_commited)

  web_jvm_heap_init = get_json('Heap Init (MB)', web_jvm_state)
  web_jvm_heap_init_metric.set(web_jvm_heap_init)

  web_jvm_heap_max = get_json('Heap Max (MB)', web_jvm_state)
  web_jvm_heap_max_metric.set(web_jvm_heap_max)

  web_jvm_heap_used = get_json('Heap Used (MB)', web_jvm_state)
  web_jvm_heap_used_metric.set(web_jvm_heap_used)

  web_jvm_non_heap_committed = get_json('Non Heap Committed (MB)', web_jvm_state)
  web_jvm_non_heap_committed_metric.set(web_jvm_non_heap_committed)

  web_jvm_non_heap_init = get_json('Non Heap Init (MB)', web_jvm_state)
  web_jvm_non_heap_init_metric.set(web_jvm_non_heap_init)

  web_jvm_non_heap_used = get_json('Non Heap Used (MB)', web_jvm_state)
  web_jvm_non_heap_used_metric.set(web_jvm_non_heap_used)

  web_jvm_threads = get_json('Threads', web_jvm_state)
  web_jvm_threads_metric.set(web_jvm_threads)

# Web Database Connection
  web_database_connection = get_json('Web Database Connection', data)
  web_pool_active_connection = get_json('Pool Active Connections', web_database_connection)
  web_pool_active_connection_metric.set(web_pool_active_connection)

  web_pool_max_connection = get_json('Pool Max Connections', web_database_connection)
  web_pool_max_connection_metric.set(web_pool_max_connection)

  web_pool_initial_size = get_json('Pool Initial Size', web_database_connection)
  web_pool_initial_size_metric.set(web_pool_initial_size)

  web_pool_idle_connections = get_json('Pool Idle Connections', web_database_connection)
  web_pool_idle_connections_metric.set(web_pool_idle_connections)

  web_pool_min_idle_connections = get_json('Pool Min Idle Connections', web_database_connection)
  web_pool_min_idle_connections_metric.set(web_pool_min_idle_connections)

  web_pool_max_idle_connections = get_json('Pool Max Idle Connections', web_database_connection)
  web_pool_max_idle_connections_metric.set(web_pool_max_idle_connections)


# Compute Engine Tasks
  compute_engine_tasks = get_json('Compute Engine Tasks', data)
  compute_engine_tasks_pending = get_json('Pending', compute_engine_tasks)
  compute_engine_tasks_pending_metric.set(compute_engine_tasks_pending)

  compute_engine_tasks_inprogress = get_json('In Progress', compute_engine_tasks)
  compute_engine_tasks_inprogress_metric.set(compute_engine_tasks_inprogress)

  compute_engine_tasks_error_progress = get_json('Processed With Error', compute_engine_tasks)
  compute_engine_tasks_error_progress_metric.set(compute_engine_tasks_error_progress)

  compute_engine_tasks_success_progress = get_json('Processed With Success', compute_engine_tasks)
  compute_engine_tasks_success_progress_metric.set(compute_engine_tasks_success_progress)

  compute_engine_tasks_progressing_time = get_json('Processing Time (ms)', compute_engine_tasks)
  compute_engine_tasks_progressing_time_metric.set(compute_engine_tasks_progressing_time)

  compute_engine_tasks_worker = get_json('Worker Count', compute_engine_tasks)
  compute_engine_tasks_worker_metric.set(compute_engine_tasks_worker)  

# Compute Engine JVM State
  compute_engine_jvm_state = get_json('Compute Engine JVM State', data)
  compute_engine_jvm_state_max_memory = get_json('Worker Count', compute_engine_jvm_state)
  compute_engine_jvm_state_max_memory_metric.set(compute_engine_jvm_state_max_memory)  

  compute_engine_jvm_free_memory = get_json('Free Memory (MB)', compute_engine_jvm_state)
  compute_engine_jvm_free_memory_metric.set(compute_engine_jvm_free_memory)

  compute_engine_jvm_heap_commited = get_json('Heap Committed (MB)', compute_engine_jvm_state)
  compute_engine_jvm_heap_commited_metric.set(compute_engine_jvm_heap_commited)

  compute_engine_jvm_heap_init = get_json('Heap Init (MB)', compute_engine_jvm_state)
  compute_engine_jvm_heap_init_metric.set(compute_engine_jvm_heap_init)

  compute_engine_jvm_heap_max = get_json('Heap Max (MB)', compute_engine_jvm_state)
  compute_engine_jvm_heap_max_metric.set(compute_engine_jvm_heap_max)

  compute_engine_jvm_heap_used = get_json('Heap Used (MB)', compute_engine_jvm_state)
  compute_engine_jvm_heap_used_metric.set(compute_engine_jvm_heap_used)

  compute_engine_jvm_non_heap_committed = get_json('Non Heap Committed (MB)', compute_engine_jvm_state)
  compute_engine_jvm_non_heap_committed_metric.set(compute_engine_jvm_non_heap_committed)

  compute_engine_jvm_non_heap_init = get_json('Non Heap Init (MB)', compute_engine_jvm_state)
  compute_engine_jvm_non_heap_init_metric.set(compute_engine_jvm_non_heap_init)

  compute_engine_jvm_non_heap_used = get_json('Non Heap Used (MB)', compute_engine_jvm_state)
  compute_engine_jvm_non_heap_used_metric.set(compute_engine_jvm_non_heap_used)

  compute_engine_jvm_threads = get_json('Threads', compute_engine_jvm_state)
  compute_engine_jvm_threads_metric.set(compute_engine_jvm_threads)

# Compute Engine Database Connection
  compute_engine_database_connection = get_json('Compute Engine Database Connection', data)
  compute_engine_pool_active_connection = get_json('Pool Active Connections', compute_engine_database_connection)
  compute_engine_pool_active_connection_metric.set(compute_engine_pool_active_connection)

  compute_engine_pool_max_connection = get_json('Pool Max Connections', compute_engine_database_connection)
  compute_engine_pool_max_connection_metric.set(compute_engine_pool_max_connection)

  compute_engine_pool_initial_size = get_json('Pool Initial Size', compute_engine_database_connection)
  compute_engine_pool_initial_size_metric.set(compute_engine_pool_initial_size)

  compute_engine_pool_idle_connections = get_json('Pool Idle Connections', compute_engine_database_connection)
  compute_engine_pool_idle_connections_metric.set(compute_engine_pool_idle_connections)

  compute_engine_pool_min_idle_connections = get_json('Pool Min Idle Connections', compute_engine_database_connection)
  compute_engine_pool_min_idle_connections_metric.set(compute_engine_pool_min_idle_connections)

  compute_engine_pool_max_idle_connections = get_json('Pool Max Idle Connections', compute_engine_database_connection)
  compute_engine_pool_max_idle_connections_metric.set(compute_engine_pool_max_idle_connections)

# Search State
  search_state = get_json('Search State', data)
  cpu_usage = get_json('CPU Usage (%)', search_state)
  cpu_usage_metric.set(cpu_usage)

  disk_available = get_json('Disk Available', search_state)
  disk_available_metric.set(convert(disk_available))

  store_size = get_json('Store Size', search_state)
  store_size_metric.set(convert(store_size))

  translog_size = get_json('Translog Size', search_state)
  translog_size_metric.set(convert(translog_size))

  jvm_heap_used = get_json('JVM Heap Used', search_state)
  jvm_heap_used_metric.set(convert(jvm_heap_used))

  jvm_heap_max = get_json('JVM Heap Max', search_state)
  jvm_heap_max_metric.set(convert(jvm_heap_max))

  jvm_non_heap_used = get_json('JVM Non Heap Used', search_state)
  jvm_non_heap_used_metric.set(convert(jvm_non_heap_used))

  jvm_threads = get_json('JVM Threads', search_state)
  jvm_threads_metric.set(jvm_threads)

  open_file_descriptors = get_json('Open File Descriptors', search_state)
  open_file_descriptors_metric.set(open_file_descriptors)

  max_file_descriptors = get_json('Max File Descriptors', search_state)
  max_file_descriptors_metric.set(max_file_descriptors)

# Search Indexes
  search_indexes = get_json('Search Indexes', data)
  index_docs = get_json('Index components - Docs', search_indexes)
  index_docs_metric.set(index_docs)

# Server Push Connections
  server_push_connections = get_json('Server Push Connections', data)
  sonarlint_client = get_json('SonarLint Connected Clients', server_push_connections)
  sonarlint_client_metric.set(sonarlint_client)

# Statistics
  statistics = get_json('Statistics', data)
  total_of_user = get_json('userCount', statistics)
  total_of_user_metric.set(total_of_user)

  total_of_project = get_json('projectCount', statistics)
  total_of_project_metric.set(total_of_project)

  total_line_of_code = get_json('ncloc', statistics)
  total_line_of_code_metric.set(total_line_of_code)

  total_of_plugins = get_json('plugins', statistics)
  total_of_plugins_metric.set(len(total_of_plugins))

  project_count_by_language = get_json('projectCountByLanguage', statistics)
  for c in project_count_by_language:
    project_count_by_language_metric.labels(language=c['language']).set(c['count'])

  ncloc_count_by_language = get_json('nclocByLanguage', statistics)
  for c in ncloc_count_by_language:
    ncloc_count_by_language_metric.labels(language=c['language']).set(c['ncloc'])
