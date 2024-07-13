import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="Stephen123",
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor.execute('SELECT * FROM sold_data')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
