#!python
# coding=utf-8
import sys
from PySide import QtGui, QtCore
app=QtGui.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
t=QtCore.QTranslator()
t.load(QtCore.QLocale.system().name())
app.installTranslator(t)
from gui import GUI
g=GUI()
g.show()
sys.exit(app.exec_())
