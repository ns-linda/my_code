import MysqlDB
import sys
class AppInfo():

    def make_conn(make):
        try:
            db = MysqlDB.connect('localhost', 'db_name','username', 'pwd')
        except:
            sys.exit()
            db.connect()
            conn=db.cursor()
            conn.execute_query("select * from applications where application_name = 'box'")
            x=conn.fetch_all()
            for item in x:
                print(item)

            db.close()

obj = AppInfo()
obj.make_conn()
