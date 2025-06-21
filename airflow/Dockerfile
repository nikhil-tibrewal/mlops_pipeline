FROM apache/airflow:2.7.3-python3.9

# Apache Airflow Docker image enforces running as the airflow user, not root, for security reasons.
USER airflow

# Install your Python dependencies as the airflow user.
RUN pip install --no-cache-dir scikit-learn mlflow

# Switch back to root to copy and run entrypoint
USER root

# Copy and set permissions on the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint to fix permissions and then run CMD
ENTRYPOINT ["/entrypoint.sh"]

# Restore user so CMD runs as airflow
USER airflow
