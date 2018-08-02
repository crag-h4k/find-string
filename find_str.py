#!/usr/bin/python3

from sys import argv
from os import listdir
from datetime import datetime

def find_string(directory,ftype,search_string):
	arr = []
	temp_arr = []

	while True:
		try:
	
			for fname in listdir(directory):
				if (fname[0] == '.') or (not fname.endswith(ftype)):
					continue
				if not directory.endswith('/'):
					directory = directory + '/'

				path = directory+fname
				with open(path) as f:
					for num, line in enumerate(f,0):
						info = fname + '\n' + line
						if 
						if (search_string in line) and (info not in arr):
							arr.append(info)
							ts = datetime.now().strftime('%H:%M:%S')
							
							print(ts,arr[-1])
				f.close()

		except KeyboardInterrupt:
			break
	
for i in argv:
	print(i)

find_string(directory = argv[1], ftype = argv[2], search_string = argv[3])

