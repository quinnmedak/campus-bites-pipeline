import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Connection settings for the local PostgreSQL database running in Docker
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "campus_bites",
    "user": "postgres",
    "password": "postgres",
}

CSV_PATH = "data/campus_bites_orders.csv"

# SQL statement to create the orders table if it doesn't already exist
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS orders (
    order_id            INTEGER PRIMARY KEY,
    order_date          DATE,
    order_time          TIME,
    customer_segment    TEXT,
    order_value         NUMERIC(8, 2),
    cuisine_type        TEXT,
    delivery_time_mins  INTEGER,
    promo_code_used     TEXT,
    is_reorder          TEXT
);
"""

def load():
    # Read the CSV file into a DataFrame
    df = pd.read_csv(CSV_PATH)

    # Connect to the database and open a cursor
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Create the orders table if it doesn't exist
    cur.execute(CREATE_TABLE_SQL)

    # Insert all rows into the orders table
    # ON CONFLICT DO NOTHING makes the script safe to re-run without duplicating rows
    rows = list(df.itertuples(index=False, name=None))
    execute_values(
        cur,
        """
        INSERT INTO orders (
            order_id, order_date, order_time, customer_segment,
            order_value, cuisine_type, delivery_time_mins,
            promo_code_used, is_reorder
        ) VALUES %s
        ON CONFLICT (order_id) DO NOTHING
        """,
        rows,
    )

    conn.commit()
    cur.close()
    conn.close()

    print(f"Loaded {len(rows)} rows into orders.")

if __name__ == "__main__":
    load()
