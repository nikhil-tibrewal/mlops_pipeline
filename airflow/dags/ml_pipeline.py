# Inside the Docker container, tell Python where the models/ folder is because it’s not in the PYTHONPATH
import sys
sys.path.append('/opt/airflow/models')

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging
from train_model import run_training

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
}

dag = DAG(
    "mlops_pipeline",
    default_args=default_args,
    description="Train model using MLflow",
    schedule_interval=None,
    catchup=False,
)

train_task = PythonOperator(
    task_id="train_model",
    python_callable=run_training,
    dag=dag,
)

train_task
