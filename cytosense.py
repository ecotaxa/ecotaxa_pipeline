


import os
from ParserToTsv import ParserToTsv
from Project import Project
from enums import Instrument
from pathlib import Path
# from summarise_pulses import summarise_pulses

from tools import copy_to_file, order_dict
from tsv import Tsv

class CytoSense(Project):

    _read = []
    filename = ""
    data_filename = ""

    _tempTsv = {}
    _pulsesData = {}
    _listModeData = {}
    tsv = None

    delimiter = ","
    float_format="."

    def __init__(self, raw_data_path, data_to_export_base_path, cytoSense_model, title, type = "Cefas"):
    
        if type == "ULCO":
            self.delimiter = ";"
            self.float_format=","
    
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
        
    def filter(self, path):
        if not path.is_file():
            return False
        # print("hidden file: "+str(path.name)[0]+ " <== " + str(path.name))
        if str(path.name)[0]==".": return False
        # print("filter:"+str(path.name)[-4:])
        extension = str(path.name)[-4:]
        if extension == ".cyz" or extension == ".txt" or extension == ".zip":
            # print("eject")
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
                    # print("analysing")
                    filename = self.extract_name(strpath)
                    print("filename = " + filename)
                    if not filename in self._read:
                        self._read.append(filename )
                        self.analyse(filename)
                    else:
                        print("over: " + filename)
                else:
                    print("next "+ path.name)
                # if i > 5:
                #     break

    def rois_path(self):
        return  os.path.join(self.raw_data_path, "/")

    def analyse(self, filename):

        print("Analyse " + filename )

        self.filename = filename
        folder = self.define_folders(filename)

        self.data_filename = "Pulses"

        parser = ParserToTsv(self)
        # pulses_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
        # parser.read_csv_filecyto( pulses_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn"})
        pulses_filename = self.raw_data_path +"/../../"+ "pulse_fits" + ".csv"
        parser.read_csv_filecyto( pulses_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn2"})

        # poly = summarise_pulses(pulses_filename)

        self.data_filename = "Listmode"
        listmode_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
        parser.read_csv_filecyto( listmode_filename, self.project_path,{"delimiter":self.delimiter , "fn":"listModeRowFn"})

        # move in analyse (do it after scan the 3 files)
        # self._tsv = self.init_tsv()
        # tsvName = self._tsv.tsv_format_name( folder['tsvName'] )
        # self._tsv.generate_tsv(folder['destFolder'] / tsvName)

        self.copy_images(folder)

        self.store_data_in_tsv(folder)
    

    def copy_images(self, folder):
        for object_id in self._tempTsv.keys():
            cytosense_id=object_id.split("_")[-1:][0]
            images = self.images(cytosense_id)
            nbImages = 0  # must be < 10
            for i in images:
                nbImages += 1
                r = copy_to_file(Path(self.raw_data_path +"/"+folder['tsvName']+"_Images"+"/"+i), folder['destFolder'])
                if not r:
                    copy_to_file(Path("img/empty.jpg"), folder['destFolder'], True, i)
                if nbImages > 1:
                    self.add_rank(object_id, nbImages,images[i])

    def add_rank(self, id, rank, image):
        row = self._tempTsv[id]
        row['id_rank']=rank
        row['img_file_name']=image
        self._tempTsv[id+"_"+str(rank)]

    def store_data_in_tsv(self, folder):
        tsv = self.init_tsv()
        tsvName = tsv.tsv_format_name( folder['tsvName'] )
        for object_id in self._tempTsv.keys():
            row = self._tempTsv[object_id]
            self.data_to_tsv_format2(tsv, row)
            #tsv.addData(row)
        tsv.generate_tsv(folder['destFolder'] / tsvName , self._tempTsv) 

    def listModeRowFn(self, data: dict):
        id = data['object_id']
        self._listModeData[id] = data

    def pulseRowFn2(self, data: dict):
        id = data['object_id']
        self._pulsesData[id] = data

    def pulseRowFn(self, data: dict):
        id = data['object_id']
        if id in self._pulsesData:
            pulse = self._pulsesData[data['object_id']]
        else:
            pulse = { 'object_fws':[],"object_sws":[],"object_fl_erllow":[],"object_fl_orange":[],"object_fl_red":[],"object_curvature":[]}
        #pulse[]
        #concat signal

        # index = ['object_fws',"object_sws","object_fl_erllow","object_fl_orange","object_fl_red","object_curvature"]

        for i in pulse.keys():
            
            pulse[i].append(data[i])

        # update the pulse
        self._pulsesData[id] = pulse
    
    def store(self, name):
        if name == "Pulse":
            # if self._pulsesData['object_id'] in self._tempTsv:
            #     self._tempTsv[self._pulsesData['object_id']].update(self._pulsesData)
            # else:
            #     self._tempTsv[self._pulsesData['object_id']] = self._pulsesData
            for k in self._pulsesData:
                # self._tempTsv[self._listModeData['object_id']] = self._listModeData
                if k in self._tempTsv:
                    self._tempTsv[k].update(self._pulsesData)
                else:    
                    self._tempTsv[k] = self._pulsesData

        if name == "Mode":
            # if self._listModeData['object_id'] in self._tempTsv:
            #     self._tempTsv[self._listModeData['object_id']].update(self._listModeData)
            # else:
            for k in self._listModeData:
                # self._tempTsv[self._listModeData['object_id']] = self._listModeData
                if k in self._tempTsv:
                    self._tempTsv[k].update(self._listModeData)
                else:
                    self._tempTsv[k] = self._listModeData
            self._listModeData={}

    def images(self, index):
        i = [
            self.filename + "_" + "Cropped" + "_" + index + ".jpg",
            # self.filename + "_" + "Uncropped" + "_" + index + ".jpg",
        ]
        return i

    def rank(self, r):
        return 1

    def image(self, index):
        # return self.images(index)[0]
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
        
        # build the row
        for tsvkey in mapping:
            map = mapping[tsvkey]
            if tsvkey != 'object_id':
                if map['file'] != None:
                    if map['file'] != self.data_filename: continue

            index = map['index']

            result = self.apply_fn(map['fn'], data[index])

            if self.float_format == ',':
                if map['type']=='[f]':
                    # result = self.change_to_point(result)
                    result = str(result).replace(",", "." )
            
            #tsvrow.append(result)

            # print("data_to_tsv_format - add row: " + str(data[0]))
            tsvrow[tsvkey]=result

        # keyorder = self.model.keyorder()
        # rowResult = order_dict(tsvrow, keyorder )

        return tsvrow
        # return rowResult

    # def change_to_point(data):


    def data_to_tsv_format2(self, tsv: Tsv, data):
    # def data_to_tsv_format2(self, tsv: Tsv, dataKey):
        # insert data in an array following mapping
        # tsvrow = {}
        # result = []
        mapping = self.model.mapping
        print("data_to_tsv_format2 - data len ", len(data))
        for dataKey in data:
        # if not dataKey in data:
            result = []
            for tsvkey in mapping:
                d = data[dataKey]
                if tsvkey in d:
                    result.append(d[tsvkey])
                else:
                    print('missing key:' + tsvkey)
            
            #result.append(data[])
            print("data_to_tsv_format - add row: " +result[0])
            tsv.addData(result)
            
            #tsvrow.append(result)
            #tsvrow[tsvkey]=result

        # keyorder = self.model.keyorder()
        # rowResult = order_dict(tsvrow, keyorder )

        #return tsvrow
        #return rowResult



    def define_id(self, data):
        return self.filename + "_" + data
