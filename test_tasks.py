

from pathlib import PurePath
import unittest
from cytosense import NamePatternComponent
from cytosenseModel import pulse
from tasks import add_ulco_pulse_csv_file_to_parse, define_sample_pipeline_folder, summarize_csv_pulse

# from tasks import add_ulco_pulse_csv_file_to_parse, define_sample_pipeline_folder, summarize_csv_pulse





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
        raise "NamePatternComponent.eSampleName not found" 
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
        raise "NamePatternComponent.eSampleName not found" 
    name = "".join(pattern)
    return name


def build_name_ulco_pulse_filename(data):
    # pattern = [ NamePatternComponent.eSampleName , "_Pulse" , ".cvs" ]
    # try:
    #     # name_index = file_pattern.index(NamePatternComponent.eSampleName)
    #     name_index = pattern.index(NamePatternComponent.eSampleName)
    #     pattern[name_index] = str(data['sample_name'])
    # except:
    #     raise "NamePatternComponent.eSampleName not found" 
    # path = "".join(pattern)
    # return path
    return data['sample_name'] + "_Pulse.csv"




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

    def test_build_name_kw(self):
        file_pattern = [ NamePatternComponent.eSampleName , "_Pulse" , ".csv" ]
        sample_name= 'mySample'
        ut = build_name_kw( sample_name = sample_name, file_pattern = file_pattern)

        self.assertEqual(ut , sample_name + "_Pulse" + ".csv" )

    def test_build_name_ulco_pulse_filename(self):
        data = {'sample_name': 'mySample' }
        ut = build_name_ulco_pulse_filename(data)
        self.assertEqual(ut,"mySample_Pulse.csv")




    # def test_cvs_file_to_parse_missing_argument(self):
    #     # ut = cvs_file_to_parse(filetype="filetype", mapping={}, filename_pattern="filename_pattern")
    #     self.assertRaises(Exception, cvs_file_to_parse, mapping={}, filename_pattern="filename_pattern")

    # def test_cvs_file_to_parse_bad_name__argument(self):
    #     # ut = cvs_file_to_parse(filetype="filetype", mapping={}, filename_pattern="filename_pattern")
    #     self.assertRaises(Exception, cvs_file_to_parse, filetype="filetype", mapping={}, filename_pattern="filename_pattern")


    # def test_cvs_file_to_parse(self):

    #     mapping={}
    #     filename_pattern = [ NamePatternComponent.eSampleName , "_Pulse" , ".csv" ]
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


    def test_change_function(self):

        myLambda = lambda : True # is_file_exist_mooc_true

        ut = add_ulco_pulse_csv_file_to_parse()
        ut.is_file_exist = myLambda
        self.assertEqual(myLambda , ut.is_file_exist)

    def test_add_ulco_pulse_csv_file_to_parse(self):
        data = { 
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample'
        }

        ut = add_ulco_pulse_csv_file_to_parse()
        ut.is_file_exist = lambda _ : True
        result = ut.run(data)

        self.assertEqual(result['csv_pulse'],  {'filename': 'mySample_Pulse.csv',
                                                'mapping': pulse,
                                                'path': PurePath('/_raw/mySample_Pulse.csv')})



    def test_add_ulco_pulse_csv_file_to_parse_file_do_not_exist(self):
        data = { 
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample'
        }

        ut = add_ulco_pulse_csv_file_to_parse()
        # ut.is_file_exist = lambda : False # is_file_exist_mooc_false

        self.assertRaises(Exception, ut.run, data)

        

    def test_process_pulse(self):
        data = {
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample',
                'csv_pulse':  {'filename': 'mySample_Pulse.csv',
                                'mapping': pulse,
                                'path': PurePath('/_raw/mySample_Pulse.csv')}
            }
        # ut = summarize_csv_pulse()
        ut = summarize_csv_pulse_test()
        # ut.save_dataframe_to_csv = lambda : 'csv saved'
        # ut.summarise_pulses_function = summarize_pulses_function
        # ut.save_dataframe_to_csv = save_csv
        result = ut.run(data)

        self.assertEqual( result['csv_pulse']['path'] , PurePath( data['raw_folder'], str(data['sample_name'] + "_PolynomialPulse.csv") ) )
        self.assertEqual(summarize_called, 1)
        self.assertEqual(save_called, 1)


if __name__ == '__main__':
    unittest.main()

