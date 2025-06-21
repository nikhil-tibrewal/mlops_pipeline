#!/bin/bash

# Fetch latest run ID from MLflow
RUN_ID=$(docker compose exec airflow-webserver mlflow runs list --experiment-id 0 --order-by start_time DESC --max-results 1 | awk 'NR==2 {print $1}')

# Path to .env file
ENV_FILE=".env"

# Preserve all existing lines except LATEST_RUN_ID, and add the new one
if [ -f "$ENV_FILE" ]; then
    # Remove old LATEST_RUN_ID if exists
    grep -v '^LATEST_RUN_ID=' "$ENV_FILE" > "$ENV_FILE.tmp"
else
    touch "$ENV_FILE.tmp"
fi

# Append new LATEST_RUN_ID
echo "LATEST_RUN_ID=$RUN_ID" >> "$ENV_FILE.tmp"

# Replace .env with updated version
mv "$ENV_FILE.tmp" "$ENV_FILE"

echo "✅ .env updated with LATEST_RUN_ID=$RUN_ID"