import os
import warnings
from flask_appbuilder.security.manager import AUTH_DB

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:$9Mf859#@database-1.c9cs4cuaglbl.us-east-1.rds.amazonaws.com:5432/supersetdb'

WTF_CSRF_ENABLED = True
FEATURE_FLAGS = {
    "DASHBOARD_NATIVE_FILTERS": True,
    "ALERT_REPORTS": True,  # Enable ALERT_REPORTS feature flag
}
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://myredis:6379/0',  # Assuming Redis is hosted at hostname 'myredis'
}
LOG_LEVEL = 'DEBUG'
AUTH_TYPE = AUTH_DB
ENABLE_PROXY_FIX = True

RATELIMIT_STORAGE_URL = 'redis://myredis:6379/3'  # Use Redis for rate limiting

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module='flask_limiter.extension')
warnings.filterwarnings("ignore", category=UserWarning, module='werkzeug.local')

