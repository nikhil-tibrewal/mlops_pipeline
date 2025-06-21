FROM apache/airflow:2.7.3-python3.9

# Apache Airflow Docker image enforces running as the airflow user, not root, for security reasons.
USER airflow

# Install your Python dependencies as the airflow user.
RUN pip install --no-cache-dir scikit-learn mlflow
