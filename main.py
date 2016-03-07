import sqlite3
import os


openconnection=sqlite3.connect('sevenfortyone.db')
openconnectioncursor=openconnection.cursor()


openconnectioncursor.execute("CREATE TABLE IF NOT EXISTS customers(first_name VARCHAR(30) NOT NULL, last_name VARCHAR(30) NOT NULL, email VARCHAR(60) NULL, phone CHAR(10) NOT NULL, street VARCHAR(50) NOT NULL, city VARCHAR(40) NOT NULL, state CHAR(2) NOT NULL, zipcode MEDIUMINT UNSIGNED NOT NULL, date_entered TIMESTAMP, customer_id INT UNSIGNED NOT NULL PRIMARY KEY)")

openconnectioncursor.execute("INSERT INTO customers VALUES('yusuf', 'salami', 'meat@meat.com', '3333333333', '123 main st', 'ikeja', 'lg', '33333', strftime(), last_insert_rowid())")
openconnection.commit()
openconnection.close()
