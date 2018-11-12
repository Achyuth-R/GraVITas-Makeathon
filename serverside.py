  import paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.43.31', username='pi', password='alohomora')
ftp_client=ssh_client.open_sftp()
for i in xrange(1,51):
	ftp_client.get('/home/pi/projects/makerep/photos/'+str(i)+'.jpg','/home/neha/projects/makerep/photos/'+str(i)+'.jpg')
ftp_client.close()
