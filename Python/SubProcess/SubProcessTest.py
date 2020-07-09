import subprocess
import datetime
import sys

def runScript ():


    # proc = subprocess.Popen(command,shell=True, executable='/bin/bash', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    # proc.wait()
    # for line in proc.stdout:
    #     result_stdout += line;
    # for line in proc.stderr:
    #     result_stderr += line;
    # print result_stdout
    # print result_stderr

   p=subprocess.Popen('cat /tmp/test2.log',shell=True, executable='/bin/bash', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
   stdoutput,erroutput = p.communicate()
   for line in stdoutput.split("\n"):
       print line
   print len(stdoutput)
   print erroutput, len(erroutput)
   # p=subprocess.Popen('cat /tmp/test2.log',shell=True, executable='/bin/bash', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
   # print p.wait()

runScript()


