#!/usr/bin/python3

import mysql.connector
import database_connection
import pprint

SCORE_73_76 = '73-76'
SCORE_74_77 = '74-77'
SCORE_75_78 = '75-78'
SCORE_74_76 = '74-76'
SCORE_75_77 = '75-77'
SCORE_75_76 = '75-76'
SCORE_UNDER = 'Under'

SELECT_SQL = "select result_type_id, name, description, start_score, end_score, is_76 from result_types"
known_types = [SCORE_73_76, SCORE_74_77, SCORE_75_78, SCORE_74_76, SCORE_75_77, SCORE_75_76, SCORE_UNDER]
result_types = {}

def load_to_dict():
    conn = database_connection.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchall()
        for row in rows:
            print("is_76 "+str(row[5]))
            if row[1] not in known_types:
                print("****Result type "+row[1]+" not known*****")
            result_types[row[1]]={"result_type_id":row[0],
                                "name":row[1],
                                "description":row[2],
                                "start_score":row[3],
                                "end_score":row[4],
                                "is_76":row[5]==1}
        
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        cursor.close()
    
def get_result_type(type):
    if not result_types:
        load_to_dict()
    return result_types.get(type)

if __name__ == '__main__':
    load_to_dict()
    pprint.pprint(result_types)
    print("73 to 76: "+str(get_result_type(SCORE_73_76)))
    print("75 to 77: "+str(get_result_type(SCORE_75_77)))
    print("Under: "+str(get_result_type(SCORE_UNDER)))
    