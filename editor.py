import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(250, 150)
        self.setWindowTitle('simple')
        self.show()


app = QApplication(sys.argv)
main_window = MyWidget()


sys.exit(app.exec_())