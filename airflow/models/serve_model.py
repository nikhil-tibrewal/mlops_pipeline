import os
import mlflow
import subprocess
from mlflow.tracking import MlflowClient

def run_serve():
    """
    This function connects to the MLflow tracking server,
    fetches the latest logged model from experiment 0,
    and serves it as a REST API using mlflow.models.serve.
    """
    # Initialize the MLflow client
    client = MlflowClient()

    # Search for the latest run from the default experiment
    experiment = client.get_experiment_by_name("default")
    if experiment is None:
        raise Exception("Experiment 'default' not found.")
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
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

    # Use Popen to persist the server beyond Airflow’s Python process
    proc = subprocess.Popen(
        ["mlflow", "models", "serve", "-m", model_uri, "-p", port, "--no-conda"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = proc.communicate(timeout=10)
    print("STDOUT:", stdout.decode())
    print("STDERR:", stderr.decode())
