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
        MainWindow.resize(523, 515)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.captureButton = QtWidgets.QPushButton(self.centralWidget)
        self.captureButton.setGeometry(QtCore.QRect(30, 360, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captureButton.sizePolicy().hasHeightForWidth())
        self.captureButton.setSizePolicy(sizePolicy)
        self.captureButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.captureButton.setObjectName("captureButton")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(30, 400, 93, 28))
        self.playButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playButton.setObjectName("playButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralWidget)
        self.deleteButton.setGeometry(QtCore.QRect(390, 360, 93, 28))
        self.deleteButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteButton.setObjectName("deleteButton")
        self.exportButton = QtWidgets.QPushButton(self.centralWidget)
        self.exportButton.setGeometry(QtCore.QRect(390, 400, 93, 28))
        self.exportButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exportButton.setObjectName("exportButton")
        self.imageView = QtWidgets.QLabel(self.centralWidget)
        self.imageView.setGeometry(QtCore.QRect(30, 20, 441, 301))
        self.imageView.setText("")
        self.imageView.setScaledContents(True)
        self.imageView.setObjectName("imageView")
        self.currentFrameLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentFrameLabel.setGeometry(QtCore.QRect(150, 370, 91, 16))
        self.currentFrameLabel.setObjectName("currentFrameLabel")
        self.numFrames = QtWidgets.QLineEdit(self.centralWidget)
        self.numFrames.setGeometry(QtCore.QRect(220, 400, 31, 22))
        self.numFrames.setFocusPolicy(QtCore.Qt.NoFocus)
        self.numFrames.setObjectName("numFrames")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(200, 400, 16, 16))
        self.label_3.setObjectName("label_3")
        self.currentFrame = QtWidgets.QSpinBox(self.centralWidget)
        self.currentFrame.setGeometry(QtCore.QRect(150, 400, 42, 22))
        self.currentFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.currentFrame.setStyleSheet("")
        self.currentFrame.setObjectName("currentFrame")
        self.speedGroup = QtWidgets.QGroupBox(self.centralWidget)
        self.speedGroup.setGeometry(QtCore.QRect(270, 350, 111, 81))
        self.speedGroup.setCheckable(False)
        self.speedGroup.setChecked(False)
        self.speedGroup.setObjectName("speedGroup")
        self.slowRadio = QtWidgets.QRadioButton(self.speedGroup)
        self.slowRadio.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.slowRadio.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slowRadio.setChecked(False)
        self.slowRadio.setObjectName("slowRadio")
        self.mediumRadio = QtWidgets.QRadioButton(self.speedGroup)
        self.mediumRadio.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.mediumRadio.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mediumRadio.setChecked(True)
        self.mediumRadio.setObjectName("mediumRadio")
        self.fullRadio = QtWidgets.QRadioButton(self.speedGroup)
        self.fullRadio.setGeometry(QtCore.QRect(10, 60, 95, 20))
        self.fullRadio.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fullRadio.setObjectName("fullRadio")
        self.slowRadio.raise_()
        self.mediumRadio.raise_()
        self.fullRadio.raise_()
        self.mediumRadio.raise_()
        self.fullRadio.raise_()
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(90, 470, 120, 80))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 523, 26))
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
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.currentFrameLabel.setText(_translate("MainWindow", "Current Frame"))
        self.label_3.setText(_translate("MainWindow", "/"))
        self.speedGroup.setTitle(_translate("MainWindow", "Speed"))
        self.slowRadio.setText(_translate("MainWindow", "slow"))
        self.mediumRadio.setText(_translate("MainWindow", "medium"))
        self.fullRadio.setText(_translate("MainWindow", "full"))
        self.menuStop_Motion_Studio.setTitle(_translate("MainWindow", "Stop Motion Studio"))

