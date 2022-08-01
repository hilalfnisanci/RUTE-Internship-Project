from threading import Thread
from venv import create
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
import createBar
from mqttEvents import Mqtt

class CreateDu1(QWidget):
    
    def __init__(self, parent=None):
        super(CreateDu1, self).__init__(parent)
        self.du1Grid = QGridLayout()
        self.createDownButtons()
        self.createLeftButtons()
        self.createUpButtons()
        self.createRightButtons()
        self.createInsideButtons()
        self.createBarsfromImages()
    
    def createDownButtons(self):
        
        # alt butonlar
        self.pushButton1 = QPushButton("1", self)
        self.pushButton1.setGeometry(100, 540, 60, 60)
        self.pushButton1.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton("2", self)
        self.pushButton2.setGeometry(170, 540, 60, 60)
        self.pushButton2.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton("3", self)
        self.pushButton3.setGeometry(240, 540, 60, 60)
        self.pushButton3.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton3)

        self.pushButton4 = QPushButton("4", self)
        self.pushButton4.setGeometry(310, 540, 60, 60)
        self.pushButton4.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton4)

        self.pushButton5 = QPushButton("5", self)
        self.pushButton5.setGeometry(380, 540, 60, 60)
        self.pushButton5.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton5)

        self.pushButton6 = QPushButton("6", self)
        self.pushButton6.setGeometry(450, 540, 60, 60)
        self.pushButton6.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton6)

        self.pushButton7 = QPushButton("7", self)
        self.pushButton7.setGeometry(520, 540, 60, 60)
        self.pushButton7.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton7)

        self.pushButton8 = QPushButton("8", self)
        self.pushButton8.setGeometry(590, 540, 60, 60)
        self.pushButton8.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton8)

        self.pushButton9 = QPushButton("9", self)
        self.pushButton9.setGeometry(660, 540, 60, 60)
        self.pushButton9.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton9)

        self.pushButton10 = QPushButton("10", self)
        self.pushButton10.setGeometry(730, 540, 60, 60)
        self.pushButton10.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButton10)
    
    def createUpButtons(self):

        # üst butonlar
        self.pushButtonOpen = QPushButton("Open", self)
        self.pushButtonOpen.setGeometry(100, 20, 60, 60)
        self.pushButtonOpen.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        # self.pushButtonOpen.clicked.connect(self.pub)
        self.du1Grid.addWidget(self.pushButtonOpen)

        self.pushButtonFlag = QPushButton("Flag", self)
        self.pushButtonFlag.setGeometry(170, 20, 60, 60)
        self.pushButtonFlag.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonFlag)

        self.pushButtoni = QPushButton("i", self)
        self.pushButtoni.setGeometry(240, 20, 60, 60)
        self.pushButtoni.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtoni)

        self.pushButtonInfo = QPushButton("Info", self)
        self.pushButtonInfo.setGeometry(310, 20, 60, 60)
        self.pushButtonInfo.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonInfo)

        self.pushButtonFault = QPushButton("Fault", self)
        self.pushButtonFault.setGeometry(380, 20, 60, 60)
        self.pushButtonFault.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonFault)

        self.pushButtonV0 = QPushButton("V=0", self)
        self.pushButtonV0.setGeometry(450, 20, 60, 60)
        self.pushButtonV0.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonV0)

        self.pushButtonV1 = QPushButton("V>0", self)
        self.pushButtonV1.setGeometry(520, 20, 60, 60)
        self.pushButtonV1.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonV1)

        self.pushButtonBrightness = QPushButton("*", self)
        self.pushButtonBrightness.setGeometry(590, 20, 60, 60)
        self.pushButtonBrightness.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonBrightness)

        self.pushButtonDayNight = QPushButton("Day/Night", self)
        self.pushButtonDayNight.setGeometry(660, 20, 60, 60)
        self.pushButtonDayNight.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonDayNight)

        self.pushButtonChange = QPushButton("<->", self)
        self.pushButtonChange.setGeometry(730, 20, 60, 60)
        self.pushButtonChange.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonChange)

    def createLeftButtons(self):

        # sol butonlar oluşturulur
        self.pushButtonF1 = QPushButton("F1", self)
        self.pushButtonF1.setGeometry(20, 110, 60, 60)
        self.pushButtonF1.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonF1)

        self.pushButtonF2 = QPushButton("F2", self)
        self.pushButtonF2.setGeometry(20, 180, 60, 60)
        self.pushButtonF2.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonF2)

        self.pushButtonF3 = QPushButton("F3", self)
        self.pushButtonF3.setGeometry(20, 250, 60, 60)
        self.pushButtonF3.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonF3)

        self.pushButtonF4 = QPushButton("F4", self)
        self.pushButtonF4.setGeometry(20, 320, 60, 60)
        self.pushButtonF4.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonF4)

        self.pushButtonF5 = QPushButton("F5", self)
        self.pushButtonF5.setGeometry(20, 390, 60, 60)
        self.pushButtonF5.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonF5)

        self.pushButtonF6 = QPushButton("F6", self)
        self.pushButtonF6.setGeometry(20, 460, 60, 60)
        self.pushButtonF6.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonF6)

    def createRightButtons(self):

        # sağ butonlar
        self.pushButtonC = QPushButton("C", self)
        self.pushButtonC.setGeometry(810, 110, 60, 60)
        self.pushButtonC.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonC)

        self.pushButtonLeft = QPushButton("<-", self)
        self.pushButtonLeft.setGeometry(810, 180, 60, 60)
        self.pushButtonLeft.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonLeft)

        self.pushButtonRight = QPushButton("⯈", self)
        self.pushButtonRight.setGeometry(810, 250, 60, 60)
        self.pushButtonRight.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonRight)

        self.pushButtonUp = QPushButton("up", self)
        self.pushButtonUp.setGeometry(810, 320, 60, 60)
        self.pushButtonUp.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonUp)

        self.pushButtonDown = QPushButton("down", self)
        self.pushButtonDown.setGeometry(810, 390, 60, 60)
        self.pushButtonDown.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonDown)

        self.pushButtonE = QPushButton("E", self)
        self.pushButtonE.setGeometry(810, 460, 60, 60)
        self.pushButtonE.setStyleSheet("QPushButton{border-radius : 15; border : 1px solid white;background-color : #3A3535;color : white}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonE)

    def createInsideButtons(self):
        # create G button
        self.pushButtonG = QPushButton("", self)
        self.pushButtonG.setGeometry(100, 370, 69, 50)
        self.pushButtonG.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.pushButtonG.setIcon(QIcon("images\BRKMDG.png"))
        self.pushButtonG.setIconSize(QSize(69, 48))
        self.du1Grid.addWidget(self.pushButtonG)

        self.pushButtonkV = QPushButton("", self)
        self.pushButtonkV.setGeometry(100, 420, 69, 50)
        self.pushButtonkV.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.pushButtonkV.setIcon(QIcon("images\SYSTR.png"))
        self.pushButtonkV.setIconSize(QSize(69, 48))
        self.du1Grid.addWidget(self.pushButtonkV)


        self.pushButtonStspan = QPushButton("",self)
        self.pushButtonStspan.setGeometry(169, 420, 69, 50)
        self.pushButtonStspan.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.pushButtonStspan.setIcon(QIcon("images\STSPAN.png"))
        self.pushButtonStspan.setIconSize(QSize(69, 48))
        self.du1Grid.addWidget(self.pushButtonStspan)


        # create system button
        self.pushButtonSystem = QPushButton("Sistem", self)
        self.pushButtonSystem.setGeometry(100, 470, 69, 50)
        self.pushButtonSystem.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonSystem)


        # create case (durum) button
        self.pushButtonCase = QPushButton("Durum", self)
        self.pushButtonCase.setGeometry(169, 470, 69, 50)
        self.pushButtonCase.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonCase)


        # create care button
        self.pushButtonCare = QPushButton("Bakım", self)
        self.pushButtonCare.setGeometry(238, 470, 69, 50)
        self.pushButtonCare.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonCare)


        # create backup button
        self.pushButtonBackup = QPushButton("Yedek", self)
        self.pushButtonBackup.setGeometry(307, 470, 69, 50)
        self.pushButtonBackup.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonBackup)

        self.btntraction = QPushButton(self)
        self.btntraction.setGeometry(376, 470, 69, 50)
        self.btntraction.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.btntraction.setIcon(QIcon("images\TractionInterlockOK.png"))
        self.btntraction.setIconSize(QSize(69, 48))
        self.du1Grid.addWidget(self.btntraction)
        
        self.btnMenuBrk = QPushButton(self)
        self.btnMenuBrk.setGeometry(445, 470, 69, 50)
        self.btnMenuBrk.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.btnMenuBrk.setIcon(QIcon("images\MENUBRK.png"))
        self.btnMenuBrk.setIconSize(QSize(69, 48))
        self.du1Grid.addWidget(self.btnMenuBrk)

        self.btnDIR = QPushButton(self)
        self.btnDIR.setGeometry(514, 420, 69, 50)
        self.btnDIR.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.btnDIR.setIcon(QIcon("images\DBRAPL.png"))
        self.btnDIR.setIconSize(QSize(69, 48))
        self.du1Grid.addWidget(self.btnDIR)


        self.btnCabdeac = QPushButton(self)
        self.btnCabdeac.setGeometry(731, 101, 58, 52)
        self.btnCabdeac.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.btnCabdeac.setIcon(QIcon("images\CABDEAC.png"))
        self.btnCabdeac.setIconSize(QSize(58, 52))
        self.du1Grid.addWidget(self.btnCabdeac)


        # TRLNOFF.png
        self.btnTrlnoff = QPushButton(self)
        self.btnTrlnoff.setGeometry(731, 154, 58, 52)
        self.btnTrlnoff.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.btnTrlnoff.setIcon(QIcon("images\TRLNOFF.png"))
        self.btnTrlnoff.setIconSize(QSize(58,52))
        self.du1Grid.addWidget(self.btnTrlnoff)


        # DIRFWD.png
        self.btnDırfwd = QPushButton(self)
        self.btnDırfwd.setGeometry(731, 208, 58, 52)
        self.btnDırfwd.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.btnDırfwd.setIcon(QIcon("images\DIRFWD.png"))
        self.btnDırfwd.setIconSize(QSize(58, 52))
        self.du1Grid.addWidget(self.btnDırfwd)


        # create key-brake button
        self.pushButtonKey = QPushButton("Anahtar/Fren", self)
        self.pushButtonKey.setGeometry(583, 470, 69, 50)
        self.pushButtonKey.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonKey)

        # create office button
        self.pushButtonOffice = QPushButton("Atölye", self)
        self.pushButtonOffice.setGeometry(652, 470, 69, 50)
        self.pushButtonOffice.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonOffice)

        # create mode pull button
        self.pushButtonPull = QPushButton("Çekme Modu", self)
        self.pushButtonPull.setGeometry(721, 470, 69, 50)
        self.pushButtonPull.setStyleSheet("QPushButton{color : white; background-color : transparent;}QPushButton::pressed{background-color : gray;}")
        self.du1Grid.addWidget(self.pushButtonPull)

    def UiComponents(self):
        self.bar1 = QProgressBar(self)
        self.bar1.setGeometry(140, 120, 35, 200)
        self.bar1.setValue(70)
        self.bar1.setAlignment(Qt.AlignCenter)
        self.bar1.setOrientation(Qt.Vertical) # default olarak yatay ama orientation ile dikey yapılır
        self.bar1.setStyleSheet("QProgressBar"
                          "{"
                          "border: solid white;"
                          "border-radius: 5px;"
                          "color: white; "
                          "}"
                          "QProgressBar::chunk "
                          "{background-color: blue;"
                          "border-radius :5px;"
                          "}")
        self.bar1.setTextVisible(False)
        self.du1Grid.addWidget(self.bar1)

    # çizim işlemleri gerçekleştirilir
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
        
        # sol üst parçayı iki parçaya bölen kısım
        painter.drawLine(275, 100, 275, 370)
        
        # sağ taraftaki küçük 5 tane kutu çizilir
        painter.drawLine(730, 100, 730, 370)
        painter.drawLine(730, 154, 790, 154)
        painter.drawLine(730, 208, 790, 208)
        painter.drawLine(730, 262, 790, 262)
        painter.drawLine(730, 316, 790, 316)
        
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

        # 28, 250, 50
        """dataValue = mqtt.sendData(barName="kV")
        print("kontrol: ", mqtt.sendData(barName="kV"))"""
        
        
        # print(pv, "  -  ", type(pv))   Mqtt.takeData(barName='kV')    Mqtt.takeData(barName='A')
        createBar.CreateBar().paintEvent(painter=painter, barName="kV", page="du1", progressValue = Mqtt.takeData(barName='kV'))

        createBar.CreateBar().paintEvent(painter=painter, barName="A", page="du1", progressValue= Mqtt.takeData(barName='A'))

        createBar.CreateBar().paintEvent(painter=painter, barName="kN", page="du1", progressValue=Mqtt.takeData(barName='kN'))

        createBar.CreateBar().paintEvent(painter=painter, barName='brakeBar1', page='du1', progressValue=Mqtt.takeData(barName='brakeBar1'))
    
        t1 = Thread(target=self.update())
        t1.start()

        self.dateTime = QDateTime.currentDateTime()
        painter.drawText(550, 400, self.dateTime.toString())

        painter.end()

    def createBarsfromImages(self):

        """# kN bar  left - 300 , Right - 100
        self.label1 = QLabel(self)
        self.pixmap1 = QPixmap('images\TrDynBrakeBarV1.png')
        self.label1.setPixmap(self.pixmap1)
        self.label1.setGeometry(280, 120, self.pixmap1.width(), self.pixmap1.height())"""

        #YelArrow.png
        self.arrowLabel = QLabel(self)
        self.icon = QPixmap('images\YelArrow.png')
        self.arrowLabel.setPixmap(self.icon)
        self.arrowLabel.setGeometry(375, 334, self.icon.width(), self.icon.height())
        self.arrowLabel.resize(20, 10)

        # FS  2 bar left 6,0  Right 6
        """self.label2 = QLabel(self)
        self.pixmap2 = QPixmap('images\BrakePipePressV1.png')
        self.label2.setPixmap(self.pixmap2)
        self.label2.setGeometry(450, 102, self.pixmap2.width(), self.pixmap2.height())"""
        
        #YelArrow.png
        self.arrowLabel2 = QLabel(self)
        self.arrowLabel2.setPixmap(self.icon)
        self.arrowLabel2.setGeometry(545, 125, self.icon.width(), self.icon.height())
        self.arrowLabel2.resize(20, 10)

        self.label3 = QLabel(self)
        self.pixmap3 = QPixmap('images\BPPT.png')
        self.label3.setPixmap(self.pixmap3)
        self.label3.setGeometry(508, 330, self.pixmap3.width(), self.pixmap3.height())

        #BCPT.png
        self.label4 = QLabel(self)
        self.pixmap4 = QPixmap("images\BCPT.png")
        self.label4.setPixmap(self.pixmap4)
        self.label4.setGeometry(620, 335, self.pixmap4.width(), self.pixmap4.height())
        