import os

os.system('python src/data_ingestion.py')#used to execute end point of the pipeline
print('Data Ingestion Completed')
os.system('python src/data_preprocessing.py')#used to execute end point of the pipeline
print('Data Preprocessing Completed')
os.system('python src/feature_engineering.py')#used to execute end point of the pipeline
print('Feature Engineering Completed')
os.system('python src/model_building.py')#used to execute end point of the pipeline
print('Model Building Completed')
os.system('python src/model_evaluation.py')#used to execute end point of the pipeline
print('Model Evaluation Completed')