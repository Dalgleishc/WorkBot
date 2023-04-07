import sqlite3

# Connect to the database (create a new one if it doesn't exist)
conn = sqlite3.connect('workbot.db')

# Create a table for storing user information
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             height FLOAT,
             weight FLOAT,
             age INTEGER,
             body_fat FLOAT,
             bench_max FLOAT,
             squat_max FLOAT,
             deadlift_max FLOAT)''')

# Insert a new user into the database
def add_user(height, weight, age, body_fat, bench_max, squat_max, deadlift_max):
    conn.execute("INSERT INTO users (height, weight, age, body_fat, bench_max, squat_max, deadlift_max) \
                  VALUES (?, ?, ?, ?, ?, ?, ?)", (height, weight, age, body_fat, bench_max, squat_max, deadlift_max))
    conn.commit()
    print("User added successfully!")

# Retrieve user information from the database
def get_user(id):
    cursor = conn.execute("SELECT * from users WHERE id=?", (id,))
    user = cursor.fetchone()
    return user

# Close the database connection
def close_connection():
    conn.close()
