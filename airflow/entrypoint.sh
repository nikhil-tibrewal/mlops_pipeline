#!/bin/bash
set -e

# Fix permissions so airflow user can write to /opt/airflow/mlruns
chown -R airflow:root /opt/airflow/mlruns

# Continue with the original CMD
exec "$@"