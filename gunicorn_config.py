# gunicorn_config.py
import multiprocessing

# Timeout plus long pour éviter les worker timeout
timeout = 120  # 2 minutes au lieu de 30 secondes par défaut

# Nombre de workers
workers = multiprocessing.cpu_count() * 2 + 1

# Type de worker
worker_class = 'sync'

# Logs
loglevel = 'info'
accesslog = '-'
errorlog = '-'

# Keep alive
keepalive = 5

# Maximum de requêtes avant de redémarrer un worker
max_requests = 1000
max_requests_jitter = 50