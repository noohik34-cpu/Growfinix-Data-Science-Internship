import sqlite3
import pandas as pd

# Create database
conn = sqlite3.connect("travel.db")

# Load CSV files
users = pd.read_csv("Task4_SQL/users.csv")
bookings = pd.read_csv("Task4_SQL/bookings.csv")

# Store tables in SQLite
users.to_sql("users", conn, if_exists="replace", index=False)
bookings.to_sql("bookings", conn, if_exists="replace", index=False)

# SQL JOIN Query
query = """
SELECT
users.user_id,
users.name,
users.city,
bookings.destination,
bookings.amount
FROM users
INNER JOIN bookings
ON users.user_id = bookings.user_id
"""

result = pd.read_sql(query, conn)

print(result)

result.to_csv("Task4_SQL/final_output.csv", index=False)

conn.close()

print("\nTask 4 Completed Successfully!")