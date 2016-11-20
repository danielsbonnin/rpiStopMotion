# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 461, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.dial = QtWidgets.QDial(self.centralWidget)
        self.dial.setGeometry(QtCore.QRect(330, 350, 50, 64))
        self.dial.setObjectName("dial")
        self.captureButton = QtWidgets.QPushButton(self.centralWidget)
        self.captureButton.setGeometry(QtCore.QRect(30, 360, 93, 28))
        self.captureButton.setObjectName("captureButton")
        self.frameRateSpinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.frameRateSpinBox.setGeometry(QtCore.QRect(160, 370, 42, 22))
        self.frameRateSpinBox.setObjectName("frameRateSpinBox")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(150, 350, 81, 16))
        self.label.setObjectName("label")
        self.numFramesSpinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.numFramesSpinBox.setGeometry(QtCore.QRect(250, 370, 42, 22))
        self.numFramesSpinBox.setObjectName("numFramesSpinBox")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(240, 350, 71, 20))
        self.label_2.setObjectName("label_2")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(30, 400, 93, 28))
        self.playButton.setObjectName("playButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralWidget)
        self.deleteButton.setGeometry(QtCore.QRect(390, 360, 93, 28))
        self.deleteButton.setObjectName("deleteButton")
        self.exportButton = QtWidgets.QPushButton(self.centralWidget)
        self.exportButton.setGeometry(QtCore.QRect(390, 400, 93, 28))
        self.exportButton.setObjectName("exportButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuStop_Motion_Studio = QtWidgets.QMenu(self.menuBar)
        self.menuStop_Motion_Studio.setObjectName("menuStop_Motion_Studio")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuStop_Motion_Studio.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.captureButton.setText(_translate("MainWindow", "Capture"))
        self.label.setText(_translate("MainWindow", "Frame Rate"))
        self.label_2.setText(_translate("MainWindow", "# Frames"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.menuStop_Motion_Studio.setTitle(_translate("MainWindow", "Stop Motion Studio"))

