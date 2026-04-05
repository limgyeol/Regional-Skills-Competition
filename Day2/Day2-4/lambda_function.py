from pymysql.cursors import DictCursor
import pymysql
import json
import os

DB_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv("DB_PORT")),
    'database': os.getenv("DB_NAME"),
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
}

def lambda_handler(event, context):
    method = event['method']
    print(method)
    print(event)

    if method == "POST":
        return create_user(event['body'])
    elif method == "GET":
        return get_user(event['body'])
    elif method == "DELETE":
        return delete_user(event['body'])
    else:
        return {"statusCode": 400, "body": json.dumps({"message": "Unsupported method"})}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

def create_user(body):
    name = body['name']
    age = int(body['age'])
    country = body['country']

    if not all([name, age, country]):
        return {"statusCode": 400, "body": json.dumps({"message": "Missing required fields"})}
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, age, country) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, age, country))
            connection.commit()
    finally:
        connection.close()

    return {"statusCode": 201, "body": json.dumps({"message": "User created successfully"})}

def get_user(body):
    name = body['name']
    age = int(body['age'])

    if not all([name, age]):
        return {"statusCode": 400, "body": json.dumps({"message": "Query parameters missing"})}
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE name = %s AND age = %s"
            cursor.execute(sql, (name, age))
            result = cursor.fetchone()
    finally:
        connection.close()

    if not result:
        return {"statusCode": 404, "body": json.dumps({"message": "User not found"})}

    return {"statusCode": 200, "body": json.dumps(result)}

def delete_user(body):
    name = body['name']
    age = int(body['age'])

    if not all([name, age]):
        return {"statusCode": 400, "body": json.dumps({"message": "Query parameters missing"})}
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE name = %s AND age = %s"
            cursor.execute(sql, (name, age))
            connection.commit()
    finally:
        connection.close()

    return {"statusCode": 200, "body": json.dumps({"message": "User deleted successfully"})}