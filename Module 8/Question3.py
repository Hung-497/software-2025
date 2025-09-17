import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Giahung@!497',
        autocommit=True)
    cursor = connection.cursor()
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def run_airport_distance():
    icao_code1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").upper()

    airport1_coordinates = get_airport_coordinates(icao_code1)
    if airport1_coordinates is None:
        print(f"Airport with ICAO code {icao_code1} not found in the database.")
        return
    airport2_coordinates = get_airport_coordinates(icao_code2)
    if airport2_coordinates is None:
        print(f"Airport with ICAO code {icao_code2} not found in the database.")
        return
    distance = geodesic(airport1_coordinates, airport2_coordinates).kilometers
    print(f"Distance between {icao_code1} and {icao_code2}: {distance:.2f} kilometers")

run_airport_distance()
