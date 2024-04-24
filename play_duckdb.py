import duckdb

cursor = duckdb.connect(database="ducktest.db")
print(cursor.execute("SELECT 42").fetchall())


cursor.execute("CREATE TABLE IF NOT EXISTS t1 (i INTEGER, j INTEGER);")

for i in range(1, 44444):
    cursor.execute(f"INSERT INTO t1 (i, j) VALUES ({i}, {i + i})")


cursor.execute("Select count(*) from t1;")
