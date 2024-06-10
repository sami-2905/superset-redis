#!/bin/bash
# Start Redis in the background
#redis-server --daemonize yes

# Upgrade the database schema to the latest version
superset db upgrade

# Initialize Superset (roles, permissions)
superset init

# Execute the CMD from the Dockerfile, e.g., start Superset
exec "$@"

