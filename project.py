# Sebastien Galvagno 06/2023
import os
from Parser.Template import Template
from Tools.tools import create_folder
from tsv import Tsv 


class Project:
     
    def __init__(self, project : dict):
          
        try: 
            self.project_name = project['name']
            #self.raw_data_folder = project['raw_data_folder']
            #self.work_data_folder = project['work_data_folder']
            self.project_path = project['path']
            self.raw_data_folder = os.path.join(self.project_path, "_raw")
            self.work_data_folder = os.path.join(self.project_path, "_work")
            self.pipeline = project['pipeline']
            self.metadata = project['metadata']
        except:
            raise Exception("missing key in project argument")

    def generate_project_architecture(self) :
        create_folder(self.project_path) 
        create_folder(self.raw_data_folder)
        create_folder(self.work_data_folder)

class Project2:
    def __init__(self, raw_data_path, data_to_export_base_path, model : Template, title, instrument):
        self.raw_data_path = raw_data_path
        self.project_path = os.path.join(data_to_export_base_path, title)
        self.model = model
        self.title = title
        self.instrument = instrument
        # create _raw in destination project path and copy the entire raw folder from raw_data_path
        self.generate_project_architecture()

    def generate_project_architecture(self) :
        create_folder(self.project_path) 
        create_folder(os.path.join(self.project_path, "_raw"))
        create_folder(os.path.join(self.project_path, "_work"))

    @property 
    def keyorder(self):
        return self.model.keyorder

    # def data_to_tsv_format(self, data):
    #     # insert data in an array following mapping
    #     tsvrow = []
    #     mapping = self.model.mapping
    #     for tsvkey in mapping:
    #         map = mapping[tsvkey]
    #         index = map['index']
    #         result = self.apply_fn(map['fn'], data[index])
    #         tsvrow.append(result)
    #     return tsvrow

    @property
    def mapping(self):
        return self.model

    def id(self, data):
        k = self.model.key('object_id')
        # pri#nt(k)
        v = k['index']
        return data[v]


    def additionnal_process(self, data):
            #TODO add here image processing
            pass

    def import_in_ecotaxa(self):
        #TODO
        pass


    def apply_fn(self, fn, data):
        if fn is None: 
                return data
        cls = self
        try:
            #print("call: " + fn)
            method = getattr(cls, fn)
            return method(data)
        except AttributeError:
            raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))

    def init_tsv(self):
        tsv = Tsv()
        mapping = self.model.mapping
        for k in mapping:
            t = mapping[k]['type'] #todo add function in model to do that
            tsv.add_feature("",k,t) # TODO: replace "" by None
        return tsv

    def define_folders(self, name):
        pass

    def define_id(self, data):
        pass

