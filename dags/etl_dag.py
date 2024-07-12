from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
import logging 

import os 

logger = logging.getLogger("airflow.task")
path = os.environ['AIRFLOW_HOME']

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 7, 12, 0, 0),
    'retries' : 3,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id='ETL_Pipeline',
    default_args = default_args,
    schedule_interval='@daily'
) as dag:

    run_etl = BashOperator(
        task_id = "run_ETL",
        bash_command = f"pip install -r requiremets.txt && python {path}/dags/src/user_interaction_data.py"
    )

run_etl