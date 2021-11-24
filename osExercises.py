import os
import time

def os_info():
	return os.name, os.uname(), os.getcwd(), os.listdir('.')
	# os name, os info, directory of os in memory, files in the memory location as os.

def all_files_in_path(path):
	files = [name for name in os.listdir(path)]
	return files


def subdirs(path):
	lst = []
	for entry in os.scandir(path):
		if entry.is_dir():
			typ = 'dir'
			dire = entry.name
			subdir = os.path.join(path, dire) + f': {typ}'
			lst.append(subdir)
		else: pass	
	return lst

def is_empty_file(filepath):
	filesize = os.path.getsize(filepath)
	if not filesize:
		return True
	else: return False

def EREW_check(filepath):
	exist = 'Exist: ' + os.access(filepath, os.F_OK) # or os.path.exists(filepath)
	readabe = 'Readable: ' + os.access(filepath, os.R_OK)
	writable = 'Writeable: ' + os.access(filepath, os.W_OK)
	executable = 'Executable: ' + os.access(filepath, os.X_OK)
	return exist, readable, writable, executable

def file_info(filepath):
	info = os.stat(filepath)
	size = 'Size: ' + info.st_size
	permission = 'Permission: ' + info.st_mode
	owner = 'Owner: ' + info.st_uid
	device = 'Device: ' + info.st_dev
	toc = 'Created: '+time.ctime(info.st_ctime)
	tom = 'Last modified: ' + time.ctime(info.st_mtime)
	toa = 'Last accessed: ' + time.ctime(info.st_atime)
	l = []
	l.extend((size, permission, owner, device, toc, tom, toa))
	for i in l:
		print(i)

