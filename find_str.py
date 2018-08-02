#!/usr/bin/python3

from sys import argv
from os import listdir
from datetime import datetime
from string import whitespace

def format_time(line,*time_format):
	#if time_format == 'unix_epoch':
	for i in line:
		if i.isdigit():
			epoch_time = line[:16]
			readable_time = (datetime.utcfromtimestamp(float(epoch_time))).strftime('%H:%M:%S')
			new_line = readable_time + line.strip(line[:16])
			#print(new_line)
			return new_line
		else:
			return line


def find_string(directory,ftype,search_string,*time_format):
	arr = []

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
						line = format_time(line,time_format)
						info = fname + '\n' + line
						if (search_string in line) and (info not in arr):
							arr.append(info)

						else:	
							continue

						print(arr[-1])
				f.close()

		except KeyboardInterrupt:
			break
	
for i in argv:
	print(i)
directory = argv[1]
ftype = argv[2]
search_string = argv[3]
time_format = argv[4]

find_string(directory, ftype, search_string, *time_format)
#find_string(directory = argv[1], ftype = argv[2], search_string = argv[3], *argv[4])

