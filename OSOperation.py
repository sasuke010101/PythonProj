#coding=utf-8
import os,subprocess,signal

p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():
   if 'QQ' in line:
     pid = int(line.split(None, 1)[0])
     os.kill(pid, signal.SIGKILL)


os.system("open /Applications/QQ.app")
