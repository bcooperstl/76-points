#!/usr/bin/python3

import configparser
import pprint

FILENAME = "../resources/76points.properties"

properties = {}
loaded = False



def load_database_properties():
    parser = configparser.ConfigParser()
    parser.read(FILENAME)
    properties["username"]=parser.get("database","username")
    properties["password"]=parser.get("database","password")
    properties["database"]=parser.get("database","database")
    properties["host"]=parser.get("database","host")
    loaded = True
    
def get_username():
    if loaded == False:
        load_database_properties()
    return properties["username"]

def get_password():
    if loaded == False:
        load_database_properties()
    return properties["password"]

def get_database():
    if loaded == False:
        load_database_properties()
    return properties["database"]

def get_host():
    if loaded == False:
        load_database_properties()
    return properties["host"]

if __name__ == '__main__':
    load_database_properties()
    pprint.pprint(properties)
    print("username:"+get_username())
    print("password:"+get_password())
    print("database:"+get_database())
    print("host:"+get_host())
    
