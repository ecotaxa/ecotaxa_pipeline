
from pathlib import PurePath
from Cytosense.cytosenseModel import pulse
from Pipeline.task import Task
import Tools.tools as tools
# import ULCO_samples_sort as ulco    
from Localization.csv_configuration import french_csv_configuration, english_csv_configuration

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
