# Sebastien Galvagno 

import os
from pathlib import Path
import subprocess


from Project import Project
from tsv import Tsv 
#from cpicsModel import cpicsModel
from tools import createFolder
from ParserToTsv import ParserToTsv


# ../../aux2/20191125.aux.dat  
# 20191125.roicoords.txt 
# ../../logs/20191125.syslog.txt

class CPICsProject(Project):
    def __init__(self, path, roisModel):
        super().__init__(path,roisModel)

    def roisPath(self):
        return self.path+"/rois/ROICoord/"

    def generateProject(self,projectPath):
        createFolder(projectPath)

        roisPath = self.roisPath()
        for path in os.scandir(roisPath):
            if path.is_file():
                filename = path.name
                parser = ParserToTsv(self)
                parser.readCVSFile( self.roisPath()+filename, projectPath)

    def extractSubNumber(self,name):
        suf = name.split('_',1)[1]
        return suf.split(".",1)[0]
    
    def defineSubFolder(self,name):
        return name[0]+name[1]+"00"




    def defineFolders(self,name,destPath):
        dateFolder = name.split('_',1)[0]
        subNumber = self.extractSubNumber(name)
        subFolder = dateFolder + "_" + self.defineSubFolder(subNumber)

        imageName = Path(self.path) / "rois" / dateFolder / subFolder / name
        destFolder = Path(destPath) / dateFolder
        return { 'destFolder':destFolder, 'imageName':imageName , 'tsvName':dateFolder }


    def dataToTsvFormat(self,data):
        # insert data in an array following mapping
        tsvrow = []
        mapping = self.model.getMapping()
        for tsvkey in mapping:
            rois = mapping[tsvkey]
            index = rois['index']
            result = self.applyFn(rois['fn'], data[index])
            tsvrow.append(result)

        return tsvrow

    def additionnalProcess(self, data):
        #TODO add here image processing
        pass

    def applyFn(self,fn,data):
        if fn is None: 
                return data
        cls = self
        try:
            method = getattr(cls, fn)
            return method(data)
        except AttributeError:
            raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))

    def initTsv(self):
        tsv = Tsv()
        mapping = self.model.getMapping()
        for k in mapping:
            t = mapping[k]['type'] #todo add function in model to do that
            tsv.add_feature("",k,t) # TODO: replace "" by None
        return tsv



    #2019/11/25 21:50:15.277
    def date(self,data):
        return data[:4]+data[5:7]+data[8:10]

    def time(self,data):
        return str(int(data[11:13])*60+int(data[14:16]))


    def dateFromName(self,name):
        dict = self.deconstructCpicsFileName(name)
        return dict['year']+dict['month']+dict['day']

    def timeFromName(self,name):
        dict = self.deconstructCpicsFileName(name)
        return str(int(dict['hour'])*60)+dict['min']

    def id(self,name):
        return name[:-4]

    def deconstructCpicsFileName(self,filename):
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




