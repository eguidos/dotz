import mysql.connector as mysql


class Start:

    def __init__(self):
        self.mysql = mysql

    def config(self):
        try:
            bd = self.mysql.connect(
                host="localhost",
                user="root",
                passwd="admin",
                db="mysql"
            )
            return bd
        except ConnectionError:
            print(f'Um erro foi encontrado ao acessar o banco {self.mysql}')
        finally:
            print(f'Conexão realizada com sucesso')


