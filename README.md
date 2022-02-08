# airflow-poc

## Run multiple models in parallel in airflow

I have used Apache Airflow an open-source tool for orchestrating workflow to compare different models. Apache airflow makes your workflow simple, well organized, and more systematic which can be easily authored, and schedules based on the requirement.

## Comparing multiple models
I will be using a cloud composer (a GCP based managed services) to create an airflow environment. We can also create a local environment. As soon as you create a cloud composer, it creates a bucket in your cloud storage automatically which is eventually mounted with your composer environment. Similarly, you will have the same directory structure when you install on your local environment. In the DAG folder, you need to upload all your python script or DAG which will get rendered into the airflow server and show in the UI, and then you can trigger it manually or if scheduled, it will trigger automatically.

## Below is the DAG created in Google composer
DAG explaining the basic flow of the pipeline
