from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'compare-ml-modelstest',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:


    download_data = PythonOperator(
        task_id = 'load_data',
        python_callable=load_data
    )
    run_lr_model = PythonOperator(
        task_id = 'Logistic_Regression_Model',
        python_callable=lr_model
    )
    run_rf_model= PythonOperator(
        task_id = 'Random_Forest_Model',
        python_callable=rf_model
    )
    run_svm_model=PythonOperator(
        task_id = 'Support_Vector_Machine_Model',
        python_callable=svm_model
    )
    compare_models = PythonOperator(
        task_id = 'compare_models',
        python_callable=compare_model
    )

    download_data >> [run_lr_model,run_rf_model,run_svm_model] >> compare_models
