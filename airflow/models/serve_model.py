import os
import mlflow
from mlflow.tracking import MlflowClient

def run_serve():
    """
    This function connects to the MLflow tracking server,
    fetches the latest logged model from experiment 0,
    and serves it as a REST API using mlflow.models.serve.
    """
    # Initialize the MLflow client
    client = MlflowClient()

    # Search for the latest run from the default experiment (ID 0)
    runs = client.search_runs(
        experiment_ids=["0"],
        order_by=["start_time DESC"],
        max_results=1
    )

    if not runs:
        raise Exception("No MLflow runs found to serve a model.")

    # Extract latest run ID
    run_id = runs[0].info.run_id
    model_uri = f"runs:/{run_id}/model"

    # Serve the model on specified port (default: 5001)
    port = os.getenv("MODEL_PORT", "5001")
    print(f"Serving model from {model_uri} on port {port}...")

    # Launch model serving (non-blocking)
    os.system(f"mlflow models serve -m {model_uri} -p {port} --no-conda &")
