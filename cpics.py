# Sebastien Galvagno 

import os
from pathlib import Path

from Project import Project
# from tsv import Tsv 
#from cpicsModel import cpicsModel
# from tools import create_folder
from ParserToTsv import ParserToTsv
from Ecotaxa.enums import Instrument


# ../../aux2/20191125.aux.dat  
# 20191125.roicoords.txt 
# ../../logs/20191125.syslog.txt

class CPICsProject(Project):
    def __init__(self, raw_data_path, data_to_export_base_path, roisModel, title):
        super().__init__(raw_data_path, data_to_export_base_path, roisModel, title, Instrument.CPICS)

    def rois_path(self):
        return  os.path.join(self.raw_data_path, "cpics/rois/ROICoord/")
    
    def copy_raw_data(self):
        #TODO
        pass


    def filter_row(self,data):
        if data[0][0] == "#" or data[0][0] == "^@":
            return True
        return False

    def process_project(self):
        rois_path = self.rois_path()
        for path in os.scandir(rois_path):
            if path.is_file():
                filename = path.name
                parser = ParserToTsv(self)
                parser.read_csv_file( self.rois_path()+filename, self.project_path)

    def extract_sub_number(self, name):
        suf = name.split('_',1)[1]
        return suf.split(".",1)[0]
    
    def define_sub_folder(self,name):
        return name[0]+name[1]+"00"

    def define_folders(self, name):
        dateFolder = name.split('_',1)[0]
        subNumber = self.extract_sub_number(name)
        subFolder = dateFolder + "_" + self.define_sub_folder(subNumber)
        imageName = Path(self.raw_data_path) / "cpics" / "rois" / dateFolder / subFolder / name
        destFolder = Path(self.project_path)/ "_work" / dateFolder
        return { 'destFolder':destFolder, 'imageName':imageName , 'tsvName':dateFolder }


    # def data_to_tsv_format(self, data):
    #     # insert data in an array following mapping
    #     tsvrow = []
    #     mapping = self.model.mapping
    #     for tsvkey in mapping:
    #         rois = mapping[tsvkey]
    #         index = rois['index']
    #         result = self.apply_fn(rois['fn'], data[index])
    #         tsvrow.append(result)
    #         return tsvrow

    # def additionnal_process(self, data):
    #     #TODO add here image processing
    #     pass

    # def import_in_ecotaxa(self):
    #     #TODO
    #     pass


    # def apply_fn(self, fn, data):
    #     if fn is None: 
    #             return data
    #     cls = self
    #     try:
    #         method = getattr(cls, fn)
    #         return method(data)
    #     except AttributeError:
    #         raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))

    # def init_tsv(self):
    #     tsv = Tsv()
    #     mapping = self.model.mapping
    #     for k in mapping:
    #         t = mapping[k]['type'] #todo add function in model to do that
    #         tsv.add_feature("",k,t) # TODO: replace "" by None
    #     return tsv



    #2019/11/25 21:50:15.277
    def date(self, data):
        return data[:4]+data[5:7]+data[8:10]

    def time(self,data):
        return str(int(data[11:13])*60+int(data[14:16]))


    def date_from_name(self, name):
        dict = self.deconstructCpicsFileName(name)
        return dict['year']+dict['month']+dict['day']

    def time_from_name(self, name):
        dict = self.deconstructCpicsFileName(name)
        return str(int(dict['hour'])*60)+dict['min']

    def id(self, name):
        return name[:-4]

    def deconstruct_cpics_file_name(self, filename):
        #returns a dictonaring with the deconstructed filename
        #20190726_121131.773.1.png
        year = filename[:4]
        month = filename[4:6]
        day  = filename[6:8]
        hour  = filename[9:11]
        minute = filename[11:13]
        second = filename[13:15]
        millisecond = filename[16:19]
        imageNumber = filename[20:-4]
        d_filename = dict([('year',year), ('month', month), ('day', day), 
                        ('hour', hour), ('minute', minute),('second', second),
                        ('millisecond', millisecond),
                        ('imageNumber', imageNumber)])
        return d_filename

#Date,Time,Name,Position upper leftx,Position upper lefty,Position lower rightx,Position lower rightY,Temperature,Conductivity,Pressure,Depth,Salinity,Sound Velocity,local density




