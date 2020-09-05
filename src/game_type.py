#!/usr/bin/python3

import mysql.connector
import database_connection
import pprint

REGULAR_SEASON = 'R'
POSTSEASON = 'P'

SELECT_SQL = "select game_type_id, game_type from game_types"
known_types = [REGULAR_SEASON, POSTSEASON]
game_types = {}

def load_to_dict():
    conn = database_connection.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchall()
        for row in rows:
            if row[0] not in known_types:
                print("****Game type "+row[0]+" not known*****")
            game_types[row[0]]={"game_type_id":row[0],"game_type":row[1]}
        
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        cursor.close()
    
def get_game_type(type):
    if not game_types:
        load_to_dict()
    return game_types.get(type)

if __name__ == '__main__':
    load_to_dict()
    pprint.pprint(game_types)
    print("Postseason: "+str(get_game_type(POSTSEASON)))
    print("Regular Season: "+str(get_game_type(REGULAR_SEASON)))
    