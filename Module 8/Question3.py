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
    icao_code1 = input("Give first airport ICAO code: ").upper()
    icao_code2 = input("Give second airport ICAO code: ").upper()
    airport1_coordinates = get_airport_coordinates(icao_code1)
    airport2_coordinates = get_airport_coordinates(icao_code2)
    distance = geodesic(airport1_coordinates, airport2_coordinates)
    print(f"Distance between {icao_code1} and {icao_code2}: {distance} kilometers")


run_airport_distance()
