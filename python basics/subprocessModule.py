''' The subprocess module enables you to start new applications from your Python program.
    You can start a process in Python using the Popen function call.
    stdout is the process output. stderr will be written only if an error occurs.
    If you want to wait for the program to finish you can call Popen.wait().
'''

from subprocess import Popen,PIPE
process=Popen(['cat','test.py'],stdout=PIPE,stderr=PIPE)
stdout,stderr=process.communicate()
print(stdout)

#subprocess.call() : which can be used to start a program.
import subprocess
subprocess.call(["ls", "-l"])

#save process output
import subprocess
s = subprocess.check_output(["echo", "Hello World!"])
print("s = " + s)