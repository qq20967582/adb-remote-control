# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 180)
        MainWindow.setMinimumSize(QtCore.QSize(450, 180))
        MainWindow.setMaximumSize(QtCore.QSize(450, 180))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(80, 10, 60, 20))
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 10, 40, 20))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 60, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 40, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 10, 60, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 10, 60, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 60, 50, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 60, 70, 20))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(160, 60, 50, 20))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_openwindow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openwindow.setGeometry(QtCore.QRect(230, 60, 90, 20))
        self.pushButton_openwindow.setObjectName("pushButton_openwindow")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 110, 50, 20))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 110, 50, 20))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_openwindows_batch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openwindows_batch.setGeometry(QtCore.QRect(230, 110, 90, 20))
        self.pushButton_openwindows_batch.setObjectName("pushButton_openwindows_batch")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 110, 70, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(330, 60, 90, 20))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_connect_batch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect_batch.setGeometry(QtCore.QRect(330, 110, 90, 20))
        self.pushButton_connect_batch.setObjectName("pushButton_connect_batch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_1.setText(_translate("MainWindow", "800"))
        self.label_1.setText(_translate("MainWindow", "宽度："))
        self.label_2.setText(_translate("MainWindow", "传输带宽："))
        self.label_3.setText(_translate("MainWindow", "FPS："))
        self.lineEdit_2.setText(_translate("MainWindow", "5"))
        self.lineEdit_3.setText(_translate("MainWindow", "10"))
        self.label_4.setText(_translate("MainWindow", "ip前缀："))
        self.lineEdit_4.setText(_translate("MainWindow", "10.2.10."))
        self.pushButton_openwindow.setText(_translate("MainWindow", "打开窗口"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setText(_translate("MainWindow", "20"))
        self.pushButton_openwindows_batch.setText(_translate("MainWindow", "批量打开窗口"))
        self.label_5.setText(_translate("MainWindow", "批量连接IP："))
        self.pushButton_connect.setText(_translate("MainWindow", "仅连接"))
        self.pushButton_connect_batch.setText(_translate("MainWindow", "批量仅连接"))
