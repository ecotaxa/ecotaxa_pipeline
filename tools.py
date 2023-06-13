# Sebastien Galvagno

import os
import sys
import subprocess
from pathlib import Path



def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def copy_to_file(filename: Path, subFolder):
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

def create_folder(path: Path):
    #print("create folder" + path)
    p = Path(path)
    try :
        if not os.path.isdir(path):
            #os.mkdir(path)
            #os.makedirs(path, exist_ok=True)
            p.mkdir(parents=True, exist_ok=True)
    except OSError as error: 
        path_str = str(p.absolute)

        eprint("cannot create folder : " + path_str +", "+ str(error))



def print_dict(d:dict, title=""):
    if title != "":
        print(title)
    for k in d:
        s = ""
        for v in d[k]:
            s = s + v + ":" + str(d[k][v]) + ","
        print( k + " -> " + s)

