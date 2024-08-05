import MySQLdb
import sys
username = ''
password = ''
database = 'app_info'


def fetch_app_name(dbconn):
    try:
        db = MySql.connect(username, password, database)
    except:
        print("error while connecting")
        sys.exit()
    db.cursor
    sql = "select application_name, description from applications"
    results = db.fetchall()
    result_dump = {}
    for i in results:
        application_name = i[0]
        description = i[1]
        result_dump = application_name[description]
        #print(json.dump(result_dump))
        with open('result.json', w):
            result_dump.json.write(result_dump)




