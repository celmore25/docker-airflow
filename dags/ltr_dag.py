from datetime import datetime, timedelta
from airflow import DAG
# from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import sys
sys.path.insert(1, '/usr/local/airflow/ltr')
sys.path.insert(1, '/usr/local/airflow/ltr/files')
# from invoke import *


LTR_DEFAULT_ARGS = {
#    'owner': 'Jermey "the big man" Demlow aka Office Linebacker',
#       https://www.youtube.com/watch?v=RzToNo7A-94
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('ltr_dag',
        description='Testing ML LTR Model',
        schedule_interval='0 12 * * *',
        start_date = datetime(2017,3,20), catchup=False,
        default_args = LTR_DEFAULT_ARGS)

# bash_command = 'source /home/vailairflowVM/airflowproc/scripts/ltr/files/set_up.sh'

set_env = BashOperator(
    task_id='set_up_environment',
    bash_command=f'source /usr/local/airflow/ltr/files/set_up.sh ',
    dag=dag
)

def main():
    pass 

run_model = PythonOperator(
        task_id ='Invoke',
        python_callable = main,
        dag=dag)

set_env >> run_model