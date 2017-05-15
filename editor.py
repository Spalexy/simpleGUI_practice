import sys
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QAction
from PyQt5.QtGui import QIcon

class MyWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(250, 150)
        self.setWindowTitle('simple')
        self.setWindowIcon(QIcon('pencil.jpg'))

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.show()


app = QApplication(sys.argv)
main_window = MyWidget()


sys.exit(app.exec_())