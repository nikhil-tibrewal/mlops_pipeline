from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
}

dag = DAG(
    "mlops_pipeline",
    default_args=default_args,
    description="Train and deploy sklearn model",
    schedule_interval=None,
    catchup=False,
)

def train_model():
    subprocess.run(["python3", "/app/models/train_model.py"], check=True)

def deploy_model():
    import os
    import mlflow
    from mlflow.tracking import MlflowClient

    client = MlflowClient()
    latest_run = client.search_runs(
        experiment_ids=["0"], order_by=["start_time DESC"], max_results=1
    )[0]
    run_id = latest_run.info.run_id

    os.system(f"mlflow models serve -m runs:/{run_id}/model -p 5001 --no-conda &")

train_task = PythonOperator(
    task_id="train_model",
    python_callable=train_model,
    dag=dag,
)

deploy_task = PythonOperator(
    task_id="deploy_model",
    python_callable=deploy_model,
    dag=dag,
)

train_task >> deploy_task