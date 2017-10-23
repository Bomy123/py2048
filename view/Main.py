from PyQt5.QtWidgets import QWidget,QApplication , QTableWidget, QHBoxLayout, QLabel, QLayout
from PyQt5.QtGui import QFont,QPicture
import sys
import controller.FingerEvent
import util.NormalUtils
class MainWindow(QWidget):
    data = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("2048小游戏")
        self.resize(500,500)
        self.focusPolicy()
        self.font = QFont()
        self.initUi()
        util.NormalUtils.printlist(self.data)

    def initUi(self):
        # self.tllayout = QTableWidget()
        # self.tllayout.setColumnCount(4)
        # self.tllayout.setRowCount(4)
        # #self.tllayout.setFont(QFont(QFont.Black))
        # self.tllayout.setColumnWidth(100,100)
        # self.tllayout.setRowHeight(100,100)
        # self.tllayout.setFixedHeight(400)
        # self.tllayout.setFixedWidth(400)
        self.lb1 = QLabel("test")

        self.lb1.setFixedWidth(100)
        self.lb1.setFixedHeight(100)
        self.setStyleSheet('background: transparent;'
                            'border-color: rgb(0, 66, 111);'
                            'margin: 2px;')
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.lb1)
        self.setLayout(mainLayout)
        #self.tllayout.setFont(QFont.Black)

    def keyPressEvent(self,event):

        if(event.key() == 16777235):#up
            self.data = controller.FingerEvent.fingerup(self.data)
        if(event.key() == 16777237):#down
            self.data = controller.FingerEvent.fingerdown(self.data)
        if (event.key() == 16777234):#left
            self.data = controller.FingerEvent.fingerleft(self.data)
        if (event.key() == 16777236):#right
            self.data = controller.FingerEvent.fingerright(self.data)
        util.NormalUtils.printlist(self.data)
        # print(event.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())