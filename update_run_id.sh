#!/bin/bash

set -e

# Path to .env file
ENV_FILE=".env"

# Step 1: Extract FERNET_KEY (if exists)
FERNET_KEY=$(grep '^FERNET_KEY=' "$ENV_FILE" | cut -d '=' -f2-)

# Step 2: Get experiment_id for "default"
EXPERIMENT_ID=$(curl -s http://localhost:5000/api/2.0/mlflow/experiments/search \
  -X POST -H "Content-Type: application/json" -d '{"max_results": 10}' \
  | jq -r '.experiments[] | select(.name=="default") | .experiment_id')

# Step 3: Get latest run_id from that experiment
RUN_ID=$(curl -s http://localhost:5000/api/2.0/mlflow/runs/search \
  -X POST -H "Content-Type: application/json" \
  -d "{\"experiment_ids\": [\"$EXPERIMENT_ID\"], \"max_results\": 1, \"order_by\": [\"start_time DESC\"]}" \
  | jq -r '.runs[0].info.run_id')

# Step 4: Overwrite .env with updated variables
echo "FERNET_KEY=$FERNET_KEY" > "$ENV_FILE"
echo "MODEL_RUN_ID=$RUN_ID" >> "$ENV_FILE"

echo "✅ Updated .env with latest run ID: $RUN_ID"