from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from analoggaugewidget import AnalogGaugeWidget
import createBar
from mqttEvents import Mqtt
from threading import Thread

class CreateDu2(QWidget):
    def __init__(self, parent=None):
        super(CreateDu2, self).__init__(parent)
        self.du2Grid = QGridLayout()

        self.createLeftButtons()
        self.createRightButtons()
        self.createDownButtons()
        self.createUpButtons()
        self.createGaugeMeter()
        self.createInsideButtons()
        self.createImages()

     # aşağıda yer alan butonlar için fonksiyon oluşturulur
    def createDownButtons(self):
        
        # alt butonlar
        self.pushButton1 = QPushButton("1", self)
        self.pushButton1.setGeometry(100, 540, 60, 60)
        self.pushButton1.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton("2", self)
        self.pushButton2.setGeometry(170, 540, 60, 60)
        self.pushButton2.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton("3", self)
        self.pushButton3.setGeometry(240, 540, 60, 60)
        self.pushButton3.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton3)

        self.pushButton4 = QPushButton("4", self)
        self.pushButton4.setGeometry(310, 540, 60, 60)
        self.pushButton4.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton4)

        self.pushButton5 = QPushButton("5", self)
        self.pushButton5.setGeometry(380, 540, 60, 60)
        self.pushButton5.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton5)

        self.pushButton6 = QPushButton("6", self)
        self.pushButton6.setGeometry(450, 540, 60, 60)
        self.pushButton6.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton6)

        self.pushButton7 = QPushButton("7", self)
        self.pushButton7.setGeometry(520, 540, 60, 60)
        self.pushButton7.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton7)

        self.pushButton8 = QPushButton("8", self)
        self.pushButton8.setGeometry(590, 540, 60, 60)
        self.pushButton8.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton8)

        self.pushButton9 = QPushButton("9", self)
        self.pushButton9.setGeometry(660, 540, 60, 60)
        self.pushButton9.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton9)

        self.pushButton10 = QPushButton("10", self)
        self.pushButton10.setGeometry(730, 540, 60, 60)
        self.pushButton10.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButton10)

    # yukarıda yer alan butonlar için fonksiyon oluşturulur
    def createUpButtons(self):

        # üst butonlar
        self.pushButtonOpen = QPushButton("Open", self)
        self.pushButtonOpen.setGeometry(100, 20, 60, 60)
        self.pushButtonOpen.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonOpen)

        self.pushButtonFlag = QPushButton("Flag", self)
        self.pushButtonFlag.setGeometry(170, 20, 60, 60)
        self.pushButtonFlag.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonFlag)

        self.pushButtoni = QPushButton("i", self)
        self.pushButtoni.setGeometry(240, 20, 60, 60)
        self.pushButtoni.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtoni)

        self.pushButtonInfo = QPushButton("Info", self)
        self.pushButtonInfo.setGeometry(310, 20, 60, 60)
        self.pushButtonInfo.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonInfo)

        self.pushButtonFault = QPushButton("Fault", self)
        self.pushButtonFault.setGeometry(380, 20, 60, 60)
        self.pushButtonFault.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonFault)

        self.pushButtonV0 = QPushButton("V=0", self)
        self.pushButtonV0.setGeometry(450, 20, 60, 60)
        self.pushButtonV0.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonV0)

        self.pushButtonV1 = QPushButton("V>0", self)
        self.pushButtonV1.setGeometry(520, 20, 60, 60)
        self.pushButtonV1.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonV1)

        self.pushButtonBrightness = QPushButton("*", self)
        self.pushButtonBrightness.setGeometry(590, 20, 60, 60)
        self.pushButtonBrightness.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonBrightness)

        self.pushButtonDayNight = QPushButton("Day/Night", self)
        self.pushButtonDayNight.setGeometry(660, 20, 60, 60)
        self.pushButtonDayNight.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonDayNight)

        self.pushButtonChange = QPushButton("<->", self)
        self.pushButtonChange.setGeometry(730, 20, 60, 60)
        self.pushButtonChange.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonChange)

    # sol tarafta yer alan butonlar için fonksiyon oluşturulur
    def createLeftButtons(self):

        # sol butonlar oluşturulur
        self.pushButtonF1 = QPushButton("F1", self)
        self.pushButtonF1.setGeometry(20, 110, 60, 60)
        self.pushButtonF1.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonF1)

        self.pushButtonF2 = QPushButton("F2", self)
        self.pushButtonF2.setGeometry(20, 180, 60, 60)
        self.pushButtonF2.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonF2)

        self.pushButtonF3 = QPushButton("F3", self)
        self.pushButtonF3.setGeometry(20, 250, 60, 60)
        self.pushButtonF3.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonF3)

        self.pushButtonF4 = QPushButton("F4", self)
        self.pushButtonF4.setGeometry(20, 320, 60, 60)
        self.pushButtonF4.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonF4)

        self.pushButtonF5 = QPushButton("F5", self)
        self.pushButtonF5.setGeometry(20, 390, 60, 60)
        self.pushButtonF5.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonF5)

        self.pushButtonF6 = QPushButton("F6", self)
        self.pushButtonF6.setGeometry(20, 460, 60, 60)
        self.pushButtonF6.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonF6)

    # sağ tarafta yer alan butonlar için fonksiyon oluşturulur
    def createRightButtons(self):

        # sağ butonlar
        self.pushButtonC = QPushButton("C", self)
        self.pushButtonC.setGeometry(810, 110, 60, 60)
        self.pushButtonC.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonC)

        self.pushButtonLeft = QPushButton("<-", self)
        self.pushButtonLeft.setGeometry(810, 180, 60, 60)
        self.pushButtonLeft.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonLeft)

        self.pushButtonRight = QPushButton("⯈", self)
        self.pushButtonRight.setGeometry(810, 250, 60, 60)
        self.pushButtonRight.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonRight)

        self.pushButtonUp = QPushButton("up", self)
        self.pushButtonUp.setGeometry(810, 320, 60, 60)
        self.pushButtonUp.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonUp)

        self.pushButtonDown = QPushButton("down", self)
        self.pushButtonDown.setGeometry(810, 390, 60, 60)
        self.pushButtonDown.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonDown)

        self.pushButtonE = QPushButton("E", self)
        self.pushButtonE.setGeometry(810, 460, 60, 60)
        self.pushButtonE.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonE)

    def createInsideButtons(self):
        # create G button
        self.pushButtonG = QPushButton("", self)
        self.pushButtonG.setGeometry(100, 370, 69, 50)
        self.pushButtonG.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.pushButtonG.setIcon(QIcon("images\BRKMDG.png"))
        self.pushButtonG.setIconSize(QSize(69, 48))
        self.du2Grid.addWidget(self.pushButtonG)

        # create system button
        self.pushButtonCCTV = QPushButton("CCTV", self)
        self.pushButtonCCTV.setGeometry(100, 470, 69, 50)
        self.pushButtonCCTV.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonCCTV)

        # create case (durum) button
        self.pushButtonShow = QPushButton("Göster", self)
        self.pushButtonShow.setGeometry(169, 470, 69, 50)
        self.pushButtonShow.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonShow)

        # create key-brake button
        self.pushButtonCare = QPushButton("Bakım", self)
        self.pushButtonCare.setGeometry(583, 470, 69, 50)
        self.pushButtonCare.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonCare)

        # create office button
        self.pushButtonBackup = QPushButton("Yedek", self)
        self.pushButtonBackup.setGeometry(652, 470, 69, 50)
        self.pushButtonBackup.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du2Grid.addWidget(self.pushButtonBackup)
        

        self.pushButtonStspan = QPushButton("",self)
        self.pushButtonStspan.setGeometry(169, 420, 69, 50)
        self.pushButtonStspan.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        """self.pushButtonStspan.setIcon(QIcon("images\STSPAN.png"))
        self.pushButtonStspan.setIconSize(QSize(69, 48))"""
        self.du2Grid.addWidget(self.pushButtonStspan)


        self.btnDIR = QPushButton(self)
        self.btnDIR.setGeometry(514, 420, 69, 50)
        self.btnDIR.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        """self.btnDIR.setIcon(QIcon("images\DBRAPL.png"))
        self.btnDIR.setIconSize(QSize(69, 48))"""
        self.du2Grid.addWidget(self.btnDIR)


    def createGaugeMeter(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(110, 110, 250, 250)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame = QFrame()
        self.frame.setObjectName("frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = AnalogGaugeWidget(self.frame)

        self.widget.setMinimumSize(QSize(200, 200))
        self.widget.setMaximumSize(QSize(400, 400))
        self.widget.setBaseSize(QSize(200, 200))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.frame)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.white, 2, Qt.SolidLine))

        # merkezdeki ana dörtgen, her şeyi içine alan kısım
        painter.drawRect(100, 100, 690, 420)
        
        # ana dörtgeni ortadan ikiye bölen kısım
        painter.drawLine(445, 100, 445, 520)
        
        # ana dörtgeni alt-üst olarak iki parçaya bölen kısım
        painter.drawLine(100, 370, 790, 370)
        
        # alt parça yapılır
        painter.drawLine(100, 470, 790, 470)
        painter.drawLine(100, 420, 790, 420)
        painter.drawLine(169, 370, 169, 520)
        painter.drawLine(238, 370, 238, 520)
        painter.drawLine(307, 370, 307, 520)
        painter.drawLine(376, 370, 376, 520)
        painter.drawLine(514, 420, 514, 520)
        painter.drawLine(583, 420, 583, 520)
        painter.drawLine(652, 420, 652, 520)
        painter.drawLine(721, 420, 721, 520)


        # pv = Mqtt.takeData(barName='kV')
        # print(pv, "  -  ", type(pv))    Mqtt.takeData(barName='kV')    Mqtt.takeData(barName='A')

        createBar.CreateBar().paintEvent(painter=painter, barName="kV", page="du2", progressValue = Mqtt.takeData(barName='kV'))
        createBar.CreateBar().paintEvent(painter=painter, barName="A", page="du2", progressValue = Mqtt.takeData(barName='A'))
        createBar.CreateBar().paintEvent(painter=painter, barName="kN/FM", page="du2", progressValue= Mqtt.takeData(barName='kN/FM'))
        createBar.CreateBar().paintEvent(painter=painter, barName="BatV", page="du2", progressValue=Mqtt.takeData(barName='BatV'))

        t1 = Thread(target=self.update())
        t1.start()

        self.createScrollImg()

        self.dateTime = QDateTime.currentDateTime()
        painter.drawText(550, 400, self.dateTime.toString())

        painter.end()


    def createImages(self):

        #YelArrow.png
        self.arrowLabel = QLabel(self)
        self.icon = QPixmap('images\YelArrow.png')
        self.arrowLabel.setPixmap(self.icon)
        self.arrowLabel.setGeometry(675, 345, self.icon.width(), self.icon.height())
        self.arrowLabel.resize(20, 10)

    def createScrollImg(self):

        if "pantoScroll" in Mqtt.scrollDict.keys():
            if 99 == Mqtt.scrollDict["pantoScroll"]:
                self.pushButtonStspan.setIcon(QIcon("images\PANTODR.png"))
                self.pushButtonStspan.setIconSize(QSize(69, 48))
            elif 0 == Mqtt.scrollDict["pantoScroll"]:
                self.pushButtonStspan.setIcon(QIcon("images\PANTOUP.png"))
                self.pushButtonStspan.setIconSize(QSize(69, 48))

        if "frenScroll" in Mqtt.scrollDict.keys():
            if 99 == Mqtt.scrollDict["frenScroll"]:
                self.btnDIR.setIcon(QIcon("images\BRACT2.png"))
                self.btnDIR.setIconSize(QSize(69, 48))
            if 0 == Mqtt.scrollDict["frenScroll"]:
                self.btnDIR.setIcon(QIcon("images\BRR2.png"))
                self.btnDIR.setIconSize(QSize(69, 48))