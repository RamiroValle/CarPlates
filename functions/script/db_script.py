import mysql.connector
import sys
import json


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("No file passed. Usage: python3 db_script.py [filename].json")
        raise
    if not file_name.endswith('.json'):
        print("File passed is not .json")
        return
    
    db = connect()
    cr = db.cursor()
    with open(file_name, "r") as f:
        js = json.load(f)
    sql = "INSERT INTO cars (plate, model) VALUES (%s, %s) ON DUPLICATE KEY UPDATE id=id"
    cr.executemany(sql, list(js.items()))
    db.commit()
    db.close()


def connect():
    db = mysql.connector.connect(host="db", port=3306, user="admin", password="admin", database="mysql")
    cr = db.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS cars (id INT AUTO_INCREMENT PRIMARY KEY, plate varchar(9) NOT NULL UNIQUE, model varchar(255) NOT NULL)")
    db.commit()
    return db
    

if __name__ == "__main__":
    main()