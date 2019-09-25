#! python3
import random 
import os 
from optparse import *
import time 
import platform 
import string
import playsound 


if platform.system() == "Linux" :
    os.system("clear")

elif platform.system() == "Windows" : 
    os.system("cls")

def colors():
    
    W  = '\033[0m'    # white (default)
    R  = '\033[1;31m' # red
    G  = '\033[1;32m' # green bold
    O  = '\033[1;33m' # orange
    B  = '\033[1;34m' # blue
    P  = '\033[1;35m' # purple
    C  = '\033[1;36m' # cyan
    GR = '\033[1;37m' # gray

colors()

def banner():
    print(""" \033[1;36m

    ____        ______                     
   / __ \__  __/ ____/______  ______  _  __
  / /_/ / / / / /   / ___/ / / / __ \| |/_/
 / ____/ /_/ / /___/ /  / /_/ / / / />  <  
/_/    \__, /\____/_/   \__,_/_/ /_/_/|_|  
      /____/                Author : ZetSu              
                             
        """)

banner()
print('\033[1;32m'+"\n")


parser = OptionParser("""Usage   : PyCrunx.py -c To use Characters -l length of password -o Wordlist name
Example : PyCrunx.py -c abcd1234 -l 8 -o wordlist """)   


if platform.system() == "Linux" :
    print(text.replace("\w"),("/w"))


parser.add_option('-c','--Characters',dest='characters',metavar=' ',type=str,help='To use characters')
parser.add_option('-l','--Length',dest='length',metavar=' ',type=int,help='Length of passwords')
parser.add_option('-o','--output',dest='output',metavar=' ',type=str,help="Wordlist's name")
options,args = parser.parse_args()
if options.characters == None and options.length == None and options.output == None:
    print(parser.usage)
else :
    def passwords(length=options.length):
            characters = options.characters
            return ''.join(random.choice(characters) for i in range(length))

    file = open(options.output+".txt", "w")

    num = 0
    while num < len(options.characters)*options.length :
        num += 1
        file = open(options.output+".txt", "a")
        file.write(options.characters+"\n")
        file.write(passwords()+"\n")
        file.close()
    lines    = options.length*len(options.characters)
    filesize = str(os.path.getsize(options.output+".txt"))
    time.sleep(0.3)
    print("""\033[1;33m
        Your wordlist has been successfully saved as """+options.output+".txt"+"""
        Number of lines :"""+" "+str(lines)+"""
        Wordlist size   :"""+" "+str(filesize)+" KB")
    print('\033[1;32m')
    playsound.playsound('sound.wav')
