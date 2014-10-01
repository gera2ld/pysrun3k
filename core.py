#!python
# coding=utf-8
# Author: Gerald <gera2ld@163.com>
# Compatible with Python 2
import time,struct,socket,logging,sys
if sys.version_info>(3,):
	from urllib import request
	from urllib.parse import quote
else:
	import urllib2 as request
	from urllib import quote
	input=raw_input

class SRun3K:
	keeping=False
	uid=-1
	diff=0
	host=None
	port=3335
	_callback=None
	def __init__(self, callback=None):
		self._callback=callback
		self.opener=request.build_opener()
		self.opener.addheaders.append(('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1 SRun3K Client_W115S0B20131021A-SRun3K'))
	def callback(self, data):
		data.setdefault('message','Something not good happened...')
		if self._callback:
			self._callback(data)
		else:
			logging.info(data['message'])
	def setServer(self, host, port=None):
		self.host=host
		if port: self.port=port
		logging.info('Using server %s:%d',self.host,self.port)
		return True
	def postData(self,url,data):
		if isinstance(data,str): data=data.encode()
		r=self.opener.open(url,data,timeout=5)
		g=r.read().decode()
		return g
	def encode(self,code,key):
		code=bytearray(code)
		key=bytearray(key)
		d=bytearray()
		n=m=len(key)-1
		for i in code:
			j=i^key[m]
			k=(0xf&j>>4)+99
			l=(j&0xf)+54
			d.append(l if m%2 else k)
			d.append(k if m%2 else l)
			m-=1
			if m<0: m=n
		d=quote(bytes(d))
		return d
	def keepAlive(self):
		data=struct.pack('Q',self.uid)
		s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.settimeout(1)
		try:
			s.sendto(data,(self.host,self.port))
			d,addr=s.recvfrom(1024)
		except Exception as e:
			d='Error: '+d[8:].decode()
		s.close()
		if d[:8]!=data:
			return d
	def logIn(self, username, password, mac=None):
		def getMAC():
			import uuid,re
			node=uuid.getnode()
			mac='%012x' % node
			return '-'.join(re.findall('..',mac))
		def logInOnce():
			self.now=int(time.time())
			t=self.now-self.diff
			k=str(t//60).encode()
			c=self.encode(password,k)
			m=self.encode(mac,k)
			data_login='username=%s&password=%s&drop=0&type=2&n=100&mac=%s' % (username, c, m)
			g=self.postData('http://%s/cgi-bin/do_login' % self.host,data_login)
			return g
		logging.info('Logging in as %s...',username)
		password=password.encode()
		if mac is None: mac=getMAC()
		mac=mac.encode()
		try:
			g=logInOnce()
			m,_,t=g.partition('@')
			if _:
				t=int(t)
				self.diff=self.now-t
				g=logInOnce()
				m,_,t=g.partition('@')
		except Exception as e:
			self.callback({'message':str(e).replace('\n',' ')})
			return
		if _:	# error occurred
			self.callback({'message':m})
			return
		if not g: return
		cb={'message':g}
		m=g.split(',')
		if len(m)==5:
			self.uid=int(m[0])
			cb['message']='Logged in successfully.'
			cb['window']='hide'
		self.callback(cb)
		if self.keeping: return
		self.keeping=True
		delay=60
		error=0
		while self.uid>0:
			time.sleep(delay)
			d=self.keepAlive()
			if d is None:	# Kept alive
				logging.info('Kept alive.')
				if error:	# clear error
					delay=60
					error=0
			else:
				if not error:
					delay=10
				error+=1
				if error>=6:
					self.uid=-1
					self.callback({'message':'Error keeping alive, connection closed.','window':'show'})
				else:
					logging.info('Error keeping alive, retry 10 seconds later.')
		self.keeping=False
	def logOut(self):
		if self.uid<0: return
		try:
			g=self.postData('http://%s/cgi-bin/do_logout' % self.host,'uid=%s' % self.uid)
		except Exception as e:
			self.callback({'message':str(e)})
			return
		if g=='logout_ok':
			self.uid=-1
			self.callback({'message':'Logged out successfully.'})
		else:
			self.callback({'message':g})

def main(args):
	import pickle,base64,getpass
	conf_file='core.conf'
	try:
		conf=pickle.load(open(conf_file, 'rb'))
		assert isinstance(conf,dict)
	except:
		conf={}
	u=base64.b64decode(conf.get('u', b'')).decode()
	p=base64.b64decode(conf.get('p', b'')).decode()
	h=conf.setdefault('h', '124.17.96.78')
	logging.info('Starting SRun3K Stupid...')
	if not u or not p:
		while not u:
			u=str(input('Input username: '))
		conf['u']=base64.b64encode(str(u).encode())
		while not p:
			p=getpass.getpass('Input password (not shown): ')
		conf['p']=base64.b64encode(p.encode())
		pickle.dump(conf, open(conf_file, 'wb'))
		logging.info('Config saved.')
	s=SRun3K()
	s.setServer(h)
	s.logIn(u,p)

if __name__=='__main__':
	logging.basicConfig(level=logging.NOTSET,format='%(asctime)s - %(levelname)s: %(message)s')
	main(sys.argv)
