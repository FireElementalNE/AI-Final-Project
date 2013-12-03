import sys,os
from subprocess import Popen, PIPE
sublime_location = '\"C:\Program Files\Sublime Text 2\sublime_text.exe\" '
commands = []
try:
	directory = sys.argv[1]
except IndexError:
	print 'Usage: python ' + sys.argv[0] + ' <directory> <search term>'
	sys.exit(0)
for root, dirnames, filenames in os.walk(directory):
	for filename in filenames:
		if filename.endswith('py'):
			commands.append(sublime_location+directory+filename)


for x in commands:
	os.system(x)