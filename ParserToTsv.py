# Sebastien Galvagno 06/2023

import csv
from tools import eprint

from tools import copy_to_file, create_folder

import re

class ParserToTsv:

    def __init__(self, project):
        self._model = project
        self._tsv = self._model.init_tsv()

    def read_csv_file(self, file_name, dest_path):
        print ("processing: " + file_name)
        with open(file_name,"r") as fp:
            reader = csv.reader( fp )

            #for data in reader:
            line = -1
            while True:
                line +=1
                try:
                    data = next(reader)
                except StopIteration:
                    break
                except csv.Error:
                    eprint("Cannot read file \"" + file_name + "\" at line " + str(line))
                    continue
                except IOError:
                    continue
                else:
                    # to filtering the commented line, 
                    # in the sample data we have a file named 20191202.roicoordswithheader.txt 
                    # that contain the header
                    if data[0][0] == "#" or data[0][0] == "^@":
                        continue
                    imageName = data[2]
                    folder = self._model.define_folders(imageName)
                    
                    create_folder(folder['destFolder'])

                    additionaldata = self._model.additionnal_process(folder['imageName']) #TODO change function name

                    status = copy_to_file( folder['imageName'], folder['destFolder'])
                    #print("status:" + str(status) )

                    if status:
                        tsvrow = self._model.data_to_tsv_format(data)
                        tsvrow.update(additionaldata)
                        self._tsv.addData(tsvrow)

            #tsvName = self.id(name) + ".tsv"
            tsvName = self._tsv.tsv_format_name( folder['tsvName'] )
            self._tsv.generate_tsv(folder['destFolder'] / tsvName)


def read_csv_file(self, file_name, dest_path, fn):
        print ("processing: " + file_name)
        with open(file_name,"r") as fp:
            reader = csv.reader( fp )

            #for data in reader:
            line = -1
            while True:
                line +=1
                try:
                    data = next(reader)
                except StopIteration:
                    break
                except csv.Error:
                    eprint("Cannot read file \"" + file_name + "\" at line " + str(line))
                    continue
                except IOError:
                    continue
                else:
                    # to filtering the commented line, 
                    # in the sample data we have a file named 20191202.roicoordswithheader.txt 
                    # that contain the header
                    if fn['filter']:
                        continue
                    imageName = data[2]
                    folder = self._model.define_folders(imageName)
                    
                    create_folder(folder['destFolder'])

                    additionaldata = self._model.additionnal_process(folder['imageName']) #TODO change function name

                    status = copy_to_file( folder['imageName'], folder['destFolder'])
                    #print("status:" + str(status) )

                    if status:
                        tsvrow = self._model.data_to_tsv_format(data)
                        tsvrow.update(additionaldata)
                        self._tsv.addData(tsvrow)

            #tsvName = self.id(name) + ".tsv"
            tsvName = self._tsv.tsv_format_name( folder['tsvName'] )
            self._tsv.generate_tsv(folder['destFolder'] / tsvName)


def read_txt_file(self, file_name):
    print ("processing: " + file_name)

    data = {}
    with open(file_name, "r") as fp:
        for l_no, line in enumerate(fp):

            s = line.split(":")
            data[s[0]]= s[1]
        

        
    tsvrow = self._model.data_to_tsv_format(data)
    return tsvrow
        

def info_file(self, path):

    data = {}

    with open(path,'r') as fp:
        for l_no, line in enumerate(fp):
            pass


def apply_fn(self, fn, data):
    if fn is None: 
        return data
    cls = self
    try:
        method = getattr(cls, fn)
        return method(data)
    except AttributeError:
        raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))