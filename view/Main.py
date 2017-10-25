from PyQt5.QtWidgets import QWidget,QApplication ,  QLabel, QGridLayout
from PyQt5.QtGui import QFont,QPicture,QPalette,QPixmap
from PyQt5.QtCore import Qt,QSize
import sys
import controller.FingerEvent
import util.NormalUtils
class MainWindow(QWidget):
    data = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    count = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("QLabel{color:rgb(100,100,100,250);font-size:40px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(100,100,100,120);}")
        self.setWindowTitle("2048小游戏")
        self.resize(500,500)
        self.focusPolicy()
        self.font = QFont()
        self.fingerEvent = controller.FingerEvent.FingerEvent()
        self.pxmap = QPixmap()
        self.initUi()
        # util.NormalUtils.printlist(self.data)

    def initUi(self):
        mainlayout = QGridLayout()
        self.setLayout(mainlayout)
        self.lbs = []
        pos = [(i, j) for i in range(0, 4) for j in range(0, 4)]
        for position in zip(pos):
            lb = QLabel()
            qf = QFont()
            qf.setPixelSize(50)
            qf.setBold(True)
            lb.setAlignment(Qt.AlignCenter)
            lb.setFont(qf)
            lb.setAutoFillBackground(True)
            qp = QPalette()
            qp.setColor(QPalette.Window,Qt.darkBlue)
            lb.setPalette(qp)
            lb.setMinimumHeight(100)
            lb.setMaximumHeight(100)
            lb.setMaximumWidth(100)
            lb.setMinimumWidth(100)
            self.pxmap.load("../res/0.png")

            qs = QSize(100, 100)
            print(lb.height(), lb.width())
            lb.setPixmap(self.pxmap.scaled(qs))
            self.lbs.append(lb)
            mainlayout.addWidget(lb,*position[0])




    def keyPressEvent(self,event):
        try:
            if(event.key() == Qt.Key_Up):#up
                self.data = self.fingerEvent.fingerup(self.data)
                self.setdatasource()
                # print(event.key,"up")
            if(event.key() == Qt.Key_Down):#down
                self.data = self.fingerEvent.fingerdown(self.data)
                self.setdatasource()
                # print(event.key, "down")
            if (event.key() == Qt.Key_Left):#left
                self.data = self.fingerEvent.fingerleft(self.data)
                self.setdatasource()
                # print(event.key, "left")
            if (event.key() == Qt.Key_Right):#right
                self.data = self.fingerEvent.fingerright(self.data)
                self.setdatasource()
            del event
        except Exception as e:
            print(e.__str__())
        # util.NormalUtils.printlist(self.data)
        # print(event.text())

    def setdatasource(self):
        pos = 0
        for i in range(0, 4):
            for j in range(0, 4):

                if self.data[i][j] < 128:
                    self.pxmap.load("../res/"+str(self.data[i][j])+".png")
                    qs = QSize(100, 100)
                    self.lbs[pos].setPixmap(self.pxmap.scaled(qs))
                else:
                    self.lbs[pos].setText(str(self.data[i][j]))
                pos = pos+1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())