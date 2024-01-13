"""
Parse the Info.txt Cytosense file
"""

from pathlib import PurePath
from typing import Dict, Tuple
from Pipeline.Exception.ExecuteException import ExecuteException
from Pipeline.Exception.MappingException import MappingException
from Parser.Template import Template
from DebugTools.debug_tools import dump
from Pipeline.task import Task
import re
import pandas as pd
import Cytosense.cytosenseModel as cytosenseModel



class add_info_file_task(Task):

    _need_keys = ['raw_folder', 'sample_name']
    _update_keys = ['txt_infos']

    _init_params = ['model','localisation']

    def __init__(self, **kwargs):

        for argument in self._init_params:
            if argument in kwargs:
                self.__setattr__(argument, kwargs[argument])
            else:
                raise Exception(f"Missing argument: '{argument}' - when you called {self.__class__.__name__}")
        
        # if 'model' in kwargs:
        #     self.model = kwargs['model']
        #     self.__setattr__('model', kwargs['model'])
        # else:
        #     raise Exception("Argument missing 'model'")
        
    def run(self):

        filename = self._data['sample_name'] + "_Info.txt"

        path = PurePath(self._data['raw_folder'] , filename )

        self._data['txt_infos'] = {} 
        self._data['txt_infos']['mapping'] = self.model
        self._data['txt_infos']['csv_configuration'] = self.localisation
        self._data['txt_infos']['path'] = path


class parse_Infos(Task):
    
    _need_keys = ['txt_infos'] # ['txt_infos|path','txt_infos|csv_configuration']
    _update_keys = ['df_list'] # ['df_list|txt_infos']

    regex = ""

    # labels = {'Channel 2', 'Smart triggered number of particles', 'Channel 4', 'Trigger level (mV)', 'Flow rate (μL/sec)', 'Measurement date', 'Channel 1', 'Instrument', 'Beam width', 'Core speed', 'Concentration (part/μL)', 'Volume (μL)', 'CytoUSB Block size', 'Channel 7', 'Channel 3', 'Channel 5', 'User Comments', 'Channel 6', 'Measurement duration', 'Total number of particles'}
    # sublabels = {'sensitivity level'}

    def _init_df(self) -> pd.DataFrame:
        df = pd.DataFrame(columns=[key for key in self._model._mapping])
        # for key in self._model._mapping :
        #     # if key:
        #     df[key] =  self._model._mapping[key]['type']
        return df
    
    # def __init__(self) -> None:
    #     super().__init__()
    #     self._model = cytosenseModel.Info()

    #     self._mapping = self._model._mapping
    #     # _model.search_header
    #     self._init_df()

    _model : Template = None
    
    def run(self):
        self._fileType = 'txt_infos'
        self._analysing = self._data[self._fileType]
        self._model  = self._analysing['mapping']

        filename = self._data['txt_infos']['path']
        localisation = self._data['txt_infos']['csv_configuration']
        row = self.read(filename,localisation)

        df = self._init_df()
        df.loc[len(df)]= row

        if not 'df_list' in self._data:
            self._data['df_list'] = {}
        self._data['df_list']['txt_infos'] = df



    # def read(self,filename,csv_configuration) -> pd.DataFrame:
    def read(self,filename,csv_configuration) -> Dict[str,dict]:

        with open(filename, mode="r", encoding="utf-8-sig" ) as fp:
            # lines = fp.readlines()
            lines = fp.read().splitlines()

        row = {}
        for linenumber, line in enumerate(lines):
            print(linenumber, line)
            if len(line)==0:continue

            splittedline = line.split(':',1)
            if len(splittedline)<=1: continue

            # header = splittedline[0]
            header,fileValue = splittedline

            if header == "  - sensitivity level":
                print("  - sensitivity level")

            # fileValue = splittedline[1]

            fileValue = fileValue.strip()
            # if len(fileValue)==0: continue

            # if ( csv_configuration['decimal'] == ','):
            #     fileValue = fileValue.replace(',','.')    

            # fileValue = self._model.cast_value(header)       

            tuples = self.map_row(self._model, (header,fileValue) )
            # df.loc[len(df)]= row
            if tuples == None:
                print("zrggggg")
                continue
            for tuple in tuples:
                key, value = tuple
                if 'index' in self._model._mapping[key] and self._model._mapping[key]['index'] == linenumber+1:
                    row[key] = value
        
        return row


    def map_row(self, model: Template, data: Tuple[str,str], paragraph = False) -> list[Tuple]:
            '''
            a key in the file can map several ecotaxa keys
            '''
    # def map_row(self, model: Template, data: Tuple[str,str]): # -> Tuple(str,str|int|float):
            header, fileValue = data
            ecotaxaKeys = model.searchKeyFromFileHeader(header)

            if len(ecotaxaKeys) == 0:
                if paragraph == True:
                    paragraph = False
                else:
                    raise Exception(f"key mapping not found: {header}")

            # row = {}
            rows = []
            for key in ecotaxaKeys:

                # paragraph = False
                if 'paragraph' in self._model._mapping[key] : paragraph = True
                
                fn = model.fn(key)
                if fn:
                    try:
                        fn = model.fn(key)
                        value = self.apply_fn(fn, fileValue)
                        # row[key] = model.cast_value(model,key,value,decimal=self._analysing['csv_configuration']['decimal'])
                        # row[key] = model.cast_value(key,value,decimal=self._analysing['csv_configuration']['decimal'])
                        value = model.cast_value(key, value, decimal=self._analysing['csv_configuration']['decimal'])
                        rows.append( (key, value) )
                    except ExecuteException as e:
                        # tools.eprint("Mapping issue: Function `{}` called in mapping `{}` is not implemented".format(e.functionNamefn, self._mapping))
                        raise MappingException(executeException=e, model=self._model, line=(key,value), result=rows)
                else:
                    # row[key] = model.cast_value(model,key,fileValue,decimal=self._analysing['csv_configuration']['decimal'])
                    # row[key] = model.cast_value(key,fileValue,decimal=self._analysing['csv_configuration']['decimal'])
                    value = model.cast_value(key, fileValue, decimal=self._analysing['csv_configuration']['decimal'])
                    rows.append( (key, value) )
            
            return rows


    def apply_fn(self, function, data):
        if function == None: 
                return data
        # cls = self
        cls = self._model
        try:
            method = getattr(cls, function)
            return method(self._model, data, self)
        except AttributeError:
            # raise 
            # raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))
            # tools.eprint("Function `{}` called in mapping `{}` is not implemented".format(fn, self._mapping))
            raise ExecuteException(cls.__class__.__name__, function)
            # return data



    def generate_label_list(self,filename) -> list:

        labels =  set()
        sublabels = set()
        prefix = "  - "

        with open(filename, mode="r", encoding="utf-8-sig" ) as fp:
            # lines = fp.readlines()
            lines = fp.read().splitlines()

        # Show the file contents line by line.
        # We added the comma to print single newlines and not double newlines.
        # This is because the lines contain the newline character '\n'.
        for linenumber, line in enumerate(lines):
            print(linenumber, line)
            if len(line)==0:continue

            splittedline = line.split(':',1)
            if len(splittedline)==0: continue

            label = splittedline[0]

            if label.startswith(prefix):
                label = label.removeprefix(prefix)
                sublabels.add(label)
            else:
                labels.add(label)

        dump(labels)        
        dump(sublabels)    
        return (list(labels),list(sublabels))







class cross_merge_task(Task):

    _need_keys = ['tsv_list','df_list'] # ['tsv_list|df_result|dataframe','df_list|txt_infos']
    _update_keys = ['tsv_list|df_result|dataframe']


    def run(self):
        
        df = self._data['tsv_list']['df_result']['dataframe']
        df_info = self._data['df_list']['txt_infos']

        df = pd.merge(df, df_info, how="cross")

        self._data['tsv_list']['df_result']['dataframe'] = df

    



# keysText = System.Text.RegularExpressions.Regex.Match(textData,"(?<=serial open request)(.*\n)*(?=DCU E72)",RegexOptions.IgnoreCase).Value.ToString.Trim

def generate_label_list():
    t = parse_Infos()
    local_path = "tests/cytosense/ULCO/mock_small_data"
    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    filesubname = "_Info.txt"
    filename = sample_name + filesubname
    path = PurePath( local_path, filename)
    labels, subLabels = t.generate_label_list(path)

    labels.sort()
    subLabels.sort()
    dump(labels)         
    dump(subLabels)

def test():
    t = parse_Infos()
    local_path = "tests/cytosense/ULCO/mock_small_data"
    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    filesubname = "_Info.txt"
    csv_configuration = { "decimal" : ',' }
    filename = sample_name + filesubname
    path = PurePath( local_path, filename)
    df = t.read(path, csv_configuration)
    df.to_csv("tests/cytosense/results/" + filename )

if __name__ == '__main__':
    # generate_label_list()
    test()