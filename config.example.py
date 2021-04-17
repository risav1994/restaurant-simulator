broker_url = "redis://:password@localhost:6379/0"
result_backend = "redis://:password@localhost:6379/0"
task_serializer = 'pickle'
result_serializer = 'pickle'
accept_content = ['pickle']
result_expires = 300
worker_concurrency = 10
worker_prefetch_multiplier = 1
