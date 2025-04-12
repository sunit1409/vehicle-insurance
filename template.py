import os 
from pathlib import Path

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py", 
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/model_registry.py",
    f"{project_name}/components/model_deployment.py",
    f"{project_name}/components/monitoring.py", 
    f"{project_name}/components/visualization.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py", 
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proji_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py", 
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py", 
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/pipeline/model_evaluation_pipeline.py",
    f"{project_name}/pipeline/model_deployment_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",

]

for filepath in list_of_files:
    # Ensure the directory exists
    directory = os.path.dirname(filepath)
    if directory:  # Check if the file has a directory path
        os.makedirs(directory, exist_ok=True)
    
    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # Create an empty file