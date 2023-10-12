from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget

import serviceLogin
import serviceMain
import serviceClient


class CommonApp(QWidget):
    # switch_window = pyqtSignal()
    
    def __init__(self, parent=None) -> None:
        """Этот класс делает что бы параметры не повторялись везде,
        эти параметры применяются ко всем подключенным дизайнам"""
        super(CommonApp, self).__init__(parent)

        self.setFixedSize(859, 455)
        self.m_drag = False
        self.m_DragPosition = QPoint()



class serviceLoginApp(CommonApp, serviceLogin.Ui_Form):
    swithToMain = pyqtSignal()
    
    def __init__(self, parent=None) -> None:
        """Это подключение дизайна, который был сделан в pyqt5 designer"""
        super(serviceLoginApp, self).__init__(parent)
        self.setupUi(self)

        self.login: str = None
        self.password: str = None

        self.connected()
    
    def connected(self) -> None:
        """Подключение кнопок, полей ввода и подобного и указания что им делать"""
        self.signup.clicked.connect(self.swithToMain)

        self.Login.textChanged.connect(self.changeLogin)
        self.Password.textChanged.connect(self.changePassword)
    
    def buttonEnable(self):
        """Проверка на поля(выключение кнопки)"""
        if len(self.Login.text()) >= 3 and len(self.Password.text()) >= 10:
            self.signup.setEnabled(True) # Включение кнопки
        else:
            self.signup.setEnabled(False) # Выключение кнопки
 
    def changeLogin(self, text: str) -> None:
        """Если пользователь изменил ввод в login,
        то делаем проверку"""
        self.buttonEnable()
    
    def changePassword(self, text: str) -> None:
        """Если пользователь изменил ввод в password,
        то делаем проверку"""
        self.buttonEnable()


class serviceMainApp(CommonApp, serviceMain.Ui_Form):
    swithToClient = pyqtSignal()
    
    def __init__(self, parent=None) -> None:
        """Это подключение дизайна, который был сделан в pyqt5 designer"""
        super(serviceMainApp, self).__init__(parent)
        self.setupUi(self)

        self.connected()
    
    def connected(self) -> None:
        pass




class MainApp(QtWidgets.QApplication):
    """Эта функция позволяет всем окнам загрузиться, вся логика настроенна здесь"""
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)

        self.login = serviceLoginApp() # Здесь обьявляется окно
        self.login.swithToMain.connect(self.showMain) # Тут мы потключуем сигнал для перехода в другое окно
        
        self.main = serviceMainApp() # Здесь обьявляется окно
        self.main.swithToClient.connect(self.showClient) # Тут мы потключуем сигнал для перехода в другое окно
        

        self.login.show()

        # if ldb().select_join():
        #     self.main.show()
        # else:
        #     self.login.show()
        
    """---------------"""

    def getPosition(self):
        """Здесь мы получаем место положения окна,
        для того что бы потом новое окно поставить на его место"""
        if self.activeWindow() is not None:
            return self.activeWindow().pos()
        else:
            return QtCore.QPoint(0, 0)

    def showMain(self):
        """Переключаемся на другое окно"""
        window_pos = self.getPosition()
        self.main.move(window_pos)
        self.main.show()
        self.login.close()
    
    def showClient(self):
        """Переключаемся на другое окно"""
        window_pos = self.getPosition()
        self.main.move(window_pos)
        self.main.show()
        self.login.close()
    
    # def showLogin(self):
    #     """Переключаемся на другое окно"""
    #     window_pos = self.getPosition()
    #     self.main.move(window_pos)
    #     self.main.show()
    #     self.login.close()
    
    # def showLogin(self):
    #     """Переключаемся на другое окно"""
    #     window_pos = self.getPosition()
    #     self.main.move(window_pos)
    #     self.main.show()
    #     self.login.close()
    


if __name__ == "__main__":
    import sys
    app = MainApp(sys.argv)
    sys.exit(app.exec())