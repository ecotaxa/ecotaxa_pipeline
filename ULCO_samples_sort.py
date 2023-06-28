

from enum import Enum
from pathlib import Path

from pipeline import Task
from test_pipeline import add_ulco_pulse_csv_file_to_parse
from tools import create_folder



class ulco_samples_sort(Task):
    '''
    Use this task
    When samples are on the same folder
    The samples are sort in different folder
    A folder contains pulse, listmode, infos files and an images folder
    '''

    # def __init__(self):
    #     pass
        
    def run(self, data : dict):
        try:
            self._source_folder = data['source_folder']
            self._destination_folder = data['destination_folder']
        except:
            raise("Missing arguments")

        self._copy_files()
        return self._data

    def _copy_files():
        pass    


class process_ulco_samples(Task):

    def run(self, data : dict):
        try:
            self._source_folder = data['source_folder']
            self._destination_folder = data['destination_folder']
            self._tasks = data['tasks']
        except:
            raise("Missing arguments")

        self._list_samples()
        return self._data

    def _list_samples(self):
        for sample in self._samples:
            sampleData = sample
            for task in self._tasks:
                self.data['sample'] = sampleData
                self._data = task.run(self._data)


class generate_ecotaxa_import(Task):
    pass


class analyse_cvs(Task):
    pass

class move_file_to_raw_folder(Task):
    pass

french_csv_configuration = { 'delimiter' : ';' , 'decimal' : ',' }
english_csv_configuration = { 'delimiter' : ',' , 'decimal' : '.' }




import Cytosense.define as cytosense


cefas_cytosense_pipeline = [
        move_file_to_raw_folder(cytosense.cefas_pulse_file_pattern_extra_info, cytosense.cefas_pulse_file_pattern),
        move_file_to_raw_folder(cytosense.cefas_listmode_file_pattern_extra_info, cytosense.cefas_listmode_file_pattern),
        analyse_cvs(cytosense.cefas_pulse_file_pattern, english_csv_configuration),
        analyse_cvs(cytosense.cefas_listmode_file_pattern, english_csv_configuration),
    ]

class cvs_file_to_parse(Task): pass

ulco_cytosense_pipeline = [

        # cvs_file_to_parse(filetype="PULSE", mapping={}, filename_pattern=ulco_pulse_file_pattern),
        add_ulco_pulse_csv_file_to_parse(),
        analyse_cvs(cytosense.ulco_pulse_file_pattern, french_csv_configuration),
        analyse_cvs(cytosense.ulco_listmode_file_pattern, french_csv_configuration),

    ]

ulco_samples_in_the_same_folder_pipeline = [

    ulco_samples_sort(),
    process_ulco_samples(ulco_cytosense_pipeline),
    generate_ecotaxa_import()
]

class define_sample_pipeline_folder(Task): pass

class define_sample_folder(Task):
    def __init__():
        pass

    def run(self, data):
        try:
            self._data['pipeline_folder'] = data['pipeline_folder']
            self._data['sample_folder'] = data['sample_folder']
            self._data['sample_name'] = data['sample_name']
        except:
            raise("Missing key")
        self.build_project_structure()
        return self._data

    def build_project_structure(self):
        task = define_sample_pipeline_folder()
        self._data = task.run(self._data)
        # self._data['raw_folder'] = Path.join(self._data['pipeline_folder'], self._data['sample_name'], "_raw")
        # self._data['work_folder'] = Path.join(self._data['pipeline_folder'], self._data['sample_name'], "_work")
        # self._data['images_folder'] = Path.join(self._data['raw_folder'], str(self._data['sample_name'], "_Images"))
        create_folder(self._data['raw_folder'])
        create_folder(self._data['work_folder'])

class copy_sample_in_pipeline_folder(Task):
    def run(self, data):
        try:
            _ = data['sample_folder']
            _ = data['raw_folder']
        except:
            raise("Missing key")
        self._copy_files()
        return self._data

    def _copy_files():
        pass




ulco_raw_sample_pipeline = [
    define_sample_folder(),
    copy_sample_in_pipeline_folder(),
]

ulco_sample_pipeline = [
    define_sample_pipeline_folder()] \
        .append(ulco_cytosense_pipeline)



