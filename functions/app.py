import redis
import json
import mysql.connector

redis_server = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
db = mysql.connector.connect(host="db", port=3306, user="admin", password="admin", database="mysql")


def handler(event, context):
    """Handler for the model requests. Plate should be passed in the event"""
    try:
        # browser request
        plate = event['pathParameters']['plate']
    except KeyError:
        # lambda invoke
        plate = event.get('plate')

    if plate == "undefined":
        return {
            "statusCode": 400
        }

    # requesting the model to the cache first.
    car = redis_server.get(plate)

    if not car:
        # if not found in the cache it is requested to the db
        cr = db.cursor()
        cr.execute(f"SELECT model FROM cars WHERE plate= '{plate}'")
        car = cr.fetchone()
        if car:
            car = car[0]
            # if found in the db, it is saved in cache
            redis_server.set(plate, car)
        else:
            return {
                "statusCode": 400
            }

    return {
        "statusCode": 200,
        "body": json.dumps({"model": car})
    }
