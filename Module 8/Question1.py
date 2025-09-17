import mysql.connector
def flight_game(code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Giahung@!497',
        autocommit=True)
    sql = "select name, municipality from airport where ident = %s;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (code,))
    row = cursor.fetchone()
    if row:
        print(f"Airport name: {row['name']}")
        print(f"Location: {row['municipality']}")
    else:
        print(f"No airport found with ICAO code {code}")
    cursor.close()
    connection.close()
code = input("Enter the ICAO code of an airport: ").strip().upper()
flight_game(code)
