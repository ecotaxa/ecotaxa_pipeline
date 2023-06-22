
from enum import Enum
from pathlib import Path, PurePath

from task import Task
















class define_sample_pipeline_folder(Task):

    _need_keys = ['pipeline_folder', 'sample_name']
    _update_keys = []
    _create_keys = ['raw_folder', 'work_folder', 'images_folder']

    def run(self, data):
        if  type(data['pipeline_folder']) == str:
            data['pipeline_folder'] = PurePath(data['pipeline_folder'])


        self.test_need_keys(data)
        # try:
        #     self._data['pipeline_folder'] = data['pipeline_folder']
        #     self._data['sample_name'] = data['sample_name']
        # except:
        #     raise("Missing key")
        

        self._define_keys()
        return self._data

    def _define_keys(self):
        self._data['raw_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_raw")
        self._data['work_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_work")
        self._data['images_folder'] = PurePath(self._data['raw_folder'], str(self._data['sample_name'] + "_Images"))


# class analyse_cvs(Task):
#     _need_keys = ['raw_folder', 'work_folder', 'cvs_list']
#     _update_keys = ['tsv_list']
#     _create_keys = [ 'CVSname_folder']

#     def __init__(self, )

class cvs_file_to_parse(Task):
    _need_keys = [ 'raw_folder', 'work_folder', 'file_type', 'mapping', 'filename_pattern']
    _update_keys = [ 'csv_list']
    _delete_keys = [ 'file_type', 'mapping', 'filename_pattern' ]

    def run(self, data):
        self.test_need_keys(data)
        self.addcsv()
        return self._data
    
    def addcsv(self):
        [ NamePatternComponent.eSampleName , "_" , NamePatternComponent.eIndex , "_Pulse" , ".cvs" ]
        filename = self._data['raw_folder']
        path = PurePath( self._data['raw_folder'] ,  )
        is_file_exist()
        csv_item = { }

    def build_name(self, file_pattern : list):
        pattern = file_pattern.copy()
        try:
            name_index = file_pattern.index(NamePatternComponent.eSampleName)
            pattern[name_index] = self._data['sample_name']
        except:
            pass
            raise("arg")
        path = "".join(pattern)
        return path

def is_file_exist(): pass


NamePatternComponent = Enum('NamePatternComponent', ['eSampleName' , 'eIndex', 'eImageType'])


mapping = {}
def build_name( data: dict, file_pattern : list):
    pattern = file_pattern.copy()
    try:
        name_index = file_pattern.index(NamePatternComponent.eSampleName)
        pattern[name_index] = str(data['sample_name'])
    except:
        raise("NamePatternComponent.eSampleName not found")
    path = "".join(pattern)
    return path

import unittest

class Test_Tasks(unittest.TestCase):

    def test_define_sample_pipeline_folder_missing_keys(self):
        
        data = { 'sample_name':'mySample' }

        ut = define_sample_pipeline_folder()
        self.assertRaises(BaseException, ut.run, data)

    def test_define_sample_pipeline_folder_(self):
        
        data = { 
            'pipeline_folder': '/pipeline_folder',
            'sample_name': 'mySample',
        }

        ut = define_sample_pipeline_folder()
        d = ut.run(data)

        self.assertEqual( d['pipeline_folder'], PurePath(data['pipeline_folder']))
        self.assertEqual( d['sample_name'], 'mySample')
        self.assertEqual( d['raw_folder'], PurePath(data['pipeline_folder'], data['sample_name'], "_raw"))
        self.assertEqual( d['work_folder'], PurePath(data['pipeline_folder'], data['sample_name'], "_work"))
        self.assertEqual( d['images_folder'], PurePath(data['pipeline_folder'], data['sample_name'], "_raw" , str(data['sample_name'] + "_Images")))

    def test_build_name(self):
        data = {'sample_name': 'mySample' }
        file_pattern = [ NamePatternComponent.eSampleName , "_Pulse" , ".cvs" ]
        
        ut = build_name(data, file_pattern)

        self.assertEqual(ut , str(data['sample_name']) + "_Pulse" + ".cvs" )

    def test_build_name2(self):
        data = {'sample_name': 'mySample' }
        file_pattern = [ NamePatternComponent.eSampleName , "_Pulse" , ".cvs" ]
        
        ut = build_name(data, file_pattern)

        self.assertEqual(ut , str(data['sample_name']) + "_Pulse" + ".cvs" )



if __name__ == '__main__':
    unittest.main()

