

from enum import Enum


class Task():
    pass

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

french_csv_configuration = { 'delimiter' : ';' , 'decimal' : ',' }
english_csv_configuration = { 'delimiter' : ',' , 'decimal' : '.' }

ulco_cytosense_pipeline = [
    analyse_cvs(french_csv_configuration)
]

NamePatternComponent = Enum('NamePatternComponent', ['eSampleName' , 'eIndex'])

FileExtension - Enum ( 'FileExtension', [] )

pulse_file_pattern = [ NamePatternComponent.eSampleName , "_" , NamePatternComponent.eIndex , "_Pulse" , ".cvs" ]

cefas_cytosense_pipeline = [
        analyse_cvs(english_csv_configuration)

]

ulco_samples_in_the_same_folder_pipeline = [

    ulco_samples_sort(),
    process_ulco_samples(ulco_cytosense_pipeline),
    generate_ecotaxa_import()
]

