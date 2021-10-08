from app.apiTools.formatJsonOutput import formatJsonOutput
import pymysql
import pymysql.cursors


def mysqlconnect():
    """Configuration for connect in Data Base"""
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='12182430misael',
        db='challenge',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )

    try:
        with connect.cursor() as cursor:
            sql = "SELECT * FROM data",
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connect.close()

    #Define cursor
    #cursor = connect.cursor()
    #cursor.execute("select * from data")
    #output = cursor.fetchall()
    #print(output)

    #Close connection
    #connect.close()


class AliveAPI():
    """Class for validate if API be UP"""

    def aliveAPIObject(self):
        return {"Alive": 1, "HTTPStatus": 200, "Error": {"errorTitle": None, "errorMessage": None}}

class AliveGetAPIData():