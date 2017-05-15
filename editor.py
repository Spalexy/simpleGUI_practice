import sys
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QAction
from PyQt5.QtGui import QIcon

class MyWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(250, 150)
        self.setWindowTitle('simple')
        self.setWindowIcon(QIcon('pencil.jpg'))

        exitAction = QAction('Save', self)
        exitAction.setShortcut('Ctrl+S')
        exitAction.setStatusTip('Сохранить файл')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction('Exit', self)
        saveAction.setShortcut('Ctrl+Q')
        saveAction.setStatusTip('Выход из приложения')
        saveAction.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')        
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        self.show()


app = QApplication(sys.argv)
main_window = MyWidget()


sys.exit(app.exec_())