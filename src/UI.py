# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(2097, 1405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 14, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.log_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.log_groupBox.setGeometry(QtCore.QRect(0, 1080, 2091, 251))
        self.log_groupBox.setObjectName("log_groupBox")
        self.log_textBrowser = QtWidgets.QTextBrowser(self.log_groupBox)
        self.log_textBrowser.setGeometry(QtCore.QRect(10, 30, 2081, 221))
        self.log_textBrowser.setObjectName("log_textBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 2081, 981))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.froce_groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.froce_groupBox.setObjectName("froce_groupBox")
        self.plot_force_widget = MplWidget(self.froce_groupBox)
        self.plot_force_widget.setGeometry(QtCore.QRect(0, 120, 1031, 851))
        self.plot_force_widget.setObjectName("plot_force_widget")
        self.label = QtWidgets.QLabel(self.froce_groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 111, 23))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.froce_groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 52, 121, 31))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.froce_groupBox)
        self.initialization = QtWidgets.QGroupBox(self.layoutWidget)
        self.initialization.setObjectName("initialization")
        self.plot_initial_widget = MplWidget(self.initialization)
        self.plot_initial_widget.setGeometry(QtCore.QRect(0, 30, 1031, 951))
        self.plot_initial_widget.setObjectName("plot_initial_widget")
        self.horizontalLayout.addWidget(self.initialization)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2097, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.parse_xml)
        self.comboBox.currentTextChanged['QString'].connect(MainWindow.on_force_combobox)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "column.xml"))
        self.log_groupBox.setTitle(_translate("MainWindow", "log"))
        self.froce_groupBox.setTitle(_translate("MainWindow", "force_ideal.nc"))
        self.label.setText(_translate("MainWindow", "variable:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "U"))
        self.comboBox.setItemText(1, _translate("MainWindow", "V"))
        self.comboBox.setItemText(2, _translate("MainWindow", "W"))
        self.comboBox.setItemText(3, _translate("MainWindow", "QVAPOR"))
        self.comboBox.setItemText(4, _translate("MainWindow", "QCLOUD"))
        self.comboBox.setItemText(5, _translate("MainWindow", "QRAIN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "theta"))
        self.initialization.setTitle(_translate("MainWindow", "input_souding&soil"))

from mplwidget import MplWidget
