import sys
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QAction
from PyQt5.QtGui import QIcon

class MyWidget(QMainWindow):
    """Главное окно.

    Класс, создающий главное окно и элементы интерфейса.
    Метод menu_bar создает графическое меню. 

    """
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(250, 150)
        self.setWindowTitle('Текстовый редактор')
        self.setWindowIcon(QIcon('pencil.jpg'))
        self.menu_bar()
        self.show()

    def menu_bar(self):
        exitAction = QAction('Save', self)
        exitAction.setShortcut('Ctrl+S')
        exitAction.setStatusTip('Сохранить файл')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction('Exit', self)
        saveAction.setShortcut('Ctrl+Q')
        saveAction.setStatusTip('Выход из приложения')
        saveAction.triggered.connect(qApp.quit)

        # self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')        
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        


app = QApplication(sys.argv)
main_window = MyWidget()


sys.exit(app.exec_())