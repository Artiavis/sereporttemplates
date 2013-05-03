import os
import sys
import re
import argparse

def create_regex(reglist):
    inner = "|".join(reglist)
    regex = '\w+\.(' + inner + ')$'
    return regex
    
class Remover:
    """A class to encapsulate removing functionality"""
    def __init__(self,regexp,dir,recursive):
        self.regex = regexp
        self.dir = os.path.abspath(dir)
        self.recursive = recursive
    def printmsg(self):
        print("Removing LaTeX intermediate and log files from:")
        print(self.dir)
    def remove(self):
        self.printmsg()
        if self.recursive == True:
            self.remove_recursive()
        else:
            self.remove_nonrec(self.dir)
    def remove_recursive(self):
        for root, dirs, files in os.walk(self.dir):
            # dirs[:] = [d for d in dirs if not d[0] == '.']
            self.remove_nonrec(root)
    def remove_nonrec(self,path):
        contents = os.listdir(path)
        for content in contents:
            result = re.search(self.regex,content)
            if result:
                target = os.path.join(path,content)
                os.remove(target)
                print('%(file)s removed!' % {'file':target})

def main(regex,dirs,recursive):
    for dir in dirs:
        rm = Remover(regex,dir,recursive)
        rm.remove()
    print("Done!")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Cleans up LaTeX log files")
    parser.add_argument('dirs', nargs='*', default='.', help='directories to remove from (default: current)')
    parser.add_argument('-r','--recursive',action='store_true',help='remove recursively from directories')
    parser.add_argument('-e','--extensions', nargs='*',default=['toc','bbl','aux','gz','blg','dvi','log','out'],
        help='specify file extensions to remove (default: LaTeX log files)')
    args=parser.parse_args()
    regex = '\w+\.(toc|bbl|aux|gz|blg|dvi|log|out)$'
    regex = create_regex(args.extensions)
    main(regex,args.dirs,args.recursive)