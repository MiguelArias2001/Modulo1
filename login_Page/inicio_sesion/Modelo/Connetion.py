import configparser as configdb
from mysql.connector import connect, errorcode, Error


class Connection:
    _instance = None

    def __init__(self):
        if Connection._instance != None:
            raise Exception("La coneccion ya esta en uso")
        else:
            try:
                config = configdb.ConfigParser()
                config.read('Modulo1/login_Page/inicio_sesion/Modelo/config.ini')
                print(config.sections())
                Connection._instance = self
                mysql_config = config['MySQL']
                self.conn = connect(
                    host=mysql_config['host'],
                    user=mysql_config['user'],
                    password=mysql_config['password'],
                    database=mysql_config['database']
                )
                self.conn.autocommit = True  # type: ignore
                print(self.conn.is_connected())
            except Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
                    self.conn.close()

    @staticmethod
    def get_instance():
        if Connection._instance == None:
            Connection()
        return Connection._instance

    def execute_query(self, query: str, params: tuple):
        if not self.conn:
            raise Exception("La conexión a la base de datos no se ha establecido correctamente.")
        if self.conn.is_connected() == False:
             self.conn.reconnect()
        cursor = self.conn.cursor(buffered=True)
        try:
            cursor.execute(query, params, multi=True)
            print(cursor)
            result = cursor.fetchone()
        except Error as err:
            print(err)
            result = None
        finally:
            cursor.close()
            self.conn.close()
        return result
