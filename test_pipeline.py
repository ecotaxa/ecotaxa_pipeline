
from pathlib import Path, PurePath
from Cytosense.define import NamePatternComponent
from analyze_csv_pulse import analyze_csv_pulse
from cytosenseModel import pulse
from debug_tools import dump
from mock_polynomial_pulses_ulco_small_data import mock_ulco_dataframe, mock_ulco_small_data
from mock_ulco_small_data_images import mock_trunc
import pipeline
from summarise_pulses import CSVException

import pandas as pd

#from pipeline import Pipeline__
# from pipeline import define_sample_pipeline_folder

from task import Task
# from tasks import add_ulco_pulse_csv_file_to_parse, define_sample_pipeline_folder


from pathlib import PurePath
from task import Task
from tasks import add_ulco_listmode_csv_file_to_parse, add_ulco_pulse_csv_file_to_parse, analyse_cvs_listmode, define_sample_pipeline_folder, list_images, merge_files, summarize_csv_pulse, trunc_data


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


    # test fail cannot mock is_file_exist
    def test_fail_ulco_pipeline_task_lists(self):

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


    # test fail cannot mock is_file_exist
    def test_fail_ulco_pipeline_array_of_tasks_embedded(self):

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
        # self.assertEqual(result['csv_pulse']['path'].as_posix(), PurePath(test_path).as_posix())
        self.assertEqual(result['csv_pulse']['path'], PurePath(test_path))


    def test_ulco_pipeline_analyse_pulse_ulco_mock(self):
        from csv_configuration import french_csv_configuration

        # import ULCO_samples_sort as ulco    

        local_path = PurePath('tests/cytosense/ULCO/mock')
        data = {
            'pipeline_folder': local_path,
            'sample_name': 'R4_photos_flr16_2uls_10min 2022-09-14 12h28',
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(french_csv_configuration),
            summarize_csv_pulse(),
            # analyse_csv( ulco.ulco_pulse_file_pattern, ulco.french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        # self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
        #                                         'mapping': pulse,
        #                                         'path': PurePath('/pipeline_folder/mySample/_raw/mySample_Pulses.csv')})

        self.assertEqual(result['csv_pulse']['filename'], 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_Polynomial_Pulses.csv', "filename different")

        test_path = 'tests/cytosense/ULCO/mock/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Polynomial_Pulses.csv'
        self.assertEqual(result['csv_pulse']['path'], PurePath(test_path), "path different")


    def test_ulco_pipeline_analyse_pulse_ulco_small_mock_wrong_delimiter(self):

        # import ULCO_samples_sort as ulco    
        from csv_configuration import french_csv_configuration

        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        data = {
            'pipeline_folder': PurePath(local_path),
            'sample_name': sample_name,
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
            summarize_csv_pulse(),
            # analyse_csv( ulco.ulco_pulse_file_pattern, ulco.french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        utlambda = lambda : ut.run(data)

        self.assertRaises(CSVException, utlambda)


    def test_ulco_pipeline_analyse_pulse_ulco_small_mock(self):

        # import ULCO_samples_sort as ulco    
        from csv_configuration import french_csv_configuration

        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        data = {
            'pipeline_folder': PurePath(local_path),
            'sample_name': sample_name,
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(french_csv_configuration),
            summarize_csv_pulse(),
            # analyse_csv( ulco.ulco_pulse_file_pattern, ulco.french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        # self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
        #                                         'mapping': pulse,
        #                                         'path': PurePath('/pipeline_folder/mySample/_raw/mySample_Pulses.csv')})

        self.assertEqual(result['csv_pulse']['filename'], sample_name + '_Polynomial_Pulses.csv', "filename different")

        test_path = local_path + '/' + sample_name + '_Polynomial_Pulses.csv'
        self.assertEqual(result['csv_pulse']['path'], PurePath(test_path), "path different")



    def test_ulco_pipeline_ulco_small_mock(self):

        # import ULCO_samples_sort as ulco    
        from csv_configuration import french_csv_configuration

        mock = mock_ulco_small_data()
        # local_path = mock.local_path
        # sample_name = mock.sample_name
        # dftest = mock.df
        # local_path = 'tests/cytosense/ULCO/mock_small_data'
        # sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        data = {
            'pipeline_folder': PurePath(mock.local_path),
            'sample_name': mock.sample_name,
        }
        

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(french_csv_configuration),
            add_ulco_listmode_csv_file_to_parse(french_csv_configuration),
            summarize_csv_pulse(),
            analyze_csv_pulse(),
            analyse_cvs_listmode(),
            # analyse_csv( ulco.ulco_pulse_file_pattern, ulco.french_csv_configuration),
            #analyse_csv(ulco_listmode_file_pattern, french_csv_configuration),
        ]

        # grammar pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        # self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
        #                                         'mapping': pulse,
        #                                         'path': PurePath('/pipeline_folder/mySample/_raw/mySample_Pulses.csv')})

        # self.assertEqual(result['csv_pulse']['filename'], sample_name + '_Polynomial_Pulses.csv', "filename different")
        # test_path = local_path + '/' + sample_name + '_Polynomial_Pulses.csv'
        # self.assertEqual(result['csv_pulse']['path'], PurePath(test_path), "path different")
        self.assertEqual( result['csv_pulse']['filename'], mock.polynomial_filename , " -- Different polynomail pulses filename" )
        self.assertEqual( result['csv_pulse']['path'],  PurePath( mock.local_path , mock.polynomial_filename ), " -- Different polynomail pulses path" ) 


        # self.assertEqual(result['csv_listmode']['filename'], mock.sample_name + '_Listmode.csv', "filename different")
        # test_path = mock.local_path + '/' + mock.sample_name + '_Listmode.csv'
        # self.assertEqual(result['csv_listmode']['path'], PurePath(test_path), "path different")

        self.assertEqual( result['csv_listmode']['filename'], mock.listmode_filename , " -- Different listmode filename" )
        self.assertEqual( result['csv_listmode']['path'],  PurePath( mock.local_path , mock.listmode_filename ), " -- Different listmode path" )

        import pandas as pd
        df: pd.DataFrame = result['tsv_pulse']['dataframe']
        from pandas.testing import assert_frame_equal        
        assert_frame_equal( df, mock.df )


    def test_ulco_pipeline_ulco_small_mock_merge(self):

        # import ULCO_samples_sort as ulco    
        from csv_configuration import french_csv_configuration

        mock = mock_ulco_dataframe()
        data = {
            'pipeline_folder': PurePath(mock.local_path),
            'sample_name': mock.sample_name,
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(french_csv_configuration),
            add_ulco_listmode_csv_file_to_parse(french_csv_configuration),
            summarize_csv_pulse(),
            analyze_csv_pulse(),
            analyse_cvs_listmode(),
            merge_files()
        ]

        # grammar: pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        self.assertIn('tsv_list',result, " -- 'tsv_list' don't exist")
        self.assertIn('df_result',result['tsv_list'], " -- 'df_result' don't exist")
        self.assertIn('dataframe',result['tsv_list']['df_result'], " -- 'dataframe' don't exist")
        df_result : pd.DataFrame = result['tsv_list']['df_result']['dataframe']

        df_result.to_csv("tests/cytosense/result/" + mock.sample_name + "__merge_p_l__.csv", index=False)

        dump(df_result.to_dict() )
        dump(mock.df.to_dict() )

        from pandas.testing import assert_frame_equal        

        dump(df_result['object_coef_0_FWS'].to_dict())
        dump(mock.df['object_coef_0_FWS'].to_dict())

        l = df_result['object_coef_0_FWS'].to_dict()
        r = mock.df['object_coef_0_FWS'].to_dict()

        # dump(df_result['object_coef_0_FWS'].dtypes)
        # dump(mock.df['object_coef_0_FWS'].dtypes)
        dump(l)
        dump(r)


        # arrgg fail because l has float value and r has str value in their columns
        self.assertDictEqual(l, r)

        assert_frame_equal( df_result, mock.df )


    def test_ulco_pipeline_ulco_small_mock_trunc(self):

        # import ULCO_samples_sort as ulco    
        from csv_configuration import french_csv_configuration

        mock = mock_trunc()
        data = {
            'pipeline_folder': PurePath(mock.local_path),
            'sample_name': mock.sample_name,
        }

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(french_csv_configuration),
            add_ulco_listmode_csv_file_to_parse(french_csv_configuration),
            summarize_csv_pulse(),
            analyze_csv_pulse(),
            analyse_cvs_listmode(),
            merge_files(),
            list_images(pattern_name=[NamePatternComponent.eSampleName,"_Cropped_",NamePatternComponent.eIndex,".jpg"]),
            trunc_data()
        ]

        # grammar: pipeline = [ Task | [ Task ] ]
        ulco_sample_pipeline_tasks = [ define_sample_pipeline_folder(), 
                                       ulco_cytosense_pipeline 
                                    ]

        ut = pipeline.Pipeline(ulco_sample_pipeline_tasks)
        result = ut.run(data)

        self.assertIn('tsv_list',result, " -- 'tsv_list' don't exist")
        self.assertIn('df_result',result['tsv_list'], " -- 'df_result' don't exist")
        self.assertIn('dataframe',result['tsv_list']['df_result'], " -- 'dataframe' don't exist")
        df_result : pd.DataFrame = result['tsv_list']['df_result']['dataframe']

        csv_filename = mock.sample_name + "__df_result" + ".csv"
        cvs_path = PurePath(mock.result_folder, csv_filename)
        df_result.to_csv("cvs_path", sep=',', decimal='.') 

        from pandas.testing import assert_frame_equal        
        assert_frame_equal( df_result, mock.df )

        # assert "Need to" == "finish this test"


if __name__ == '__main__':
    unittest.main()

