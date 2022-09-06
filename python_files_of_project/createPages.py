"""
createPages.py
====================================
This module to create du1 and du2 tabs
"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from du1_page import CreateDu1
from du2_page import CreateDu2

from mqttEvents import Mqtt as mqtt

class CreatePages(QWidget):

    def __init__(self, parent = None):
        super(CreatePages, self).__init__(parent)
        mqtt.run(1)
        self.create()

    def create(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: #031122;")
        self.setGeometry(100, 100, 940, 640)

        tabWidget = QTabWidget()
        du1 = CreateDu1()
        du2 = CreateDu2()
        
        tabWidget.addTab(du1, "DU 1")
        tabWidget.addTab(du2, "DU 2")
        
        layout.addWidget(tabWidget, 0, 0)
        tabWidget.setTabPosition(QTabWidget.West)

    def closeWindow(self):
        self.close()
    
def main():
    app = QApplication(sys.argv)
    ex = CreatePages()
    ex.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
