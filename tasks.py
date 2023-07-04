


from pathlib import PurePath
# import string
from Cytosense.define import NamePatternComponent
from Template import Template
from cytosenseModel import UlcoListmode, pulse

from task import Task


class summarize_csv_pulse(Task):

    _need_keys = ['raw_folder', 'csv_pulse', 'sample_name']
    _update_keys = ['csv_pulse']


    import summarise_pulses
    save_dataframe_to_csv = summarise_pulses.save_dataframe_to_csv
    summarise_pulses_function = summarise_pulses.summarise_pulses

    # def __init__(self, summarise_pulses_function = summarise_pulses.summarise_pulses):
    #     # import summarise_pulses
    #     # self.summarise_pulses_function = summarise_pulses_function if summarise_pulses_function else summarise_pulses.summarise_pulses
    #     self.summarise_pulses_function = summarise_pulses_function

    _filename = lambda self: str(self._data['sample_name'] + "_Polynomial_Pulses" + ".csv")

    def build_name(self):
        return PurePath( self._data['raw_folder'], self._filename() )

    def run(self):
    #     self.test_need_keys(data)
    #     self.process()
    #     self.remove_keys()
    #     return self._data

  
    # def process(self):
        import summarise_pulses

        pulses_filename = self._data['csv_pulse']['path']
        # poly_dataframe = self.summarise_pulses_function(pulses_filename)
        poly_dataframe = summarise_pulses.summarise_pulses(pulses_filename, csv_configuration=self._data['csv_pulse']['csv_configuration'])
        poly_filename = self.build_name()
        self._data['csv_pulse']['filename'] = self._filename()
        # self.save_dataframe_to_csv(poly_dataframe, poly_filename)
        summarise_pulses.save_dataframe_to_csv(poly_dataframe, poly_filename, csv_configuration=french_csv_configuration)
        self._data['csv_pulse']['path'] = poly_filename


import tools
# import ULCO_samples_sort as ulco    
from csv_configuration import french_csv_configuration, english_csv_configuration

class add_ulco_pulse_csv_file_to_parse(Task):
    _need_keys = [ 'raw_folder', 'sample_name']
    _update_keys = [ 'csv_pulse']

    is_file_exist = tools.is_file_exist

    def __init__(self, csv_configuration = english_csv_configuration):
        self._csv_configuration = csv_configuration

    def run(self):
    #     self.test_need_keys(data)
    #     self.addcsv()
    #     self.remove_keys()
    #     return self._data

    # def addcsv(self):

        global is_file_exist
        filename = self.build_name()
        path = PurePath( self._data['raw_folder'], filename )
        if not tools.is_file_exist(path): 
            raise Exception( "File " + str(path) + " do not exist")
        csv_item = { 
                'path': path, 
                'filename':  filename, 
                'mapping': pulse,
                'csv_configuration': self._csv_configuration
                }
        self._data['csv_pulse']= csv_item 

    def build_name(self):
        # ulco.ulco_pulse_file_pattern : [ NamePatternComponent.eSampleName , "_Pulses" , ".csv" ]
        return self._data['sample_name'] + "_Pulses.csv"


class add_csv_to_parse(Task):
    _need_keys = [ 'raw_folder', 'sample_name']
    _update_keys = [ 'file_list']

    def __init__(self, model: Template , pattern_name: str , csv_configuration = english_csv_configuration ):
        self._csv_configuration = csv_configuration
        self._pattern = pattern_name
        self._model = model

    def run(self):
        pass

class add_ulco_listmode_csv_file_to_parse(Task):
    _need_keys = [ 'raw_folder', 'sample_name']
    _update_keys = [ 'csv_listmode']

    is_file_exist = tools.is_file_exist

    def __init__(self, csv_configuration = english_csv_configuration):
        self._csv_configuration = csv_configuration

    def run(self):

        global is_file_exist
        filename = self.build_name()
        path = PurePath( self._data['raw_folder'], filename )
        if not tools.is_file_exist(path): 
            raise Exception( "File " + str(path) + " do not exist")
        csv_item = { 
                'path': path, 
                'filename':  filename, 
                'mapping': UlcoListmode,
                'csv_configuration': self._csv_configuration
                }
        self._data['csv_listmode'] = csv_item 

    def build_name(self):
        # ulco.ulco_pulse_file_pattern : [ NamePatternComponent.eSampleName , "_Pulses" , ".csv" ]
        return self._data['sample_name'] + "_Listmode.csv"
        
     





class define_sample_pipeline_folder(Task):

    _need_keys = ['pipeline_folder', 'sample_name']
    # _update_keys = []
    _create_keys = ['raw_folder', 'work_folder', 'images_folder']

    def _run(self, data):
        if  type(data['pipeline_folder']) == str:
            data['pipeline_folder'] = PurePath(data['pipeline_folder'])
            self._data = super()._run(data)
            return self._data

    def run(self):
    #     if  type(data['pipeline_folder']) == str:
    #         data['pipeline_folder'] = PurePath(data['pipeline_folder'])


    #     self.test_need_keys(data)
    #     # try:
    #     #     self._data['pipeline_folder'] = data['pipeline_folder']
    #     #     self._data['sample_name'] = data['sample_name']
    #     # except:
    #     #     raise Exception( "Missing key")
        

    #     self._define_keys()
    #     return self._data

    # def _define_keys(self):
        # self._data['raw_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_raw")
        # self._data['work_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_work")
        # self._data['images_folder'] = PurePath(self._data['raw_folder'], str(self._data['sample_name'] + "_Images"))
        self._data['raw_folder'] = PurePath(self._data['pipeline_folder'])
        self._data['work_folder'] = PurePath(self._data['pipeline_folder'], "_work" ,self._data['sample_name'])
        self._data['images_folder'] = PurePath(self._data['raw_folder'], str(self._data['sample_name'] + "_Images"))



import pandas as pd

class analyze_csv_pulse(Task):

    _need_keys = [ 'csv_pulse']
    _update_keys = ['tsv_list']
    _model = Template

    _df: pd.DataFrame

    def run(self):
        self._model = self._data['csv_pulse']['mapping']
        self._df = self._init_df()
        self._add_type() # add type line after processing the data

        self.map_csv_to_df()


        self._data['tsv_pulse']={}
        self._data['tsv_pulse']['dataframe']= self._df

        # self.df.to_csv("tests/cytosense/result/test_analyze_csv_pulse.csv")
        self._df.to_csv("tests/test_analyze_csv_pulse.csv")


    def _add_type(self):
        """
        the second header line: the line indicating types
        """
        row = {}
        print("len:", len(self._model._mapping))
        for key in self._model._mapping:
            print("mapping["+key+"]=" + str(self._model._mapping[key]['type']))
            row[key] = self._model._mapping[key]['type']
        self._df.loc[0]=row


    def _init_df(self) -> pd.DataFrame:
        df = pd.DataFrame(columns=[key for key in self._model._mapping])
        for key in self._model._mapping :
            # if key:
            df[key] =  self._model._mapping[key]['type']
        return df


    def line_filter(self, line: str):
        # remove the header line
        # processing to verify mapping could be done when the header line has been found
        # and/or simply fill the index column in mapping dict
        if line.startswith("Particle ID"): 
            self.council_headers(line)
            return False
        return True

    def cast_value(self,key,value:str):
        if self._model._mapping[key]['type'] == "[t]":
            return str(value)

        if self._model._mapping[key]['type'] == "[f]":
            if self._data['csv_pulse']['csv_configuration']['decimal'] == ',':
                value = value.replace(',','.')
            if '.' in value:
                return float(value)
            else:
                return int(value)
        
        raise Exception("Unknow type: {} for key: {} mapping", self._model._mapping[key]['type'], key)

    def map_row(self,line_as_array: list[str]) -> dict:
        row = {}
        raised = False
        for key, value in self._data['csv_pulse']['mapping']._mapping.items():
            if 'index' in value:
                index = value['index']
                if 'fn' in value:
                    try:
                        result = self.apply_fn(value['fn'], line_as_array[index])
                        row[key] = self.cast_value(key,result)
                    except ExecuteException as e:
                        # tools.eprint("Mapping issue: Function `{}` called in mapping `{}` is not implemented".format(e.functionNamefn, self._mapping))
                        row[key] = line_as_array[index]
                        # raise MappingException(excuteException=e, mapping = self._data['csv_pulse']['mapping'], line=(key,value))
                        raised = True
                else:
                    row[key] = self.cast_value(key, line_as_array[index])
        if raised:
            raise MappingException(executeException=e, model=self._data['csv_pulse']['mapping'], line=(key,value), result=row)
        return row


    # marche pas , SUR JE CHERCHE SUR LA CLEF alors qu'il faut chercher sur la donnée
    # def council_headers_booo(self, header):

    #     line_as_array = header.split(self._data['csv_pulse']['csv_configuration']['delimiter'])

    #     for ecotaxa_key in self._model._mapping:
    #         try:
    #             search_csv_key = self._model._mapping[ecotaxa_key]['header']
    #             search_csv_key = {i for i in self._model._mapping if self._model._mapping[ecotaxa_key]['header']=="_______"}

    #             index = int(line_as_array.index(search_csv_key))
    #             self._model._mapping[ecotaxa_key]['index']= index
    #             print("changed {} ".format(ecotaxa_key))
    #         except:
    #             print(ecotaxa_key)
    #             print(search_csv_key)
    #             tools.eprint("Cannot find ",search_csv_key," in mapping of ", ecotaxa_key)
    #             tools.eprint("\t", self._model._mapping[ecotaxa_key])
    
    #     print(self._model._mapping)

    def build_invert_key(self):

        self._dict_csv_ecotaxa = {}
        for ecotaxa_key in self._model._mapping:
            ecotaxa_value = self._model._mapping[ecotaxa_key]
            csv_key = ecotaxa_value['header']
            self._dict_csv_ecotaxa[csv_key]=ecotaxa_key

    def council_headers(self, header):

        line_as_array = header.split(self._data['csv_pulse']['csv_configuration']['delimiter'])
        # line_as_array = list(map(string.strip,line_as_array))
        line_as_array = [item.strip() for item in line_as_array] 

        self.build_invert_key()

        for cvs_key in line_as_array:
            try:
                # search_csv_key = self._model._mapping[ecotaxa_key]['header']
                # search_ecotaxa_key = {i for i in self._model._mapping if self._model._mapping[i]['header']=="cvs_key"}
                ecotaxa_key = self._dict_csv_ecotaxa[cvs_key]

                index_in_csv_header = int(line_as_array.index(cvs_key))
                self._model._mapping[ecotaxa_key]['index']= index_in_csv_header
                print("changed {} ".format(ecotaxa_key))
            except:
                print(cvs_key)
                tools.eprint("Cannot find ", cvs_key)

            #     print(ecotaxa_key)
            #     tools.eprint("Cannot find ",cvs_key," in mapping of ", ecotaxa_key)
            #     tools.eprint("\t", self._model._mapping[ecotaxa_key])
    
        print(self._model._mapping)



    def map_csv_to_df(self) -> pd.DataFrame:
            lines: list[str] = []
        # try :
            with open(self._data['csv_pulse']['path']) as f:
                lines = f.readlines()
            # new_rows=[]
            for line_number, line in enumerate(lines) : 
                print("{}: {}".format(line_number,line) )
                # avoid empty or comments lines
                line = line.rstrip('\n')

                if self.line_filter(line):
                    line_as_array = line.split(self._data['csv_pulse']['csv_configuration']['delimiter'])
                    line_as_array = [item.strip() for item in line_as_array] 
                     #list(map(string.strip,line_as_array))

                    new_row={}
                    try:
                        new_row = self.map_row(line_as_array)
                    except MappingException as e:
                        tools.eprint("Mapping issue: line number {} - Function `{}` called in mapping is not implemented\n{}".format(line_number, e.functionName, e.line))
                        # if e.result:
                        #     new_row = e.result
                        continue

                    # new_rows.append(new_row)
                    self._df.loc[len(self._df)]= new_row
            # if len(new_rows)>0:
            #     self._df = pd.concat([self._df, pd.DataFrame(new_rows)], ignore_index=True)
        # except UnicodeDecodeError as ude :
        #     print(ude)
        # except KeyError as key:
        #     keyValue = key.args[0]
        #     if keyValue == 'index':
        #         raise Exception("Your cvs ")

        # except Exception as e:
        #     print(e)
        
        # print(df)
        # return df


    def apply_fn(self, fn, data):
        if fn is None: 
                return data
        cls = self
        try:
            method = getattr(cls, fn)
            return method(data)
        except AttributeError:
            # raise 
            # raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))
            # tools.eprint("Function `{}` called in mapping `{}` is not implemented".format(fn, self._mapping))
            raise ExecuteException(cls.__class__.__name__, fn)
            # return data


class ExecuteException(Exception):
    def __init__(self, className, functionName):
        self.className = className
        self.functionName = functionName
        
    def message(self) -> str:
        return "Class `{}` does not implement `{}`".format(self.className, self.functionName)


class MappingException(Exception):
    executeException: ExecuteException = None
    className = ""
    functionName = ""
    # line : tuple(str, list[str]) = (None, [])
    line = None
    model : Template = None
    result : dict = None

    def __init__(self, **kwargs: object) -> None:
        if 'excuteException' in kwargs:
            self.executeException = kwargs['excuteException']
            self.className = self.executeException.className
            self.functionName = self.executeException.functionName
        # if 'line' in kwargs:
        #     self.line = kwargs['line']
        if 'model' in kwargs:
            self.model = kwargs['model']   
        if 'result' in kwargs:
            self.result = kwargs['result'] 
    
    def message(self) -> str:
        return "Mapping issue in model {}: Function `{}` called in mapping of `{}` is not implemented".format(self.model.name, self.functionNamefn, self.line[0])

