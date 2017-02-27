import os
import sys

def is_valid_dir(dir):
	return os.path.isdir(dir)
	
def logRenameInfo(oldFileName, newFileName):
	print('renamed ' + oldFileName + ' to ' + newFileName + '.')
	return
	
if len(sys.argv) != 4:
	raise ValueError('\nInvalid inputs. Please specify the following arguments\n1. File Directory\n2. Current File Extension\n3. New File Extension')
else:
	dir = sys.argv[1]
	curr_ext = sys.argv[2]
	new_ext = sys.argv[3]
	
	if is_valid_dir(dir):
		for thisFile in os.listdir(dir):
			if thisFile.endswith(curr_ext): 
				logRenameInfo(thisFile, os.path.splitext(thisFile)[0] + '.' + new_ext)
				os.rename(os.path.join(dir, thisFile), os.path.join(dir, os.path.splitext(thisFile)[0] + new_ext))
				continue
			else:
				continue
	else:
		raise ValueError('Directory ' + dir + ' is not a valid directory.')