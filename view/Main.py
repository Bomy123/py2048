from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QPixmap,QIcon
from PyQt5.QtCore import Qt, QSize
from util import RWFile
import sys
import controller.FingerEvent


class MainWindow(QWidget):
    data = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("QLabel{color:rgb(100,100,100,250);font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(100,100,100,120);}")
        self.setWindowTitle("2048小游戏")
        self.resize(500, 500)
        self.focusPolicy()
        self.setWindowIcon(QIcon("../res/icon.jpg"))
        self.font = QFont()
        self.fingerEvent = controller.FingerEvent.FingerEvent()
        self.pxmap = QPixmap()
        self.rdfile = RWFile.RWFile()
        self.cachefile = "../cache/2048.2048"
        self.rdfile.cleanfile(self.cachefile)
        self.initUi()
        QMessageBox.about(self, "About Py2048",
                          "这是一个由Python开发的小程序，作者是张明宝，这个游戏中，请使用上下左右按键来模拟手指的上下左右滑动，键盘的ESC按键可以重新开始游戏，F10按键可依将您本次的游戏记录存档，祝您游戏愉快！")

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
            qp.setColor(QPalette.Window, Qt.darkBlue)
            lb.setPalette(qp)
            lb.setMinimumHeight(100)
            lb.setMaximumHeight(100)
            lb.setMaximumWidth(100)
            lb.setMinimumWidth(100)
            self.lbs.append(lb)
            mainlayout.addWidget(lb, *position[0])
        self.setdatasource()

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_F10:
                self.selectwritefile()
            if event.key() == Qt.Key_Escape:
                self.initdata()
                self.setdatasource()
            if event.key() == Qt.Key_Up:  # up
                self.data = self.fingerEvent.fingerup(self.data)
                self.setdatasource()
                # print(event.key,"up")
            if event.key() == Qt.Key_Down:  # down
                self.data = self.fingerEvent.fingerdown(self.data)
                self.setdatasource()
                # print(event.key, "down")
            if event.key() == Qt.Key_Left:  # left
                self.data = self.fingerEvent.fingerleft(self.data)
                self.setdatasource()
                # print(event.key, "left")
            if event.key() == Qt.Key_Right:  # right
                self.data = self.fingerEvent.fingerright(self.data)
                self.setdatasource()
            del event
            if self.data == self.fingerEvent.fingerup(self.data) and self.data == self.fingerEvent.fingerdown(
                    self.data) and self.data == self.fingerEvent.fingerleft(
                self.data) and self.data == self.fingerEvent.fingerright(self.data):
                print("游戏结束")
                self.showsavemessagebox("游戏提示框",
                                        "<font size='13' color='red' face='隶书'>游戏已结束，是否保存游戏记录？</font>")
        except Exception as e:
            print(e.__str__())

    def showmessagebox(self, title, msg):
        qm = QMessageBox()
        reply = qm.information(self, title, msg,
                               QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.initdata()
            self.setdatasource()
        else:
            self.close()

    def showsavemessagebox(self, title, msg):
        qm = QMessageBox()
        reply = qm.information(self, title, msg,
                               QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.selectwritefile()
        self.showmessagebox("游戏提示框", "<font size='13' face='微软雅黑'>游戏结束，您要再来一局吗？</font>")

    def initdata(self):
        self.rdfile.cleanfile(self.cachefile)
        self.data = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

    def setdatasource(self):
        self.rdfile.writecachefile(self.cachefile, self.data.__str__())
        pos = 0
        for i in range(0, 4):
            for j in range(0, 4):

                if self.data[i][j] <= 262144:
                    self.pxmap.load("../res/" + str(self.data[i][j]) + ".png")
                    qs = QSize(100, 100)
                    self.lbs[pos].setPixmap(self.pxmap.scaled(qs))
                else:
                    self.showsavemessagebox("游戏提示框",
                                            "<font size='13' color='red' face='隶书'>请收下我的膝盖，\
                                            您的智商已经超出了我的游戏范围！是否保存游戏记录？</font>")

                pos = pos + 1

    def selectreadfile(self):
        file = QFileDialog.getSaveFileName(self, "选取文件", "C:/", "Text Files(*.2048)")

    def selectwritefile(self):
        try:
            file = QFileDialog.getSaveFileName(self, "选取文件", "C:/", "Text Files(*.2048)")
            self.rdfile.cleanfile(file[0])
            for line in self.rdfile.readfile(self.cachefile):
                self.rdfile.writefile(file[0], line.__str__().strip("\n"))
        except Exception as e:
            print(e.__str__())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())
