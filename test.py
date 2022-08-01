from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from du1_page import CreateDu1
from du2_page import CreateDu2

class CreatePages(QWidget):

    def create(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(100, 100, 940, 640)

        tabWidget = QTabWidget()
        du1 = CreateDu1()
        du2 = CreateDu2()
        
        tabWidget.addTab(du1, "DU 1")
        tabWidget.addTab(du2, "DU 2")
        
        layout.addWidget(tabWidget, 0, 0)
        tabWidget.setTabPosition(QTabWidget.West)

        self.show()

    def closeWindow(self):
        self.close()
