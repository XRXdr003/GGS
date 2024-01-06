#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/GSRAJ.GS/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf gs.so')
except:
    pass
os.system('rm -rf gs.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('gs.so'):
        os.system('curl -L https://github.com/XRXdr003/GGS/blob/main/gs.cpython-311.so?raw=true -o gd.so') 
        import gs
    else:
        import gs
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    
 
 
