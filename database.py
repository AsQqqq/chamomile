import sqlite3

class mainBase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("local.sqlite")
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        """Создаем таблицу, если она не существует"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS account (login TEXT, password TEXT, status BOOL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cars (carname TEXT, carnumber TEXT, fullname TEXT, description TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS carsassept (carname TEXT, carnumber TEXT, fullname TEXT, description TEXT, datestart TEXT, datefinish TEXT, status BOOL)''')
        self.connection.commit()
    
    def checkSignUp(self, login: str, password: str) -> bool:
        """Проверяем есть ли такой аккаунт в базе"""
        self.cursor.execute('''SELECT login, password FROM account WHERE login = ? AND password = ?''',
                             (login, password,))
        if self.cursor.fetchmany(1) != []:
            self.cursor.execute('''UPDATE account SET status = ? WHERE login = ?''', (1, login,))
            self.connection.commit()
            return True
        return False

    def join(self) -> bool:
        self.cursor.execute('''SELECT login FROM account WHERE status = 1''')
        if self.cursor.fetchmany(1) != []:
            return True
        return False

    def exit(self) -> None:
        self.cursor.execute('''SELECT login FROM account WHERE status = 1''')
        login = self.cursor.fetchone()
        self.cursor.execute('''UPDATE account SET status = ? WHERE login = ?''', (0, login[0],))
        self.connection.commit()