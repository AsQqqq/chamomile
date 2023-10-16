import sqlite3
from datetime import datetime

generate_list = [["ВАЗ-2107", "А123ВС77", "Иванов Иван Иванович", "неисправность двигателя"],
["BMW X5", "У456ОР50", "Петров Петр Петрович", "проблемы с трансмиссией"],
["Ford Focus", "Е789АХ159", "Сидоров Сидор Сидорович", "сломана передняя подвеска"],
["Toyota Camry", "К987МО123", "Николаев Николай Николаевич", "поломка - проблемы с электрикой"],
["Mercedes-Benz E-Class", "Р654СК30", "Козлов Константин Константинович", "неисправность системы охлаждения"],
["Volkswagen Golf", "В321ОТ159", "Смирнова Ольга Ивановна", "проблемы с тормозной системой"],
["Audi A4", "М456НХ77", "Зайцева Елена Петровна", "не работает кондиционер"],
["Chevrolet Cruze", "Е654ХО50", "Морозов Алексей Сергеевич", "сломано стекло двери"],
["Hyundai Sonata", "О987АС123", "Ильин Илья Игоревич", "проблемы с системой впрыска топлива"],
["Nissan Qashqai", "Л321КЕ159", "Гаврилова Анна Сергеевна", "неисправность электронной системы управления"],
["Mitsubishi Outlander", "К123ОР77", "Федоров Федор Федорович", "проблемы с системой стабилизации"],
["Opel Astra", "М456СТ50", "Кузнецов Дмитрий Александрович", "сломана рулевая колонка"],
["Renault Duster", "А987НУ123", "Соколова Анастасия Владимировна", "проблемы с системой зажигания"],
["Peugeot 308", "В321РР159", "Иванова Екатерина Ивановна", "не работает центральный замок"],
["Skoda Octavia", "Р654РО30", "Ковалев Артем Сергеевич", "проблемы с системой ABS"],
["Subaru Forester", "Е654АЕ77", "Попов Сергей Павлович", "не работает задний стеклоочиститель"],
["Kia Sportage", "О987СО50", "Григорьева Мария Алексеевна", "сломана задняя левая фара"],
["Honda Civic", "Л321АХ123", "Жуков Игорь Викторович", "проблемы с системой подачи топлива"],
["Mazda CX-5", "М456МО159", "Соловьева Алина Андреевна", "не работает стеклоподъемник на задней правой двери"],
["BMW 3 Series", "А987ОК77", "Романов Роман Романович", "проблемы с системой охлаждения двигателя"],
["Ford Mustang", "В321УХ50", "Киселев Александр Владимирович", "сломан задний бампер"],
["Toyota Corolla", "Р654ЕА123", "Воробьев Владимир Сергеевич", "проблемы с системой зажигания"],
["Mercedes-Benz C-Class", "О987ТО159", "Игнатьева Екатерина Александровна", "не работает система навигации"],
["Volkswagen Passat", "Л321СК30", "Дмитриев Дмитрий Дмитриевич", "проблемы с датчиками давления в шинах"],
["Audi Q5", "М456МХ77", "Королев Алексей Алексеевич", "сломана задняя правая амортизационная стойка"],
["Chevrolet Malibu", "А987ОТ50", "Степанова Ольга Викторовна", "проблемы с системой стабилизации"],
["Hyundai Elantra", "В321АН123", "Лебедев Иван Сергеевич", "не работает задний правый стоп-сигнал"],
["Nissan Juke", "Р654НО159", "Максимов Максим Максимович", "проблемы с системой вентиляции"],
["Mitsubishi Lancer", "О987СР30", "Прокофьева Анна Александровна", "сломана передняя правая пружина"],
["Opel Corsa", "Л321МО77", "Исаев Александр Иванович", "проблемы с системой охлаждения"]]

class mainBase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("local.sqlite")
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        """Создаем таблицу, если она не существует"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS account (login TEXT, password TEXT, status BOOL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cars (carname TEXT, carnumber TEXT, fullname TEXT, description TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS carsassept (carname TEXT, carnumber TEXT, fullname TEXT, description TEXT, startedDate TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS carsend (carname TEXT, carnumber TEXT, fullname TEXT, description TEXT, startedDate TEXT, endDate TEXT)''')
        self.cursor.execute('''INSERT INTO account(login, password, status) VALUES ("root", "root", 0)''')
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
    
    def generateMAIN(self) -> list:
        for i in generate_list: 
            self.cursor.execute('''INSERT INTO cars(carname, carnumber, fullname, description) VALUES (?, ?, ?, ?)''',
                            (i[0], i[1], i[2], i[3]))
            self.connection.commit()
        self.cursor.execute('''SELECT * FROM cars''')
        return self.cursor.fetchall()
    
    
    def updateMAIN(self) -> list:
        self.cursor.execute('''SELECT * FROM cars''')
        return self.cursor.fetchall()
    
    
    def updateCLIENT(self) -> list:
        self.cursor.execute('''SELECT * FROM carsassept''')
        return self.cursor.fetchall()
    
    
    def changeCarsMAIN(self, carNumber: str) -> bool:
        self.cursor.execute('''SELECT * FROM cars WHERE lower(carnumber) = lower(?)''',(carNumber,))
        res = self.cursor.fetchall()
        
        if res == []:
            return False
        
        if res:
            carname, carnumber, fullname, description = res[0]

        now = datetime.now()
        formatted_date = now.strftime("%d.%m.%Y")

        self.cursor.execute('''INSERT INTO carsassept(carname, carnumber, fullname, description, startedDate) VALUES (?, ?, ?, ?, ?)''',
                            (carname, carnumber, fullname, description, formatted_date))
        self.connection.commit()
        
        self.cursor.execute('''DELETE FROM cars WHERE lower(carnumber) = lower(?)''', (carNumber,))
        self.connection.commit()
        
        self.cursor.execute('''SELECT * FROM carsassept''')
        all_rows = self.cursor.fetchall()
        return all_rows
    
    
    def changeCarsCLIENT(self, carNumber: str) -> bool:
        self.cursor.execute('''SELECT * FROM carsassept WHERE lower(carnumber) = lower(?)''',(carNumber,))
        res = self.cursor.fetchall()
        
        if res == []:
            return False
        
        if res:
            carname, carnumber, fullname, description, startedDate  = res[0]

        now = datetime.now()
        formatted_date = now.strftime("%d.%m.%Y")

        self.cursor.execute('''INSERT INTO carsend(carname, carnumber, fullname, description, startedDate, endDate) VALUES (?, ?, ?, ?, ?, ?)''',
                            (carname, carnumber, fullname, description, startedDate, formatted_date))
        self.connection.commit()
        
        self.cursor.execute('''DELETE FROM carsassept WHERE lower(carnumber) = lower(?)''', (carNumber,))
        self.connection.commit()
        
        return True
            
    
