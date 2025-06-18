import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    user = os.getenv("SNOWFLAKE_USER"),
    password = os.getenv("SNOWFLAKE_PASSWORD"),
    account = os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
    database = os.getenv("SNOWFLAKE_DATABASE")
)

query = "SELECT * FROM unified_missions"
df = pd.read_sql(query,conn)
df.to_csv("Data/cleaned_combined.csv",index=False)
conn.close()

print("Downloaded and saved")