# Sebastien Galvagno

import os
import sys
import subprocess
from pathlib import Path



def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def copyFileTo(filename: Path, subFolder):
    #TODO to move in a tool class
    if not os.path.exists(filename):
        eprint("file don't exist: " + str(filename.absolute()))
        return False
    if os.stat(filename).st_size == 0:
        eprint("file is empty: " + str(filename.absolute()))
        return False
    try:
        subprocess.run(["cp", filename, subFolder], check=True, capture_output=True)
    except:
        eprint("cannot copy file: " + str(filename.absolute()))
        return False
    return True

def createFolder(path):
    #TODO to move in a tool class
    if not os.path.isdir(path):
        os.mkdir(path)


def printDict(d:dict, title=""):
    if title != "":
        print(title)
    for k in d:
        s = ""
        for v in d[k]:
            s = s + v + ":" + str(d[k][v]) + ","
        print( k + " -> " + s)