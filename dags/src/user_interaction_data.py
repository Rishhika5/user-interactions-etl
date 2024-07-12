import pandas as pd

# Extract the data from the CSV file 
def ingest_data(file_path):
    dtype_dict = {'interaction_id': 'Int64', 'user_id': 'Int64', 'product_id': 'Int64', 'action': 'str', 'timestamp': 'str'}
    df = pd.read_csv(file_path, dtype=dtype_dict)
    return df

# Clean the data
def clean_data(df):
    # Handle missing values
    df['action'].fillna('unknown', inplace=True)
    df.dropna(subset=['user_id', 'product_id', 'timestamp'], inplace=True)   
    # update the timestand dtype from string to datetime]
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    print(df.dtypes)
    return df

# Transform the data
def transform_data(df):
    df['interaction_count'] = df.groupby(['user_id', 'product_id'])['interaction_id'].transform('size')
    return df

# DB Connection creation
def create_connection():
  from sqlalchemy import create_engine
  # Set search path to prioritize dboschema
  # TODO set the secret params to use from ENV file or config file 
  engine = create_engine('postgresql://postgres:admin@localhost:5432/user_interaction_db')
  return engine

#  Load the Data into PGSql DB
def load_data(df, table_name):
    engine = create_connection()
    # Assuming 'df' is your pandas dataframe, write it to the database table
    df.to_sql(table_name, engine, index=False)
    print("Data loaded successfully!")

# Main function to call the ETL function mentions above in a structural fashion
if __name__ == "__main__":
    file_path = '../data/user_interaction_data.csv'
    data = ingest_data(file_path)
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)
    load_date = load_data(transformed_data, table_name='interaction_data1')

