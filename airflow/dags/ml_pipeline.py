from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging
from models import train_model, serve_model

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
}

dag = DAG(
    "mlops_pipeline",
    default_args=default_args,
    description="Train and serve model using MLflow",
    schedule_interval=None,
    catchup=False,
)

train_task = PythonOperator(
    task_id="train_model",
    python_callable=train_model.run_training,
    dag=dag,
)

deploy_task = PythonOperator(
    task_id="deploy_model",
    python_callable=serve_model.run_serve,
    dag=dag,
)

train_task >> deploy_task
