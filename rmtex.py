import os
import sys
import re
import argparse


def listdir_nohidden(path):
    no_hidden_list = []
    for f in os.listdir(path):
        if not f.startswith('.'):
            no_hidden_list.append(f)
    return no_hidden_list

def rmfiles(regexp,cwd,dirs,recursive):
    for dir in dirs:
        contents = listdir_nohidden(dir)
        cwd = os.path.join(cwd,dir)
        for content in contents:
            result = re.search(regexp,content)
            if result:
                target = os.path.join(cwd,content)
                os.remove(target)
                print('%(file)s removed!' % {'file':target})
            if os.path.isdir(content) and recursive:
                try:
                    rmfiles(regexp,cwd,[content],recursive)
                except:
                    pass

def main():
    parser = argparse.ArgumentParser(description = "Cleans up LaTeX log files")
    parser.add_argument('dirs', nargs='*', default='.')
    parser.add_argument('-r','--recursive',action='store_true')
    args=parser.parse_args()
    regex = '\w+\.(toc|bbl|aux|gz|blg|dvi|log|out)$'
    print("Removing LaTeX intermediate and log files from:")
    print("")
    for dir in args.dirs:
        print(os.path.join(os.getcwd(),dir))
    print("")
    here = os.getcwd()
    rmfiles(regex,here,args.dirs,args.recursive)
    print("Done!")
    
if __name__ == "__main__":
    main()