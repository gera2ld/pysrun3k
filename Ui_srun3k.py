# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Gerald\Source\PyProjects\SRun3K\srun3k.ui'
#
# Created: Tue Feb  4 09:05:28 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 234)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.labelUsr = QtGui.QLabel(self.centralWidget)
        self.labelUsr.setTextFormat(QtCore.Qt.AutoText)
        self.labelUsr.setObjectName("labelUsr")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelUsr)
        self.editUsr = QtGui.QLineEdit(self.centralWidget)
        self.editUsr.setObjectName("editUsr")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.editUsr)
        self.labelPwd = QtGui.QLabel(self.centralWidget)
        self.labelPwd.setObjectName("labelPwd")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelPwd)
        self.editPwd = QtGui.QLineEdit(self.centralWidget)
        self.editPwd.setObjectName("editPwd")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.editPwd)
        self.labelMAC = QtGui.QLabel(self.centralWidget)
        self.labelMAC.setObjectName("labelMAC")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelMAC)
        self.editMAC = QtGui.QLineEdit(self.centralWidget)
        self.editMAC.setObjectName("editMAC")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.editMAC)
        self.btMAC = QtGui.QPushButton(self.centralWidget)
        self.btMAC.setObjectName("btMAC")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.btMAC)
        self.labelHost = QtGui.QLabel(self.centralWidget)
        self.labelHost.setObjectName("labelHost")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelHost)
        self.editHost = QtGui.QLineEdit(self.centralWidget)
        self.editHost.setObjectName("editHost")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.editHost)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cbRemember = QtGui.QCheckBox(self.centralWidget)
        self.cbRemember.setChecked(True)
        self.cbRemember.setObjectName("cbRemember")
        self.gridLayout.addWidget(self.cbRemember, 0, 0, 1, 1)
        self.btLog = QtGui.QPushButton(self.centralWidget)
        self.btLog.setText("")
        self.btLog.setDefault(True)
        self.btLog.setObjectName("btLog")
        self.gridLayout.addWidget(self.btLog, 1, 0, 1, 1)
        self.btHide = QtGui.QPushButton(self.centralWidget)
        self.btHide.setObjectName("btHide")
        self.gridLayout.addWidget(self.btHide, 1, 1, 1, 1)
        self.cbAutoLogin = QtGui.QCheckBox(self.centralWidget)
        self.cbAutoLogin.setObjectName("cbAutoLogin")
        self.gridLayout.addWidget(self.cbAutoLogin, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.labelUsr.setBuddy(self.editUsr)
        self.labelPwd.setBuddy(self.editPwd)
        self.labelMAC.setBuddy(self.editMAC)
        self.labelHost.setBuddy(self.editHost)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.editUsr, self.editPwd)
        MainWindow.setTabOrder(self.editPwd, self.editMAC)
        MainWindow.setTabOrder(self.editMAC, self.btMAC)
        MainWindow.setTabOrder(self.btMAC, self.cbRemember)
        MainWindow.setTabOrder(self.cbRemember, self.btLog)
        MainWindow.setTabOrder(self.btLog, self.btHide)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SRun3K Stupid v1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUsr.setText(QtGui.QApplication.translate("MainWindow", "&User:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPwd.setText(QtGui.QApplication.translate("MainWindow", "&Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMAC.setText(QtGui.QApplication.translate("MainWindow", "&MAC:", None, QtGui.QApplication.UnicodeUTF8))
        self.btMAC.setText(QtGui.QApplication.translate("MainWindow", "&Get MAC of current device", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHost.setText(QtGui.QApplication.translate("MainWindow", "&Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbRemember.setText(QtGui.QApplication.translate("MainWindow", "&Remember me", None, QtGui.QApplication.UnicodeUTF8))
        self.btHide.setText(QtGui.QApplication.translate("MainWindow", "Minimize to &tray", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoLogin.setText(QtGui.QApplication.translate("MainWindow", "Log in at &start up", None, QtGui.QApplication.UnicodeUTF8))

import srun3k_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

