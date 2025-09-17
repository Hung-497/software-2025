import mysql.connector


def get_airports_by_country(country_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Giahung@!497',
        autocommit=True)
    sql = f"select type, count(*) as airport_count from airport where iso_country = '{country_code}' and type != 'closed' group by type order by airport_count desc;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    airports = get_airports_by_country(country_code)
    print(f"Airports in {country_code}:")
    for airport in airports:
        print(f"{airport[1]} {airport[0]} airports")


run_country_program()
