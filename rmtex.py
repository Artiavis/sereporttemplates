import os
import sys
import re


def rmfiles(regexp,dirs):
	for dir in dirs:
		files = os.listdir(dir)
		for file in files:
			result = re.search(regexp,file)
			if result:
				target = os.path.join(os.getcwd(),dir,file)
				os.remove(target)
				print('%(file)s removed!' % {'file':target})
				
regex = '\w+\.(toc|bbl|aux|gz|blg|dvi|log|out)$'
print("Removing LaTeX intermediate and log files from:")
print()
dirs = [".", "tex"]
for dir in dirs:
	print(os.path.join(os.getcwd(),dir))
print()
rmfiles(regex,dirs)
print("Done!")