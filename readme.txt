Task 1: 
This ETL process extracts user interaction data from a CSV file, cleans and transforms it, and then loads it into a database table.

Below ETL pipeline contains multiple steps to perfrom Extract, Transform and Load

1. Ingestion (ingest_data function):
Reads data from a CSV file.
Defines a dictionary dtype_dict to specify data types for each column during import:
interaction_id: Integer (Int64)
user_id: Integer (Int64)
product_id: Integer (Int64)
action: String (str)
timestamp: String (str) (will be converted later)
Uses pd.read_csv function from pandas library to read the data with the specified data types.
Returns the loaded DataFrame (df).

2. Cleaning (clean_data function):
Handles missing values:
Fills missing values in the action column with the string "unknown" using fillna function.
Drops rows with missing values in user_id, product_id, or timestamp columns using dropna function.
Converts the timestamp column from string to datetime format using pd.to_datetime function.
Returns the cleaned DataFrame (df).

3. Transformation (transform_data function):
Introduces a new column interaction_count.
Uses groupby on user_id and product_id to group the data.
Applies the transform method with the size function to calculate the count of interactions for each user-product combination and stores it in the new interaction_count column.
Returns the DataFrame with the added column (df).

4. Loading (create_connection and load_data functions):

create_connection function:
Establishes a connection to a database using sqlalchemy
Returns the created engine object (engine).

load_data function:
Calls create_connection to get the database engine. 

Uses the to_sql function from the pandas library to write the DataFrame (df) to a table named interaction_data in the connected database using the engine (engine).
Sets index=False to avoid writing the DataFrame index as a column in the table.

Prints a success message upon successful data loading.

Steps to run the code:

Prerequisites:
1. Install python 
2. Make sure the user_interaction_data.csv exists on the same location that your code exists
3. Install Postgres DB or provide the JDBC connection string for the existing Postgres Server 

1. create a virtual env andf activate 
Below sample command for the windows powershell 
python -m venv env
env/bin/Activate.ps1 

2. Install all the required modules using the requirements.txt file 
pip install -r requirements.txt

3. Execute the python scripts 
python user_interaction_data.py


Task 2: 

Instructions on how to set up and run the Airflow environme 
1. Install docker destop 
2. Get the docker-compose.yaml file provided in Airflow document using curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'
3. Create dags, config, logs and plugins folder to mount to the Docker containers 
4. run the docker file 
docker-compose up airflow-init
docker-compose up

Dag file named dags\etl_dag.py should be available with the dag name ETL_Pipeline to run on the airflow page running on localhost:8080.
    
Task 3:
SQL/user_interaction_data.sql
Execute the above sql file for schema creation, data insertion, data retrieval and created index for the most used columns to improve the query performance 

