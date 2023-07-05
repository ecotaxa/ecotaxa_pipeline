


import glob
import os
from pathlib import PurePath
# import string
from Cytosense.define import NamePatternComponent
from Template import Template
from analyze_csv_pulse import analyse_csv, analyse_csv_cytosense_file
from build_file_name import build_file_name
from cytosenseModel import UlcoListmode, pulse
from debug_tools import dump

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



class analyse_cvs_listmode(analyse_csv_cytosense_file):
    import pandas as pd

    _need_keys = [ 'csv_listmode']
    _update_keys = ['tsv_list']
    _model = Template

    _df: pd.DataFrame

    def run(self):
        self._fileType = 'csv_listmode'
        self._analysing = self._data[self._fileType]
        self._model = self._analysing['mapping']
        self._df = self._init_df()
        self._add_type() # add type line after processing the data

        self.map_csv_to_df()


        self._data['tsv_listmode']={}
        self._data['tsv_listmode']['dataframe']= self._df

        # self.df.to_csv("tests/cytosense/result/test_analyze_csv_pulse.csv")
        self._df.to_csv("tests/test_analyze_csv_listmode.csv")



import pandas as pd

class merge_files(Task):

    _need_keys = ['tsv_pulse', 'tsv_listmode']
    _update_keys = ['tsv_list']

    def run(self):
        df_pulse = self._data['tsv_pulse']['dataframe']
        df_listmode = self._data['tsv_listmode']['dataframe']

        df : pd.DataFrame = pd.merge(df_pulse, df_listmode, how="inner", on=["object_id"])


        if not 'tsv_list' in self._data:  self._data['tsv_list'] = {}
        if not 'df_result' in self._data:  self._data['tsv_list']['df_result'] = {}
        self._data['tsv_list']['df_result']['dataframe'] = df


class list_images(Task):
    """
    list all the image found in the 'images' folder
    """
    _need_keys = ['raw_folder', 'sample_name', 'images_folder']
    _create_keys = ['image_list']
    _update_keys = ['dataframe']

    def __init__(self, **kwargs):
        if 'pattern_name' in kwargs:
            self.image_name_pattern = kwargs['pattern_name']
        else:
            raise Exception("Argument missing 'pattern_name'")
        
    def filter(self,filename) -> bool:
        
        

        return True
    
    def make_key_from_image_name(self, filename:str) -> str:
        filename_less_extension = os.path.splitext(filename)[0]
        key = filename_less_extension.replace('_Cropped','')
        return key
    
    def run(self):
    
        image_list = {}
    
        image_path = self._data['images_folder']

        image_file_list = self.list_files(image_path, self.image_name_pattern)


        for image in image_file_list:
            # image_data={}
            filename=PurePath(image).name
            
            # key=os.path.splitext(filename)[0]  # Bad key 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_4206' must be 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_4206'
            key = self.make_key_from_image_name(filename)    

            # image_data["key"]= key
            # image_data["filename"]= str(filename)
            # image_data["path"]= PurePath(image)

            image_data = {
                'key': key,
                'filename': str(filename),
                'path': PurePath(image)
            }

            image_list[key]= image_data

        # dump(image_file_list)
        self._data['image_list']=image_list

    def list_files(self, from_path:PurePath, pattern=[]) -> list:
        path_pattern = "*"
        if len(pattern) != 0:
            ut = build_file_name(pattern)
            path_pattern = ut.get_name(eSampleName=self._data['sample_name'], eIndex="*")
        dir_path = PurePath(from_path, path_pattern)
        dump(dir_path)
        file_list = glob.glob(str(dir_path))
        return file_list



class trunc_data():
    """
    trunc the listmode and pulses data from image list
    if image don't exist we don't need the data. Ecotaxa need an image.
    """
    def run(self):
        pass
