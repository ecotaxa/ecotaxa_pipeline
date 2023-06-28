
from pathlib import Path, PurePath
from cytosenseModel import pulse
import pipeline

#from pipeline import Pipeline__
# from pipeline import define_sample_pipeline_folder

from task import Task
# from tasks import add_ulco_pulse_csv_file_to_parse, define_sample_pipeline_folder


from pathlib import PurePath
from task import Task
from tasks import add_ulco_pulse_csv_file_to_parse, define_sample_pipeline_folder



# class analyse_csv(Task):
#     _need_keys = ['raw_folder', 'work_folder', 'cvs_list']
#     _update_keys = ['tsv_list']
#     _create_keys = [ 'CVSname_folder']

#     def __init__(self, )

# def is_file_exist_mooc_true(path): return True
# def is_file_exist_mooc_false(path): return False





# class cvs_file_to_parse(Task):
#     _need_keys = [ 'raw_folder', 'sample_name'] #, 'work_folder', 'file_type', 'mapping', 'filename_pattern']
#     _update_keys = [ 'csv_list']

# import tools


# class cvs_file_to_parse2(Task):
#     _need_keys = [ 'raw_folder', 'sample_name'] #, 'work_folder', 'file_type', 'mapping', 'filename_pattern']
#     _update_keys = [ 'csv_list']
#     #_delete_keys = [ 'file_type', 'mapping', 'filename_pattern' ]

#     is_file_exist = tools.is_file_exist

#     def __init__(self, **kwargs):
#         #super().__init__()
#         need = ['file_type', 'mapping', 'filename_pattern', 'buildname_fn']
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#             try:
#                 index = need.index(key)
#                 need.remove(key)
#             except: pass
#         if len(need)>0: raise Exception("Missing arguments: " + ",".join(need))

#     def run(self, data):
#         self.test_need_keys(data)
#         self.addcsv()
#         self.remove_keys()
#         return self._data
    
#     def addcsv(self):
#         filename = self.build_name(self._data['file_pattern'])
#         path = PurePath( self._data['raw_folder'], filename )
#         if not self.is_file_exist(path): raise Exception( "File " + str(path) + "do not exist")
#         csv_item = { 'path': path, 'filename':  filename, 'mapping': self._data['mapping'] }
#         csv_list = { self._data['file_type'] : csv_item }

#     def build_name(self):
#         # [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
#         pattern = self.filename_pattern.copy()
#         try:
#             name_index = pattern.index(NamePatternComponent.eSampleName)
#             pattern[name_index] = self._data['sample_name']
#         except:
#           raise Exception( "NamePatternComponent.eSampleName not found" )

#         path = "".join(pattern)
#         return path

#     # def build_name(self):
#     #     # [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
#     #     pattern = self.filename_pattern.copy()
#     #     try:
#     #         name_index = pattern.index(NamePatternComponent.eSampleName)
#     #         pattern[name_index] = self._data['sample_name']
#     #     except:
#     #         pass
#     #         #raise Exception("pattern " + )
#     #     path = "".join(pattern)
#     #     return path







# mapping = {}




 
class analyse_csv(Task):
    pass

import unittest




class Test_Pipeline(unittest.TestCase):

    def test_ulco_pipeline_missing_data(self):

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
        ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder()]    
        ulco_sample_pipeline_tasks.append(ulco_cytosense_pipeline)

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        self.assertRaises(Exception, ut.run )


    def test_ulco_pipeline_task_lists(self):

        data = { 
            'pipeline_folder': '/pipeline_folder',
            'sample_name': 'mySample',
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
        ]

        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder() ]
        ulco_sample_pipeline_tasks  = ulco_sample_pipeline_tasks + ulco_cytosense_pipeline

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
                                                'mapping': pulse,
                                                'path': PurePath('/pipeline_folder/mySample/_raw/mySample_Pulses.csv')})
        
    def test_ulco_pipeline_array_of_tasks_embedded(self):

        data = { 
            'pipeline_folder': '/pipeline_folder',
            'sample_name': 'mySample',
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
            #analyse_csv(ulco_pulse_file_pattern, french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]    

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
                                                'mapping': pulse,
                                                'path': PurePath('/pipeline_folder/mySample/_raw/mySample_Pulses.csv')})
        
    
    # def test_ulco_pipeline__pulse_analyse(self):
    def test_ulco_pipeline__on_test_sample(self):

        local_path = PurePath('tests/cytosense/ULCO/mock')
        data = {
            'pipeline_folder': local_path,
            'sample_name': 'R4_photos_flr16_2uls_10min 2022-09-14 12h28',
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
            #analyse_csv(ulco_pulse_file_pattern, french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]    
        try:
            ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        except Exception as e:
            print("dir:")
            print(e.__dir__)
            print("trace:")
            print(e.with_traceback)
            raise Exception("Issue to initialise Pipeline")

        try:
            result = ut.run(data)
        except Exception as e:
            print("dir:")
            print(e.__dir__)
            print("trace:")
            print(e.with_traceback)
            raise Exception("Issue during running Pipeline")

        # self.assertEqual(result['csv_pulse'],  {'filename': 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_Pulses.csv',
        #                                         'mapping': pulse,
        #                                         'path': PurePath('tests/cytosense/mock/_raw/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Pulses.csv')})
        
        self.assertEqual(result['csv_pulse']['filename'], 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_Pulses.csv')
        # self.assertEqual(result['csv_pulse']['mapping'], pulse)

        print("['csv_pulse']['path']" + str(result['csv_pulse']['path']))
        test_path = 'tests/cytosense/ULCO/mock/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Pulses.csv'
        self.assertEqual(result['csv_pulse']['path'].as_posix(), PurePath(test_path).as_posix())
        self.assertEqual(result['csv_pulse']['path'], PurePath(test_path))


    def test_ulco_pipeline_analyse_pulse_ulco(self):

        import ULCO_samples_sort as ulco    

        data = { 
            'pipeline_folder': '/pipeline_folder',
            'sample_name': 'mySample',
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
            analyse_csv( ulco.ulco_pulse_file_pattern, ulco.french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
                                                'mapping': pulse,
                                                'path': PurePath('/pipeline_folder/mySample/_raw/mySample_Pulses.csv')})
        


if __name__ == '__main__':
    unittest.main()

