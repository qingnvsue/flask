import mysql.connector
import psycopg2
from mysql.connector import errorcode


class ConnectPostgreSQL:

    def __init__(self):
        self.config = {
            'host': 'localhost',
            'database': 'foodmart',
            'user': 'postgres',
            'password': 'master'
        }
        self.cnx = psycopg2

    def connect(self):
        try:
            self.cnx = psycopg2.connect(**self.config)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to database", error)

    def disconnect(self):
        try:
            self.cnx.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while disconnecting from database", error)

    def query(self, query):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query)
            return cursor
        except (Exception, psycopg2.Error) as error:
            print("Error while retrieving query", error)



class ConnectMySQL:

    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'master',
            'host': 'localhost',
            'database': 'foodmart',
            'auth_plugin': 'mysql_native_password',
            'raise_on_warnings': True
        }
        self.cnx = mysql.connector

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist.")
            else:
                print(err)

    def disconnect(self):
        try:
            self.cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ABORTING_CONNECTION:
                print("Error aborting connection.")
            else:
                print(err)

    def query(self, query):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query)
            return cursor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_QUERY_INTERRUPTED:
                print("The query was interrupted.")
            else:
                print(err)
