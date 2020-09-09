from config import config
import mysql.connector


def connect():
    """ Connect to the MySQL database server """
    conn = None
    try:
      params = config()
      
      print('Connecting to the MySQL database...')
      conn = mysql.connector.connect(**params)
      cur = conn.cursor()

      print('MySQL database version:')
      cur.execute('SELECT version()')
      db_version = cur.fetchone()

      print(db_version)       
      cur.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()