


import os
from ParserToTsv import ParserToTsv
from Project import Project
from enums import Instrument
from pathlib import Path

from tools import order_dict

class CytoSense(Project):

    def __init__(self, raw_data_path, data_to_export_base_path, cytoSense_model, title):
        super().__init__(raw_data_path, data_to_export_base_path, cytoSense_model, title, Instrument.CYTOSENSE)
        

    def copy_raw_data(self):
        #TODO
        pass

    def define_id(self, data):
        return self.folder['destFolder'] + data
    
    def extract_name(self, path):
        # print("extract_name() " + path)
        splitname = path.split("_")
        string_to_cut = splitname[len(splitname)-1]
        filename = path[:-len(string_to_cut)-1]
        #print("extract :" + filename)
        return str(filename)
        
    _read = []

    def filter(self, path):
        if not path.is_file():
            return False
        print("hidden file: "+str(path.name)[0]+ " <== " + str(path.name))
        if str(path.name)[0]==".": return False
        print("filter:"+str(path.name)[-4:])
        extension = str(path.name)[-4:]
        if extension == ".cyz" or extension == ".txt":
            print("eject")
            return False
        return True

    def process_project(self):
            
            os.DirEntry
            i = 0
            for path in os.scandir(self.raw_data_path):
                i+=1
                strpath = path.name
                print("found file:" + strpath)
                if self.filter(path):
                    print("analysing")
                    filename = self.extract_name(strpath)
                    print("filename = " + filename)
                    if not filename in self._read:
                        self.analyse(filename)
                else:
                    print("next")
                if i > 5:
                    break

    def rois_path(self):
        return  os.path.join(self.raw_data_path, "/")

    filename = ""
    data_filename = ""

    def analyse(self, filename):

        print("Analyse " + filename )

        self.filename = filename
        folder = self.define_folders(filename)

        self.data_filename = "Pulses"

        parser = ParserToTsv(self)
        parser.read_csv_filecyto( self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv", self.project_path,{"delimiter":";"})


        # move in analyse (do it after scan the 3 files)
        self._tsv = self.init_tsv()
        tsvName = self._tsv.tsv_format_name( folder['tsvName'] )
        self._tsv.generate_tsv(folder['destFolder'] / tsvName)

    _tsv = None

    def image(self, index):
        return self.filename + "_" + "Cropped" + "_" + index + ".jpg"

    def define_folders(self, name):
        imageName = Path(self.raw_data_path) / (name + "_Images") / (name + "_Cropped") # missing "_" + id + ".jpg"
        destFolder = Path(self.project_path) / "_work"
        return { 'destFolder': destFolder, 'imageName': imageName , 'tsvName': name }

    # def data_to_tsv_format(self, data):
    #     self.model.data_to_tsv_format(data)

    def data_to_tsv_format(self, data):
        # insert data in an array following mapping
        tsvrow = {}
        mapping = self.model.mapping
        for tsvkey in mapping:
            map = mapping[tsvkey]
            if tsvkey != 'object_id':
                if map['file'] != None:
                    if map['file'] != self.data_filename: continue

            index = map['index']
            result = self.apply_fn(map['fn'], data[index])
            #tsvrow.append(result)
            tsvrow[tsvkey]=result

        # keyorder = self.model.keyorder()
        # rowResult = order_dict(tsvrow, keyorder )

        return tsvrow
        # return rowResult

    def define_id(self, data):
        return self.filename + "_" + data
