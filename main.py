from re import S
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qtwidgets import Toggle, AnimatedToggle
import sys
import test
from mqttEvents import Mqtt as mqtt

class App(QWidget):
    count = 0
    
    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(100, 100, 980, 600)
        self.setWindowTitle("Control Unit")
        self.middlePanel()
        self.rightPanel()
        self.createButtons()
        self.leftPanel()
        # self.deneme()
    
    def deneme(self):
        toggle_1 = Toggle(self)
        toggle_2 = AnimatedToggle(self,
            checked_color="#FFB000",
            pulse_checked_color="#44FFB000"
        )

        self.layout = QVBoxLayout()
        self.layout.addWidget(toggle_1)
        self.layout.addWidget(toggle_2)
        rect = QRect(80, 80, 100, 100)
        self.layout.setGeometry(rect)
        #self.container.setGeometry(40, 80, 100, 100)

    def middlePanel(self):

        self.label = QLabel("Kumlama\nAnahtarı", self)
        self.label.setGeometry(328, 55, 60, 30)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll1 = QScrollBar(self)
        self.scroll1.setGeometry(324, 90, 50, 90)
        self.scroll1.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 20; min-width: 50px; min-height: 45px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll1.setCursor(Qt.PointingHandCursor)

        """self.imgLabel = QLabel(self)
        self.pixmap = QPixmap('images\BRR2.png')
        self.imgLabel.setPixmap(self.pixmap)
        self.imgLabel.setGeometry(380, 120, 30, 30)"""

        self.label = QLabel("  Pürjör\nAnahtarı", self)
        self.label.setGeometry(422, 55, 60, 30)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll2= QScrollBar(self)
        self.scroll2.setGeometry(418, 90, 50, 90)
        self.scroll2.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 20; min-width: 50px; min-height: 45px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll2.setCursor(Qt.PointingHandCursor)

        self.label = QLabel("Projektör\nAnahtarı", self)
        self.label.setGeometry(516, 55, 60, 30)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll3 = QScrollBar(self)
        self.scroll3.setGeometry(512, 90, 50, 90)
        self.scroll3.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 30px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll3.setCursor(Qt.PointingHandCursor)

        self.label = QLabel("Kabin Aydınlatma-\n  Okuma Lambası\n      Anahtarı", self)
        self.label.setGeometry(595, 45, 90, 40)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll4 = QScrollBar(self)
        self.scroll4.setGeometry(608, 90, 50, 90)
        self.scroll4.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 20; min-width: 50px; min-height: 45px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll4.setCursor(Qt.PointingHandCursor)

    def rightPanel(self):
        self.upButton = QPushButton("", self)
        self.upButton.setGeometry(750, 140, 50, 50)
        self.upButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}"
                                    "QPushButton::pressed{background-color : #734a12;}")
        self.upButton.setIcon(QIcon('images\DIRFWD.png'))
        self.upButton.setCursor(Qt.PointingHandCursor)
        
        self.notrButton = QPushButton("", self)
        self.notrButton.setGeometry(815, 140, 50, 50)
        self.notrButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray; color : black}"
                                      "QPushButton::pressed{background-color : #734a12;}")
        self.notrButton.setIcon(QIcon('images\DIRNTR.png'))
        self.notrButton.setCursor(Qt.PointingHandCursor)
        
        self.downButton = QPushButton("", self)
        self.downButton.setGeometry(880, 140, 50, 50)
        self.downButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray; color : black}"
                                        "QPushButton::pressed{background-color : #734a12;}")
        self.downButton.setIcon(QIcon('images\DIRRWD.png'))
        self.downButton.setCursor(Qt.PointingHandCursor)

        self.frenLabel = QLabel("   Direkt\nFren Valfi", self)
        self.frenLabel.setGeometry(784, 220, 60, 30)
        self.frenLabel.setStyleSheet("QLabel{color : white;}")

        self.scrollFren = QScrollBar(self)
        self.scrollFren.setGeometry(780, 260, 55, 120)
        self.scrollFren.setStyleSheet(  "QScrollBar{background : #a89383; border : 2px solid gray}"
                                        "QScrollBar::handle{background : #483c32; border-radius : 25; min-width: 50px; min-height: 60px;}"
                                        "QScrollBar::handle::pressed{background : #332d28;}")
        self.scrollFren.setCursor(Qt.PointingHandCursor)

        self.kornaLabel = QLabel("Havalı Korna\n  Anahtarı", self)
        self.kornaLabel.setGeometry(780, 400, 80, 30)
        self.kornaLabel.setStyleSheet("QLabel{color : white;}")

        self.scrollKorna = QScrollBar(self)
        self.scrollKorna.setGeometry(786, 440, 40, 100)
        self.scrollKorna.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                        "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                        "QScrollBar::handle::pressed{background : #332d28;}")
        self.scrollKorna.setCursor(Qt.PointingHandCursor)

        self.label = QLabel("Elektrik\nKornası", self)
        self.label.setGeometry(877, 450, 50, 30)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.kornaButton = QPushButton("",self)
        self.kornaButton.setGeometry(870, 480, 50, 50)
        self.kornaButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid gray; background-color : #fcca12; color : black}"
                                    "QPushButton::pressed{background-color : #d9aa02;}")
        self.kornaButton.setCursor(Qt.PointingHandCursor)

    def leftPanel(self):

        self.btnLabel = QLabel("  ERTMS\n    Aşırı\nYükseltme", self)
        self.btnLabel.setGeometry(60, 430, 50, 50)
        self.btnLabel.setStyleSheet("QLabel{color : white;}")

        self.buttonErtms = QPushButton("", self)
        self.buttonErtms.setGeometry(60, 480, 50, 50)
        self.buttonErtms.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid gray; background-color : red;}"
                                    "QPushButton::pressed{background-color : #990000;}")
        self.buttonErtms.setCursor(Qt.PointingHandCursor)

        self.pantoLabel = QLabel("  Panto\nKaldırma\nAnahtarı", self)
        self.pantoLabel.setGeometry(89, 85, 70, 60)
        self.pantoLabel.setStyleSheet("QLabel{color : white;}")

        self.pantoScroll = QScrollBar(self)
        self.pantoScroll.setGeometry(90, 140, 40, 100)
        self.pantoScroll.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                        "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                        "QScrollBar::handle::pressed{background : #332d28;}")
        self.pantoScroll.setCursor(Qt.PointingHandCursor)

        self.mcbLabel = QLabel("   MCB\nAnahtarı", self)
        self.mcbLabel.setGeometry(149, 85, 70, 60)
        self.mcbLabel.setStyleSheet("QLabel{color : white;}")

        self.mcbScroll = QScrollBar(self)
        self.mcbScroll.setGeometry(150, 140, 40, 100)
        self.mcbScroll.setStyleSheet("QScrollBar{background : #a89383; border : 2px solid gray}"
                                     "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                     "QScrollBar::handle::pressed{background : #332d28;}")
        self.mcbScroll.setCursor(Qt.PointingHandCursor)
        
        self.freeErtmsLabel = QLabel(" ERTMS\nSerbest\nBırakma", self)
        self.freeErtmsLabel.setGeometry(91, 250, 70, 60)
        self.freeErtmsLabel.setStyleSheet("QLabel{color : white;}")

        self.freeErtmsScroll = QScrollBar(self)
        self.freeErtmsScroll.setGeometry(90, 310, 40, 100)
        self.freeErtmsScroll.setStyleSheet("QScrollBar{background : #a89383; border : 2px solid gray}"
                                     "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                     "QScrollBar::handle::pressed{background : #332d28;}")
        self.freeErtmsScroll.setCursor(Qt.PointingHandCursor)

        self.takenErtmsLabel = QLabel("ERTMS\n Alındı\nBildirimi", self)
        self.takenErtmsLabel.setGeometry(152, 250, 70, 60)
        self.takenErtmsLabel.setStyleSheet("QLabel{color : white;}")

        self.takenErtmsScroll = QScrollBar(self)
        self.takenErtmsScroll.setGeometry(150, 310, 40, 100)
        self.takenErtmsScroll.setStyleSheet("QScrollBar{background : #a89383; border : 2px solid gray}"
                                     "QScrollBar::handle{background : #fcca12; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                     "QScrollBar::handle::pressed{background : #332d28;}")
        self.takenErtmsScroll.setCursor(Qt.PointingHandCursor)

    def createButtons(self):
        self.connectButton = QPushButton("OFF", self)
        self.connectButton.setGeometry(450, 260, 50, 50)
        self.connectButton.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : red;color : white}")
        self.connectButton.clicked.connect(self.pressButton)
        self.connectButton.setCursor(Qt.PointingHandCursor)

    def pressButton(self):
        
        if self.count%2 == 0:
            self.connectButton.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : green;color : white}")
            self.connectButton.setText("ON")
            self.count += 1
            sleep(0.3)
            mqtt.run(1)
            self.pages = test.CreatePages()
            self.pages.create()
        else:
            self.connectButton.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : red;color : white}")
            self.connectButton.setText("OFF")
            self.count += 1
            sleep(0.3)
            mqtt.run(0)
            self.pages.close()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.white, 2, Qt.SolidLine))

        painter.drawRect(40, 80, 200, 480)     # left panel
        painter.drawRect(740, 80, 200, 480)    # Right panel
        painter.drawRect(280, 40, 420, 150)    # Middle panel
        painter.drawRect(340, 380, 300, 180)   # Main control panel

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()