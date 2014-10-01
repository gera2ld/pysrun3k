#!/usr/bin/python
# coding=utf-8
from PySide.QtGui import *
from PySide.QtCore import *
import Ui_srun3k, core, threading, pickle, base64, uuid, re, time

class GUI(QMainWindow, Ui_srun3k.Ui_MainWindow):
	conf='SRun3K.conf'
	signal=Signal(dict)
	icon1=QIcon(':/internet1.ico')
	icon2=QIcon(':/internet2.ico')
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.tray=QSystemTrayIcon(self.icon1)
		self.tray.show()
		menu=QMenu()
		self.aShow=menu.addAction('')
		self.aShow.triggered.connect(self.toggleShow)
		menu.addAction('&About').triggered.connect(self.showAbout)
		menu.addAction('E&xit').triggered.connect(self.close)
		self.tray.setContextMenu(menu)
		self.tray.activated.connect(self.trayActivated)
		self.editPwd.setEchoMode(QLineEdit.Password)
		self.core=core.SRun3K(self.sigCallback)
		self.btLog.setText('&Log In')
		self.btLog.clicked.connect(self.toggleLog)
		self.btMAC.clicked.connect(self.getMAC)
		self.btHide.clicked.connect(self.hide)
		self.signal.connect(self.callback)
		self.items=[self.editUsr, self.editPwd, self.editHost, self.editMAC, self.btMAC]
		try:
			conf=pickle.load(open(self.conf, 'rb'))
			assert isinstance(conf,dict)
		except:
			conf={}
		if m is None: self.getMAC()
		else: self.editMAC.setText(m)
		self.cbRemember.setChecked(conf.get('r', True))
		self.cbAutoLogin.setChecked(conf.get('a', True))
		self.editHost.setText(conf.get('h', ''))
		if self.cbRemember.isChecked():
			try:
				self.editUsr.setText(base64.b64decode(conf.get('u', b'')).decode())
				self.editPwd.setText(base64.b64decode(conf.get('p', b'')).decode())
			except: pass
		if self.cbAutoLogin.isChecked():
			self.toggleLog()
	def showAbout(self):
		QMessageBox.about(
			self,
			self.trUtf8("SRun3K Stupid"),
			self.trUtf8("""=== For private use only ===

Dedicate to my dreamgirl,
  wish her happy and beautiful forever.

\t\t\t-- Gerald"""))
	def getMAC(self):
		node=uuid.getnode()
		mac='%012x' % node
		self.editMAC.setText('-'.join(re.findall('..',mac)))
	def toggleShow(self):
		if self.isVisible():
			self.hide()
		else:
			self.show()
	def trayActivated(self, e):
		if e==QSystemTrayIcon.Trigger:
			self.toggleShow()
		else:
			self.aShow.setText('Hide &Window' if self.isVisible() else 'Show &Window')
	def closeEvent(self, e):
		self.tray.hide()
		conf={
			'r':self.cbRemember.isChecked(),
			'h':self.editHost.text(),
			'm':self.editMAC.text(),
			'a':self.cbAutoLogin.isChecked(), 
		}
		if conf['r']:
			conf['u']=base64.b64encode(self.editUsr.text().encode())
			conf['p']=base64.b64encode(self.editPwd.text().encode())
		pickle.dump(conf, open(self.conf, 'wb'))
		quit()
	def callback(self, data):
		if self.core.uid>0:
			self.btLog.setText('&Log Out')
			self.setWindowIcon(self.icon1)
			self.tray.setIcon(self.icon1)
		else:
			self.btLog.setText('&Log In')
			self.setWindowIcon(self.icon2)
			self.tray.setIcon(self.icon2)
		w=data.get('window')
		if w=='hide': self.hide()
		elif w=='show': self.show()
		self.statusBar.showMessage(time.strftime('%H:%M ')+data.get('message','What did I do just now?'))
		self.btLog.setEnabled(True)
		if self.core.uid<=0:
			for i in self.items: i.setEnabled(True)
	def sigCallback(self, data):
		self.signal.emit(data)
	def toggleLog(self):
		self.btLog.setEnabled(False)
		if self.core.uid>0:
			t=threading.Thread(target=self.core.logOut)
			t.daemon=True
			t.start()
		elif self.core.setServer(self.editHost.text()):
			for i in self.items: i.setEnabled(False)
			t=threading.Thread(
				target=self.core.logIn,
				args=(
					self.editUsr.text(),
					self.editPwd.text(), 
					self.editMAC.text(), 
				)
			)
			t.daemon=True
			t.start()
