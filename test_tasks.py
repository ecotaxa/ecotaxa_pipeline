

from pathlib import PurePath
import unittest
from Cytosense.define import NamePatternComponent
from Template import Template
from analyze_csv_pulse import analyze_csv_pulse
from cytosenseModel import UlcoListmode, pulse
from debug_tools import dump, myDictAssert
from mock_polynomial_pulses_ulco_small_data import mock_ulco_dataframe, mock_ulco_small_data
from mock_ulco_small_data_images import mock_trunc, mock_ulco_small_data_images
from tasks import add_ulco_listmode_csv_file_to_parse, add_ulco_pulse_csv_file_to_parse, analyse_cvs_listmode, copy_images_task, define_sample_pipeline_folder, list_images, merge_files, summarize_csv_pulse, trunc_data

# from tasks import add_ulco_pulse_csv_file_to_parse, define_sample_pipeline_folder, summarize_csv_pulse

import pandas as pd



summarize_called = 0
summarize_file = None
save_called = 0

def summarize_pulses_function(path):
    global summarize_called, summarize_file
    summarize_called += 1
    summarize_file = path

def save_csv(dataframe, path):
    global save_called
    save_called += 1

class summarize_csv_pulse_test(summarize_csv_pulse):

    def __init__(self):
        # super().__init__(summarize_csv_pulse_test.summarize_pulses_function)
        super().__init__()
        self.summarise_pulses_function = summarize_pulses_function
        self.save_dataframe_to_csv = save_csv



def build_name( data: dict, file_pattern : list):
    pattern = file_pattern.copy()
    try:
        # name_index = file_pattern.index(NamePatternComponent.eSampleName)
        name_index = pattern.index(NamePatternComponent.eSampleName)
        pattern[name_index] = str(data['sample_name'])
    except:
        raise Exception( "NamePatternComponent.eSampleName not found" )
    path = "".join(pattern)
    return path



def build_name_kw( **kwargs):
    try:
        file_pattern = kwargs['file_pattern']
        sample_name = kwargs['sample_name']
    except: raise Exception("Missing arguments")
    pattern = file_pattern.copy()
    try:
        # name_index = file_pattern.index(NamePatternComponent.eSampleName)
        name_index = pattern.index(NamePatternComponent.eSampleName)
        pattern[name_index] = sample_name
    except:
        raise Exception( "NamePatternComponent.eSampleName not found" )
    name = "".join(pattern)
    return name


def build_name_ulco_pulse_filename(data):
    # pattern = [ NamePatternComponent.eSampleName , "_Pulses" , ".cvs" ]
    # try:
    #     # name_index = file_pattern.index(NamePatternComponent.eSampleName)
    #     name_index = pattern.index(NamePatternComponent.eSampleName)
    #     pattern[name_index] = str(data['sample_name'])
    # except:
    #     raise Exception( "NamePatternComponent.eSampleName not found" )
    # path = "".join(pattern)
    # return path
    return data['sample_name'] + "_Pulses.csv"




class Test_Tasks(unittest.TestCase):

    result_path = "tests/cytosense/result/"

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
        d = ut._run(data)

        self.assertIsNotNone(d)
        self.assertEqual( d['pipeline_folder'], PurePath(data['pipeline_folder']))
        self.assertEqual( d['sample_name'], 'mySample')
        # self.assertEqual( d['raw_folder'], PurePath(data['pipeline_folder'], data['sample_name'], "_raw"))
        # self.assertEqual( d['work_folder'], PurePath(data['pipeline_folder'], data['sample_name'], "_work"))
        # self.assertEqual( d['images_folder'], PurePath(data['pipeline_folder'], data['sample_name'], "_raw" , str(data['sample_name'] + "_Images")))
        self.assertEqual( d['raw_folder'], PurePath(data['pipeline_folder']))
        self.assertEqual( d['images_folder'], PurePath(data['pipeline_folder'], str(data['sample_name'] + "_Images")))

    def test_build_name(self):
        data = {'sample_name': 'mySample' }
        file_pattern = [ NamePatternComponent.eSampleName , "_Pulses" , ".cvs" ]
        
        ut = build_name(data, file_pattern)

        self.assertEqual(ut , str(data['sample_name']) + "_Pulses" + ".cvs" )

    def test_build_name2(self):
        data = {'sample_name': 'mySample' }
        file_pattern = [ NamePatternComponent.eSampleName , "_Pulses" , ".cvs" ]
        
        ut = build_name(data, file_pattern)

        self.assertEqual(ut , str(data['sample_name']) + "_Pulses" + ".cvs" )

    def test_build_name_kw(self):
        file_pattern = [ NamePatternComponent.eSampleName , "_Pulses" , ".csv" ]
        sample_name= 'mySample'
        ut = build_name_kw( sample_name = sample_name, file_pattern = file_pattern)

        self.assertEqual(ut , sample_name + "_Pulses" + ".csv" )

    def test_build_name_ulco_pulse_filename(self):
        data = {'sample_name': 'mySample' }
        ut = build_name_ulco_pulse_filename(data)
        self.assertEqual(ut,"mySample_Pulses.csv")




    # def test_cvs_file_to_parse_missing_argument(self):
    #     # ut = cvs_file_to_parse(filetype="filetype", mapping={}, filename_pattern="filename_pattern")
    #     self.assertRaises(Exception, cvs_file_to_parse, mapping={}, filename_pattern="filename_pattern")

    # def test_cvs_file_to_parse_bad_name__argument(self):
    #     # ut = cvs_file_to_parse(filetype="filetype", mapping={}, filename_pattern="filename_pattern")
    #     self.assertRaises(Exception, cvs_file_to_parse, filetype="filetype", mapping={}, filename_pattern="filename_pattern")


    # def test_cvs_file_to_parse(self):

    #     mapping={}
    #     filename_pattern = [ NamePatternComponent.eSampleName , "_Pulses" , ".csv" ]
    #     filename=""

    #     data = { 
    #             'raw_folder': PurePath('/_raw'),
    #             'work_folder': PurePath('/_work'),
    #             # 'file_type': 'PULSE', 
    #             # 'mapping':mapping,
    #             # 'filename_pattern': file_pattern
    #         }
    #     filetype="PULSE"

    #     ut = cvs_file_to_parse(file_type=filetype, mapping=mapping, filename_pattern=filename_pattern)
        
    #     self.assertEqual(filetype, ut.file_type)
    #     self.assertEqual(mapping, ut.mapping)
    #     self.assertEqual(filename_pattern, ut.filename_pattern)

    #     self.assertEqual(filename, ut.build_name())


    def test_fail_change_function(self):

        myLambda = lambda : True # is_file_exist_mooc_true

        ut = add_ulco_pulse_csv_file_to_parse()
        ut.is_file_exist = myLambda
        self.assertEqual(myLambda , ut.is_file_exist)

    # test have an issue, cannot mock is_file_exist()
        data = { 
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample'
        }

        ut = add_ulco_pulse_csv_file_to_parse()
        ut.is_file_exist = lambda path: True
        result = ut._run(data)

        self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulses.csv',
                                                'mapping': pulse,
                                                'path': PurePath('/_raw/mySample_Pulses.csv')})


    def test_add_ulco_pulse_csv_file_to_parse_true_cefas_file(self):
        from csv_configuration import english_csv_configuration

        local_path = 'tests/cytosense/Cefas/mock'
        sample_name = 'Pond_NA 2023-05-24 09h23_All Imaged Particles'
        data = {
            'raw_folder': PurePath(local_path),
            'sample_name': sample_name,
        }
        test_filename = sample_name + "_Pulses.csv"
        test_path = local_path + "/" + test_filename

        ut = add_ulco_pulse_csv_file_to_parse(english_csv_configuration)
        result = ut._run(data)

        self.assertEqual(result['csv_pulse']['filename'],  test_filename , " -- filename different")
        self.assertEqual(result['csv_pulse']['mapping'],  pulse , " -- mapping different")
        self.assertEqual(result['csv_pulse']['path'],  PurePath(test_path) , " -- path different")
        self.assertEqual(result['csv_pulse']['csv_configuration']['decimal'],  '.')
        self.assertEqual(result['csv_pulse']['csv_configuration']['delimiter'],  ',')


    def test_add_ulco_pulse_csv_file_to_parse_true_ulco_file(self):
        from csv_configuration import french_csv_configuration

        local_path = 'tests/cytosense/ULCO/mock'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        data = {
            'raw_folder': PurePath(local_path),
            'sample_name': sample_name,
        }
        test_filename = sample_name + "_Pulses.csv"
        test_path = local_path + "/" + test_filename

        ut = add_ulco_pulse_csv_file_to_parse(french_csv_configuration)
        result = ut._run(data)

        self.assertEqual(result['csv_pulse']['filename'],  test_filename , " -- filename different")
        self.assertEqual(result['csv_pulse']['mapping'],  pulse , " -- mapping different")
        self.assertEqual(result['csv_pulse']['path'],  PurePath(test_path) , " -- path different")
        self.assertEqual(result['csv_pulse']['csv_configuration']['decimal'],  ',')
        self.assertEqual(result['csv_pulse']['csv_configuration']['delimiter'],  ';')


    def test_add_ulco_listmode_csv_file_to_parse_true_ulco_file(self):
        from csv_configuration import french_csv_configuration

        local_path = 'tests/cytosense/ULCO/mock'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        data = {
            'raw_folder': PurePath(local_path),
            'sample_name': sample_name,
        }

        test_filename = sample_name + "_Listmode.csv"
        test_path = local_path + "/" + test_filename

        ut = add_ulco_listmode_csv_file_to_parse(french_csv_configuration)
        result = ut._run(data)

        self.assertEqual(result['csv_listmode']['filename'],  test_filename , " -- filename different")
        self.assertEqual(result['csv_listmode']['mapping'],  UlcoListmode , " -- mapping different")
        self.assertEqual(result['csv_listmode']['path'],  PurePath(test_path) , " -- path different")
        self.assertEqual(result['csv_listmode']['csv_configuration']['decimal'],  ',')
        self.assertEqual(result['csv_listmode']['csv_configuration']['delimiter'],  ';')


    def test_add_ulco_pulse_csv_file_to_parse_file_do_not_exist(self):
        data = { 
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample'
        }

        ut = add_ulco_pulse_csv_file_to_parse()
        # ut.is_file_exist = lambda : False # is_file_exist_mooc_false

        self.assertRaises(Exception, ut.run, data)

        
    # failed : need to mock is_file_exist
    def test_fail_process_pulse_generic(self):
        data = {
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample',
                'csv_pulse':  {'filename': 'mySample_Pulses.csv',
                                'mapping': pulse,
                                'path': PurePath('/_raw/mySample_Pulses.csv')
                            }
            }
        ut = summarize_csv_pulse()
        # ut = summarize_csv_pulse_test()
        # ut.save_dataframe_to_csv = lambda : 'csv saved'
        # ut.summarise_pulses_function = summarize_pulses_function
        # ut.save_dataframe_to_csv = save_csv
        result = ut._run(data)

        self.assertEqual( result['csv_pulse']['path'] , PurePath( data['raw_folder'], str(data['sample_name'] + "_Polynomial_Pulses.csv") ) )
        # self.assertEqual(summarize_called, 1)
        # self.assertEqual(save_called, 1)

    def test_process_pulse(self):
        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        filename = sample_name +  '_Pulses.csv'
        polynomial_filename = sample_name +  '_Polynomial_Pulses.csv'
        data = {
                'raw_folder': PurePath(local_path),
                'sample_name': sample_name,
                'csv_pulse':  {'filename': filename,
                                'mapping': pulse,
                                'path': PurePath(local_path , filename),
                                'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                            }
            }
        ut = summarize_csv_pulse()
        # ut = summarize_csv_pulse_test()
        # ut.save_dataframe_to_csv = lambda : 'csv saved'
        # ut.summarise_pulses_function = summarize_pulses_function
        # ut.save_dataframe_to_csv = save_csv
        result = ut._run(data)

        # self.assertEqual( result['csv_pulse']['filename'] , PurePath( data['raw_folder'], str(data['sample_name'] + "_Polynomial_Pulses.csv") ) )
        self.assertEqual( result['csv_pulse']['filename'], polynomial_filename , " -- Different filename" )
        self.assertEqual( result['csv_pulse']['path'],  PurePath( local_path , polynomial_filename ), " -- Different path" ) 
        # self.assertEqual( result['csv_pulse']['path'] , PurePath( data['raw_folder'], str(data['sample_name'] + "_Polynomial_Pulses.csv") ) )
        # self.assertEqual(summarize_called, 1)
        # self.assertEqual(save_called, 1)


    def test_process_pulse_wrong_pulse_file(self):
        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        polynomial_filename = sample_name +  '_Polynomial_Pulses.csv'
        data = {
                'raw_folder': PurePath(local_path),
                'sample_name': sample_name,
                'csv_pulse':  {'filename': polynomial_filename,
                                'mapping': pulse,
                                'path': PurePath(local_path , polynomial_filename),
                                'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                            }
            }
        
        ut = summarize_csv_pulse_test()
        utlambda = lambda : ut._run(data)

        self.assertRaises(Exception, utlambda )
 

    def test_init_dataframe(self):
        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        filename = sample_name +  '_Pulses.csv'

        model = Template()
        model._mapping = {
            'img_file_name': { 'type' : '[t]'},
            'img_rank': { 'type':'[f]'},
            "object_id": { "type": "[t]" },
            "object_fws": { "type": "[t]" },
            "object_sws": { "type": "[t]" }
        }
        polynomail_filename = sample_name +  '_Polynomial_Pulses.csv'
        data = {
                'raw_folder': PurePath(local_path),
                'sample_name': sample_name,
                'csv_pulse':  {'filename': filename,
                                'mapping': model,
                                'path': PurePath(local_path , filename),
                                'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                            }
        }
        ut = summarize_csv_pulse_test()
        result = ut._run(data)
        self.assertEqual(result['csv_pulse']['mapping'],  model)


    def test_process_pulse_analyse_empty_file(self):
        import pandas as pd 

        local_path = 'tests'
        sample_name = 'empty'
        polynomail_filename = sample_name +  '_Polynomial_Pulses.csv'
        model = Template()
        model._mapping = {
                'img_file_name': { 'type':'[t]', 'index':0},
                'img_rank': { 'type':'[f]', 'index':1},
                "object_id": { "type": "[t]", 'index':2 },
                "object_fws": { "type": "[t]", 'index':3 },
                "object_sws": { "type": "[t]", 'index':4 }
            }
        data = {
                'raw_folder': PurePath(local_path),
                'sample_name': sample_name,
                'csv_pulse':  {'filename': polynomail_filename,
                                'mapping': model,
                                'path': PurePath(local_path , polynomail_filename),
                                'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                            }
            }
        dftest = pd.DataFrame({ 'img_file_name': ['[t]'],
                                'img_rank': ['[f]'],
                                'object_id': ['[t]'],
                                'object_fws': ['[t]'],
                                'object_sws': ['[t]']             
                               })
        print ("dftest:" + dftest.values)

        ut = analyze_csv_pulse()
        result = ut._run(data)

        from pandas.testing import assert_frame_equal        
        
        df: pd.DataFrame = result['tsv_pulse']['dataframe']
        print ("df:" + str(df.values))

        assert_frame_equal( df, dftest )


    # def test_analyse_cvs_pulse_init_df(self):
    #     ut = analyze_csv_pulse()
    #     ut._init_df()



    def test_process_pulse_analyse(self):
        import pandas as pd 

        mock = mock_ulco_small_data()

        data = {
            'raw_folder': PurePath(mock.local_path),
            'sample_name': mock.sample_name,
            'csv_pulse':  {'filename': mock.polynomial_filename,
                            'mapping': mock.pulse_model,
                            'path': PurePath(mock.local_path , mock.polynomial_filename),
                            'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                        }
        }
    
        ut = analyze_csv_pulse()
        result = ut._run(data)

        from pandas.testing import assert_frame_equal        
        
        df: pd.DataFrame = result['tsv_pulse']['dataframe']
        print ("df:" + str(df.values))
        # to have a human view
        df.to_csv("tests/cytosense/result/" + mock.sample_name + "__pulses__" + ".csv", index=False)

        assert_frame_equal( df, mock.df )



    def test_process_listmode_analyse(self):
        import pandas as pd 

        mock = mock_ulco_small_data()
 
        data = {
            'raw_folder': PurePath(mock.local_path),
            'sample_name': mock.sample_name,
            'csv_listmode': {
                            'filename': mock.listmode_filename,
                            'mapping': mock.ulco_listmode_model,
                            'path': PurePath(mock.local_path , mock.listmode_filename),
                            'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                        }
        }
    
        ut = analyse_cvs_listmode()
        result = ut._run(data)

        from pandas.testing import assert_frame_equal        
        
        df: pd.DataFrame = result['tsv_listmode']['dataframe']
        print ("df:" + str(df.values))
        # to have a human view

        result_filename = mock.sample_name + "__listmode__" + ".csv"
        result_path = "tests/cytosense/result/"
        csv_path = PurePath(result_path, result_filename)
        df.to_csv(csv_path, index=False)

        assert_frame_equal( df, mock.df_listmode )




    def test_merge_csv_pulse_and_listmode(self):
        from  mock_polynomial_pulses_ulco_small_data import mock_ulco_dataframe
        import pandas as pd 

        mock = mock_ulco_dataframe()

        data = mock.data

        ut = merge_files()
        result = ut._run(mock.data)

        df_result = result['tsv_list']['df_result']['dataframe']

        result_filename = mock.sample_name + "__result_merge__" + ".csv"
        result_path = "tests/cytosense/result/"
        csv_path = PurePath(result_path, result_filename)

        df_result.to_csv(csv_path, index=False )

        from pandas.testing import assert_frame_equal        
        assert_frame_equal( df_result, mock.df )


    def test_image_list(self):

        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'

        image_folder = sample_name + "_Images"
        image_path = PurePath(local_path , image_folder)
        data = {
            'raw_folder': PurePath(local_path),
            'sample_name': sample_name,
            'images_folder':image_path,
        }
        image_name_pattern = [NamePatternComponent.eSampleName,"_Cropped_",NamePatternComponent.eIndex,".jpg"]

        mock = mock_ulco_small_data_images()

        ut = list_images(pattern_name=image_name_pattern)
        result = ut._run(data)

        dump(result['image_list'])
        dump(mock.image_list)

        image_result_filename = image_folder + ".csv"
        result_path = "tests/cytosense/result/"
        result_image_path = PurePath(result_path,image_result_filename)
        dfresult : pd.DataFrame = result['dataframe']['images']
        # dfresult.sort_values(by = 'object_id' , axis="columns", inplace=True )
        # dfresult.sort_values(by = 'key' , inplace=True )

        from natsort import index_natsorted
        import numpy as np
        # dfresult.sort_values(by = 'key' , inplace=True, key=lambda x: np.argsort(index_natsorted(dfresult["key"])))
        dfresult.sort_values(by = 'object_id' , inplace=True, key=lambda x: np.argsort(index_natsorted(dfresult["object_id"])))
        dfresult.to_csv(PurePath(result_image_path), index=False)

        # from pandas.testing import assert_frame_equal        

        self.assertEqual(ut.image_name_pattern, image_name_pattern, " -- pattern are different")
        # myDictAssert(result['image_list'], mock.image_list) # DON'T REMOVE : easiest to find issue in the dict with this assert than assertDictEqual
        self.assertDictEqual(result['image_list'], mock.image_list, " -- image_list dict are different")



    def test_image_list_fn_not_filtered(self):
        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'

        image_folder = sample_name + "_Images"
        image_path = PurePath(local_path , image_folder)
        self.assertEqual(str(image_path),"tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images")

        image_name_pattern = [NamePatternComponent.eSampleName,"_Cropped_",NamePatternComponent.eIndex,".jpg"]
        mock = mock_ulco_small_data_images()

        m = ['tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_10104.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_29.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_3543.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_4206.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_3269.jpg']

        ut = list_images(pattern_name=image_name_pattern)
        ut._data['sample_name']=sample_name

        utlambda = lambda _ : ut.list_files(image_path)
        # result = ut.list_files(image_path)

        # dump(result)
        self.assertRaises(Exception, utlambda )


    def test_image_list_fn(self):
        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'

        image_folder = sample_name + "_Images"
        image_path = PurePath(local_path , image_folder)
        self.assertEqual(str(image_path),"tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images")

        image_name_pattern = [NamePatternComponent.eSampleName,"_Cropped_",NamePatternComponent.eIndex,".jpg"]
        mock = mock_ulco_small_data_images()

        m = ['tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_10104.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_29.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_3543.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_4206.jpg', 'tests/cytosense/ULCO/mock_small_data/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Images/R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_3269.jpg']

        ut = list_images(pattern_name=image_name_pattern)
        ut._data['sample_name']=sample_name
        result = ut.list_files(image_path, image_name_pattern)

        # dump(result,image_name_pattern)

        self.assertListEqual(result,m)


    def test_trunc(self):
        import pandas as pd

        # mock_merge = mock_ulco_dataframe()
        # mock_images = mock_ulco_small_data_images()

        # df_merge = pd.read_csv(mock_merge.result_path)
        # df_images = pd.read_csv(mock_images.result_image_path)

        # # dfmock = pd.merge(df_merge, df_images, how="inner", on=['object_id'])
        # dfmock = pd.merge(df_merge, df_images, how="inner", left_on=['object_id'], right_on=['key'])
        # del dfmock["key"]
        # del dfmock["path"]

        # mock_merge_trunc = "mock_merge_trunc.csv"
        # result_path = "tests/cytosense/result/"
        # result_mock_merge_trunc_path = PurePath(result_path, mock_merge_trunc)
        # dfmock.to_csv(PurePath(result_mock_merge_trunc_path), index=False)

        mock = mock_trunc()
        data = mock.data

        ut = trunc_data()
        result = ut._run(data)

        self.assertIn('tsv_list',result, " -- 'tsv_list' don't exist")
        self.assertIn('df_result',result['tsv_list'], " -- 'df_result' don't exist")
        self.assertIn('dataframe',result['tsv_list']['df_result'], " -- 'dataframe' don't exist")
        df_result = result['tsv_list']['df_result']['dataframe']

        result_filename = "__purged__.csv"
        trunc_result_path = PurePath(self.result_path,result_filename)
        df_result.to_csv(trunc_result_path)

        from pandas.testing import assert_frame_equal        
        assert_frame_equal( df_result, mock.df )




        # assert "Need to" == "finish this test"

    def test_copy_images(self):

        m = mock_ulco_small_data_images()
        work_folder = PurePath(m.mock_path, "_work" ,m.sample_name)
        images_folder = PurePath(m.mock_path, str(m.sample_name + "_Images"))

        data = {
            'raw_folder': m.mock_path,
            'sample_name': m.sample_name,
            'work_folder': work_folder,
            'images_folder': images_folder,
            'image_list': m.df,
        }

        ut = copy_images_task()
        ut._run(data)

        assert "need to " "finish"
        # how to extract column from dataframe ? 


if __name__ == '__main__':
    unittest.main()

