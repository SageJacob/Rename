import os
import datetime

now = datetime.datetime.now()

def reformat(searchfile):
    encounter, i = 0, 0
    rename = ""
    while (i < len(searchfile) and encounter < 2):
        if (not searchfile[i].isalpha()):
            encounter += 1
        if (encounter == 2):
            break
        rename += searchfile[i]
        i += 1
    return rename

def main():
    cd = os.getcwd()
    a = input('enter folder name: ')
    path = cd + '/' + a
    
    cd = os.path.abspath(os.sep)
    cd = os.chdir(path)
    cd = os.listdir(path)
    print("WARNING: The current folder you are in is about to be altered!")
    boolean = input('The current folder you are in is: ' + os.getcwd() + '. Do you wish to continue? (y/n) ')
    if boolean == 'y':    
        for searchfile in cd:
            if searchfile.startswith('.'):
                continue
            small = os.getcwd()
            small = os.path.abspath(os.sep)
            newPath = path + '/' + searchfile
            small = os.chdir(newPath)
            small = os.listdir(newPath)
            for singlefile in small:
                if '.pdf' in singlefile:
                    rename = reformat(searchfile)
                    dst = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + '-' + rename + '.pdf'
                    os.rename(singlefile, dst) 
            small = cd
        
if __name__ == '__main__': 
    main() 