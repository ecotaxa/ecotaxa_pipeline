
from pathlib import PurePath
from Cytosense.cytosenseModel import UlcoListmode
from Pipeline.task import Task
import Tools.tools as tools
from Localization.csv_configuration import english_csv_configuration

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
        
     


