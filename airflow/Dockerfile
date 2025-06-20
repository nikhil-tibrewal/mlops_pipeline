FROM apache/airflow:2.7.3-python3.9

USER root
RUN pip install --no-cache-dir scikit-learn mlflow

COPY ./models /opt/airflow/models