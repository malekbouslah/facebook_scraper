import mysql.connector
from mysql.connector import Error
from datetime import datetime


def save_to_db(posts, page_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='scraping',
            user='root',
            password='root/0000'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS scraped_data (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                page_name VARCHAR(255),
                                text TEXT,
                                likes INT,
                                comments INT,
                                shares INT,
                                time DATETIME
                            )
                        """)
            print("Table created successfully")
            for post in posts:
                query = """INSERT INTO scraped_data (page_name, text, likes, comments, shares, time) 
                           VALUES (%s, %s, %s, %s, %s, %s)"""
                record = (page_name, post["text"], post["likes"], post["comments"], post["shares"], datetime.fromisoformat(post["time"]))
                cursor.execute(query, record)
            connection.commit()
            print("Records inserted successfully")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
