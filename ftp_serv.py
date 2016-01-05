#############SERVER_CODE###########################
import socket
import datetime
HOST ='localhost'
PORT =3500

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
conn, addr = s.accept()
start=datetime.datetime.now()
print start
try:
	while (True):
			if addr=='192.168.0.9'or 'localaddress':
			print 'connected by', addr
			size=conn.recv(1024)
			size=int (size)
			print size
			fo=open('rq','w')
			print 'file opened'
			#conn.send('connected')
			while (1):
				conn.send("connected")		
				data=conn.recv(size)		
				if not data: break
				fo.write(data)			
				#print(data)				
			conn.close()	
			fo.close()	
			print end
		else:
			conn.send('invalid client')
except(socket.error):
	print('transfer complete')

end=datetime.datetime.now()
print 'disconnected'
rec_time=float((end-start).microseconds)
print rec_time






