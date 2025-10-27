import mysql.connector
def flight_game(code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Giahung@!497',
        autocommit=True,
        auth_plugin="mysql_native_password",
        use_pure=True
    )

    sql = f"select name, municipality from airport where ident ='{code}' "
    cursor = connection.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        print(f"Airport name: {row[0]}")
        print(f"Location: {row[1]}")
    else:
        print(f"No airport found with ICAO code {code}")
    cursor.close()
    connection.close()
code = input("Enter the ICAO code of an airport: ").strip().upper()
flight_game(code)