#!/usr/bin/python3

import mysql.connector
import database_connection
import pprint

HOME = 'H'
AWAY = 'A'
NEUTRAL = 'N'

SELECT_SQL = "select game_location_id, game_location from game_locations"
known_locations = [HOME, AWAY, NEUTRAL]
game_locations = {}

def load_to_dict():
    conn = database_connection.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchall()
        for row in rows:
            if row[0] not in known_locations:
                print("****Game location "+row[0]+" not known*****")
            game_locations[row[0]]={"game_location_id":row[0],"game_location":row[1]}
        
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        cursor.close()
    
def get_game_location(location):
    if not game_locations:
        load_to_dict()
    return game_locations.get(location)

if __name__ == '__main__':
    load_to_dict()
    pprint.pprint(game_locations)
    print("Home: "+str(get_game_location(HOME)))
    print("Away: "+str(get_game_location(AWAY)))
    print("Neutral: "+str(get_game_location(NEUTRAL)))
    