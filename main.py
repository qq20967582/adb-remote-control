import os
import sys
import time
import threading
from main_ui import Ui_MainWindow
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory


# 仅连接
class myConnectTask(QThread):
    def __init__(self, ip, ip1, width, bandwidth, fps):
        super(myConnectTask, self).__init__()
        self.ip = ip  # ip前缀
        self.ip1 = ip1
        self.width = width
        self.bandwidth = bandwidth
        self.fps = fps

    def run(self) -> None:
        os.popen(r"scrcpy-win64-v2.0\adb.exe connect %s%s:5555" % (self.ip, self.ip1))


# 打开窗口
class myOpenWindwsTask(QThread):
    def __init__(self, ip, ip1, width, bandwidth, fps):
        super(myOpenWindwsTask, self).__init__()
        self.ip = ip  # ip前缀
        self.ip1 = ip1
        self.width = width
        self.bandwidth = bandwidth
        self.fps = fps

    def run(self) -> None:
        os.popen(r"scrcpy-win64-v2.0\scrcpy.exe --tcpip=%s%s --window-title=%s --max-size %s --video-bit-rate %sM --max-fps %s" % (self.ip, self.ip1, self.ip1, int(self.width), int(self.bandwidth), int(self.fps)))


class myMainWindow(Ui_MainWindow):
    def __init__(self):
        super(myMainWindow, self).__init__()

    def setupUi(self, MainWindow):
        super(myMainWindow, self).setupUi(MainWindow)
        self.pushButton_connect.clicked.connect(lambda: self.myConnect())
        self.pushButton_connect_batch.clicked.connect(lambda: self.myConnectBatchThreard())
        self.pushButton_openwindow.clicked.connect(lambda: self.myOpenWindow())
        self.pushButton_openwindows_batch.clicked.connect(lambda: self.myOpenWindowBatchThreard())

    def retranslateUi(self, MainWindow):
        super(myMainWindow, self).retranslateUi(MainWindow)

    # 仅连接，单个
    def myConnect(self):
        self.mc = myConnectTask(self.lineEdit_4.text(), self.spinBox.text(), self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
        self.mc.daemon = True
        self.mc.start()

    # 打开窗口，单个
    def myOpenWindow(self):
        self.mow = myOpenWindwsTask(self.lineEdit_4.text(), self.spinBox.text(), self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
        self.mow.daemon = True
        self.mow.start()

    # 仅连接，批量线程
    def myConnectBatchThreard(self):
        self.mcbt = threading.Thread(target=self.myConnectBatch, daemon=True)
        self.mcbt.start()

    # 仅连接，批量函数
    def myConnectBatch(self):
        for i in range(int(self.lineEdit_5.text()), int(self.lineEdit_6.text()) + 1):
            i = myConnectTask(self.lineEdit_4.text(), i, self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
            i.start()
            time.sleep(0.1)

    # 仅连接，批量线程
    def myOpenWindowBatchThreard(self):
        self.mowbt = threading.Thread(target=self.myOpenWindowBatch, daemon=True)
        self.mowbt.start()

    # 仅连接，批量函数
    def myOpenWindowBatch(self):
        for i in range(int(self.lineEdit_5.text()), int(self.lineEdit_6.text()) + 1):
            i = myOpenWindwsTask(self.lineEdit_4.text(), i, self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
            i.start()
            time.sleep(1)


if __name__ == '__main__':
    # 设置表格样式为Fusion
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = myMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
