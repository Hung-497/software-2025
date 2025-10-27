from flask import Flask, Response
import json
import mysql.connector

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

app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    try:
        sql = f"select name, municipality from airport where ident = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (icao,))
        row = cursor.fetchone()
        if row:
            response = {
                "ICAO": icao.upper(),
                "Name": row[0],
                "Location": row[1]
            }
        else:
            response = {
                "ICAO": "No airport found"
            }
        json_response = json.dumps(response)
        response = Response(response=json_response, status=400, mimetype="application/json")
        return response
    except ValueError:
        response = {
            "message": "Database failed",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

