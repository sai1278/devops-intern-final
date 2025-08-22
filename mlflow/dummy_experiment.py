import mlflow

mlflow.set_experiment("devops-final-demo")

with mlflow.start_run():
    mlflow.log_param("param1", 42)
    mlflow.log_metric("accuracy", 0.95)
    print("Dummy MLflow experiment logged.")
