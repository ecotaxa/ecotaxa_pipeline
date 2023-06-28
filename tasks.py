


from pathlib import PurePath
from cytosenseModel import pulse

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

    def run(self, data):
        self.test_need_keys(data)
        self.process()
        self.remove_keys()
        return self._data

    def build_name(self):
        return PurePath( self._data['raw_folder'], str(self._data['sample_name'] + "_PolynomialPulse" + ".csv"))

    def process(self):

        pulses_filename = self._data['csv_pulse']['path']
        poly_dataframe = self.summarise_pulses_function(pulses_filename)
        poly_filename = self.build_name()
        self.save_dataframe_to_csv(poly_dataframe, poly_filename)
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

    def run(self, data):
        self.test_need_keys(data)
        self.addcsv()
        self.remove_keys()
        return self._data

    def addcsv(self):

        global is_file_exist
        filename = self.build_name()
        path = PurePath( self._data['raw_folder'], filename )
        if not tools.is_file_exist(path): 
            raise "File " + str(path) + "do not exist"
        csv_item = { 
                'path': path, 
                'filename':  filename, 
                'mapping': pulse,
                'csv_configuration': self._csv_configuration
                }
        self._data['csv_pulse']= csv_item 

    def build_name(self):
        # ulco.ulco_pulse_file_pattern : [ NamePatternComponent.eSampleName , "_Pulse" , ".csv" ]
        return self._data['sample_name'] + "_Pulse.csv"








class define_sample_pipeline_folder(Task):

    _need_keys = ['pipeline_folder', 'sample_name']
    # _update_keys = []
    _create_keys = ['raw_folder', 'work_folder', 'images_folder']

    def run(self, data):
        if  type(data['pipeline_folder']) == str:
            data['pipeline_folder'] = PurePath(data['pipeline_folder'])


        self.test_need_keys(data)
        # try:
        #     self._data['pipeline_folder'] = data['pipeline_folder']
        #     self._data['sample_name'] = data['sample_name']
        # except:
        #     raise "Missing key"
        

        self._define_keys()
        return self._data

    def _define_keys(self):
        self._data['raw_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_raw")
        self._data['work_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_work")
        self._data['images_folder'] = PurePath(self._data['raw_folder'], str(self._data['sample_name'] + "_Images"))






