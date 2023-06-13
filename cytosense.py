


import os
from ParserToTsv import ParserToTsv
from Project import Project
from enums import Instrument
from pathlib import Path

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

    def analyse(self, filename):

        print("Analyse " + filename )

        self.filename = filename

        parser = ParserToTsv(self)
        parser.read_csv_filecyto( self.raw_data_path +"/"+filename + "_Pulses" + ".csv", self.project_path)


    def define_folders(self, name):
        imageName = Path(self.raw_data_path) / (name + "_Images") / (name + "_Cropped") # missing "_" + id + ".jpg"
        destFolder = Path(self.project_path) / "_work"
        return { 'destFolder':destFolder, 'imageName':imageName , 'tsvName':name }

    # def data_to_tsv_format(self, data):
    #     self.model.data_to_tsv_format(data)

    def data_to_tsv_format(self, data):
        # insert data in an array following mapping
        tsvrow = {}
        mapping = self.model.mapping
        for tsvkey in mapping:
            map = mapping[tsvkey]
            index = map['index']
            result = self.apply_fn(map['fn'], data[index])
            #tsvrow.append(result)
            tsvrow[tsvkey]=result
        return tsvrow

