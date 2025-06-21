import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def run_training():
    # Load dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Train model
    clf = RandomForestClassifier(n_estimators=100, max_depth=3)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)

    # Evaluate
    acc = accuracy_score(y_test, preds)
    print(f"Accuracy: {acc}")

    # Ensure default experiment exists
    if not mlflow.get_experiment_by_name("default"):
        mlflow.create_experiment("default")
    mlflow.set_experiment("default")

    # Log to MLflow
    with mlflow.start_run() as run:
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 3)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(clf, artifact_path="model")
        print(f"Model logged with run_id: {run.info.run_id}")
        return run.info.run_id

# Allow manual run
if __name__ == "__main__":
    run_training()