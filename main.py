from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import test
from mqttEvents import Mqtt as mqtt
import random
from paho.mqtt import client as mqtt_client
from threading import Thread

class App(QWidget):

    count = 0
    broker = 'localhost'
    topic = 'mqtt'
    client_id = f'python-mqtt-{random.randint(0, 100)}'

    client = mqtt_client.Client(client_id=client_id)
    
    def __init__(self, parent = None):
        super(App, self).__init__(parent)

        self.setStyleSheet("background-color: #031122;")
        self.setGeometry(100, 100, 980, 600)
        self.setWindowTitle("Control Unit")
        self.middlePanel()
        self.rightPanel()
        self.createButtons()
        self.leftPanel()
        self.createImages()

        self.dataThread = Thread(target=self.sendData)
        self.dataThread.start()


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
        self.scroll1.setValue(45)

        self.label = QLabel("  Pürjör\nAnahtarı", self)
        self.label.setGeometry(422, 55, 60, 30)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll2= QScrollBar(self)
        self.scroll2.setGeometry(418, 90, 50, 90)
        self.scroll2.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 20; min-width: 50px; min-height: 45px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll2.setCursor(Qt.PointingHandCursor)
        self.scroll2.setValue(45)

        self.label = QLabel("Projektör\nAnahtarı", self)
        self.label.setGeometry(516, 55, 60, 30)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll3 = QScrollBar(self)
        self.scroll3.setGeometry(512, 90, 50, 90)
        self.scroll3.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 30px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll3.setCursor(Qt.PointingHandCursor)
        self.scroll3.setValue(45)

        self.label = QLabel("Kabin Aydınlatma-\n  Okuma Lambası\n      Anahtarı", self)
        self.label.setGeometry(595, 45, 90, 40)
        self.label.setStyleSheet("QLabel{color : white;}")

        self.scroll4 = QScrollBar(self)
        self.scroll4.setGeometry(608, 90, 50, 90)
        self.scroll4.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                    "QScrollBar::handle{background : #483c32; border-radius : 20; min-width: 50px; min-height: 45px;}"
                                    "QScrollBar::handle::pressed{background : #332d28;}")
        self.scroll4.setCursor(Qt.PointingHandCursor)
        self.scroll4.setValue(45)

    def rightPanel(self):
        self.upButton = QPushButton("", self)
        self.upButton.setGeometry(750, 140, 50, 50)
        self.upButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        self.upButton.setIcon(QIcon('images\DIRFWD.png'))
        self.upButton.setCursor(Qt.PointingHandCursor)
        self.upButton.clicked.connect(self.pressUpButton)

        self.notrButton = QPushButton("", self)
        self.notrButton.setGeometry(815, 140, 50, 50)
        self.notrButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray; color : black}")
        self.notrButton.setIcon(QIcon('images\DIRNTR.png'))
        self.notrButton.setCursor(Qt.PointingHandCursor)
        self.notrButton.clicked.connect(self.pressNotrButton)
        
        self.downButton = QPushButton("", self)
        self.downButton.setGeometry(880, 140, 50, 50)
        self.downButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray; color : black}")
        self.downButton.setIcon(QIcon('images\DIRRWD.png'))
        self.downButton.setCursor(Qt.PointingHandCursor)
        self.downButton.clicked.connect(self.pressDownButton)


        self.frenLabel = QLabel("   Direkt\nFren Valfi", self)
        self.frenLabel.setGeometry(784, 220, 60, 30)
        self.frenLabel.setStyleSheet("QLabel{color : white;}")

        self.scrollFren = QScrollBar(self)
        self.scrollFren.setGeometry(780, 260, 55, 120)
        self.scrollFren.setStyleSheet(  "QScrollBar{background : #a89383; border : 2px solid gray}"
                                        "QScrollBar::handle{background : #483c32; border-radius : 25; min-width: 50px; min-height: 60px;}"
                                        "QScrollBar::handle::pressed{background : #332d28;}")
        self.scrollFren.setCursor(Qt.PointingHandCursor)
        self.scrollFren.setValue(60)
        self.scrollFren.valueChanged.connect(lambda: self.frenScrollAction())

        self.kornaLabel = QLabel("Havalı Korna\n  Anahtarı", self)
        self.kornaLabel.setGeometry(780, 400, 80, 30)
        self.kornaLabel.setStyleSheet("QLabel{color : white;}")

        self.scrollKorna = QScrollBar(self)
        self.scrollKorna.setGeometry(786, 440, 40, 100)
        self.scrollKorna.setStyleSheet( "QScrollBar{background : #a89383; border : 2px solid gray}"
                                        "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                        "QScrollBar::handle::pressed{background : #332d28;}")
        self.scrollKorna.setCursor(Qt.PointingHandCursor)
        self.scrollKorna.setValue(50)

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
        self.pantoScroll.setValue(50)
        self.pantoScroll.valueChanged.connect(lambda: self.pantoScrollAction())


        self.mcbLabel = QLabel("   MCB\nAnahtarı", self)
        self.mcbLabel.setGeometry(149, 85, 70, 60)
        self.mcbLabel.setStyleSheet("QLabel{color : white;}")

        self.mcbScroll = QScrollBar(self)
        self.mcbScroll.setGeometry(150, 140, 40, 100)
        self.mcbScroll.setStyleSheet("QScrollBar{background : #a89383; border : 2px solid gray}"
                                     "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                     "QScrollBar::handle::pressed{background : #332d28;}")
        self.mcbScroll.setCursor(Qt.PointingHandCursor)
        self.mcbScroll.setValue(50)
        self.mcbScroll.valueChanged.connect(lambda: self.mcbScrollAction())

        self.freeErtmsLabel = QLabel(" ERTMS\nSerbest\nBırakma", self)
        self.freeErtmsLabel.setGeometry(91, 250, 70, 60)
        self.freeErtmsLabel.setStyleSheet("QLabel{color : white;}")

        self.freeErtmsScroll = QScrollBar(self)
        self.freeErtmsScroll.setGeometry(90, 310, 40, 100)
        self.freeErtmsScroll.setStyleSheet("QScrollBar{background : #a89383; border : 2px solid gray}"
                                     "QScrollBar::handle{background : #483c32; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                     "QScrollBar::handle::pressed{background : #332d28;}")
        self.freeErtmsScroll.setCursor(Qt.PointingHandCursor)
        self.freeErtmsScroll.setValue(50)

        self.takenErtmsLabel = QLabel("ERTMS\n Alındı\nBildirimi", self)
        self.takenErtmsLabel.setGeometry(152, 250, 70, 60)
        self.takenErtmsLabel.setStyleSheet("QLabel{color : white;}")

        self.takenErtmsScroll = QScrollBar(self)
        self.takenErtmsScroll.setGeometry(150, 310, 40, 100)
        self.takenErtmsScroll.setStyleSheet("QScrollBar{background : #a89383; border : 2px solid gray}"
                                     "QScrollBar::handle{background : #fcca12; border-radius : 15; min-width: 50px; min-height: 45px;}"
                                     "QScrollBar::handle::pressed{background : #332d28;}")
        self.takenErtmsScroll.setCursor(Qt.PointingHandCursor)
        self.takenErtmsScroll.setValue(50)

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

    def createImages(self):

        # icon-61.png    icon-62.png
        self.icon61Label = QLabel(self)
        self.icon61 = QPixmap('images\icon-61.png')
        self.icon61Label.setPixmap(self.icon61)
        self.icon61Label.setGeometry(55, 140, self.icon61.width(), self.icon61.height())

        self.icon62Label = QLabel(self)
        self.icon62 = QPixmap('images\icon-62.png')
        self.icon62Label.setPixmap(self.icon62)
        self.icon62Label.setGeometry(55, 215, self.icon62.width(), self.icon62.height())


        # MCBStateClose.png   MCBStateOpen.png
        self.MCBOpenLabel = QLabel(self)
        self.iconMCBOpen = QPixmap('images\MCBStateClose.png')
        self.MCBOpenLabel.setPixmap(self.iconMCBOpen)
        self.MCBOpenLabel.setGeometry(200, 140, self.iconMCBOpen.width(), self.iconMCBOpen.height())

        self.MCBCloseLabel = QLabel(self)
        self.iconMCBClose = QPixmap('images\MCBStateOpen.png')
        self.MCBCloseLabel.setPixmap(self.iconMCBClose)
        self.MCBCloseLabel.setGeometry(200, 210, self.iconMCBClose.width(), self.iconMCBClose.height())

        # SANDON.png
        self.sandonLabel = QLabel(self)
        self.iconSandon = QPixmap('images\SANDON.png')
        self.sandonLabel.setPixmap(self.iconSandon)
        self.sandonLabel.setGeometry(380, 120, self.iconSandon.width(), self.iconSandon.height())


        # BRR.png
        self.BRRLabel = QLabel(self)
        self.iconBRR = QPixmap('images\BRR.png')
        self.BRRLabel.setPixmap(self.iconBRR)
        self.BRRLabel.setGeometry(470, 120, self.iconBRR.width(), self.iconBRR.height())


        # icon-66.png   icon-67.png   icon-68.png
        self.icon66Label = QLabel(self)
        self.icon66 = QPixmap('images\icon-66.png')
        self.icon66Label.setPixmap(self.icon66)
        self.icon66Label.setGeometry(565, 80, self.icon66.width(), self.icon66.height())

        self.icon67Label = QLabel(self)
        self.icon67 = QPixmap('images\icon-67.png')
        self.icon67Label.setPixmap(self.icon67)
        self.icon67Label.setGeometry(565, 110, self.icon67.width(), self.icon67.height())

        self.icon68Label= QLabel(self)
        self.icon68 = QPixmap('images\icon-68.png')
        self.icon68Label.setPixmap(self.icon68)
        self.icon68Label.setGeometry(565, 140, self.icon68.width(), self.icon68.height())


        # BRR.png  BRACT.png
        self.BRRLabel2 = QLabel(self)
        self.BRRLabel2.setPixmap(self.iconBRR)
        self.BRRLabel2.setGeometry(745, 270, self.iconBRR.width(), self.iconBRR.height())

        self.bractLabel = QLabel(self)
        self.iconBRACT = QPixmap('images\BRACT.png')
        self.bractLabel.setPixmap(self.iconBRACT)
        self.bractLabel.setGeometry(745, 340, self.iconBRACT.width(), self.iconBRACT.height())

    def pressUpButton(self):
        self.upButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : #734a12;color : black}")
        self.downButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        self.notrButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        
        msg = '{"btnValue" : "1"}'
        self.client.connect(self.broker, 1883)
        self.client.publish(topic=self.topic, payload=msg)
        print("press up button")

    def pressDownButton(self):
        self.notrButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        self.downButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : #734a12;color : black}")
        self.upButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        
        msg = '{"btnValue" : "-1"}'
        self.client.connect(self.broker, 1883)
        self.client.publish(topic=self.topic, payload=msg)
        print("press down button")
    
    def pressNotrButton(self):
        self.notrButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : #734a12;color : black}")
        self.downButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        self.upButton.setStyleSheet("QPushButton{border-radius : 25; border : 3px solid white; background-color : gray;color : black}")
        
        msg = '{"btnValue" : "0"}'
        self.client.connect(self.broker, 1883)
        self.client.publish(topic=self.topic, payload=msg)
        print("press notr button")

    def pantoScrollAction(self):
        value = self.pantoScroll.value()
        if value == 0 or value == 99:
            msg = '{"pantoScroll" : "' + str(value) + '"}'
            # print(msg)
            self.client.connect(self.broker, 1883)
            self.client.publish(topic=self.topic, payload=msg)
            print("panto scroll new value : ", value)
        
    def frenScrollAction(self):
        value = self.scrollFren.value()
        if value == 0 or value == 99:
            msg = '{"frenScroll" : "' + str(value) + '"}'

            self.client.connect(self.broker, 1883)
            self.client.publish(topic=self.topic, payload=msg)
            print("fren scroll new value : ", value)
    
    def mcbScrollAction(self):
        value = self.mcbScroll.value()
        if value == 0 or value == 99:
            msg = '{"mcbScroll" : "' + str(value) + '"}'

            self.client.connect(self.broker, 1883)
            self.client.publish(topic=self.topic, payload=msg)
            print("mcb scroll new value : ", value)

    def sendData(self):
        randAngleValue = random.randint(0, 25)
        threadMsg = '{"gaugeMeterAngle" : "'+ str(randAngleValue) +'}'

        self.client.connect(self.broker, 1883)
        self.client.publish(topic=self.topic, payload=threadMsg)

        print(str(threadMsg))

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()