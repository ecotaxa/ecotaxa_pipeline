

from Template import Template
from task import Task
from csv_configuration import english_csv_configuration

class add_csv_to_parse(Task):
    _need_keys = [ 'raw_folder', 'sample_name']
    _update_keys = [ 'file_list']

    def __init__(self, model: Template , pattern_name: str , csv_configuration = english_csv_configuration ):
        self._csv_configuration = csv_configuration
        self._pattern = pattern_name
        self._model = model

    def run(self):
        pass