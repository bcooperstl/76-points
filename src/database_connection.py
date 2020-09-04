#!/usr/bin/python3

import mysql.connector
import database_properties

conn = None

def open_connection():
    global conn
    close_connection()
    try:
        conn = mysql.connector.connect(user=database_properties.get_username(),
                                             password=database_properties.get_password(),
                                             host=database_properties.get_host(),
                                             database=database_properties.get_database())
        print("Database connection established to"+database_properties.get_username()+"@"+database_properties.get_host()+":"+database_properties.get_database())
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        conn = None

def get_connection():
    global conn
    if conn == None:
        open_connection()
    return conn

def close_connection():
    global conn
    if conn != None:
        conn.close()
        print("Database conneciton closed")
        conn = None

if __name__ == '__main__':
    open_connection()
    close_connection()
