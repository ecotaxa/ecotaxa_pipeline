
from enum import Enum
from pathlib import Path, PurePath
from cytosenseModel import pulse

#from pipeline import Pipeline__
# from pipeline import define_sample_pipeline_folder

from task import Task

import tools




from pathlib import PurePath
from task import Task




class define_sample_pipeline_folder(Task):

    _need_keys = ['pipeline_folder', 'sample_name']
    # _update_keys = []
    _create_keys = ['raw_folder', 'work_folder', 'images_folder']

    def run(self, data):
        if  type(data['pipeline_folder']) == str:
            data['pipeline_folder'] = PurePath(data['pipeline_folder'])


        self.test_need_keys(data)
        # try:
        #     self._data['pipeline_folder'] = data['pipeline_folder']
        #     self._data['sample_name'] = data['sample_name']
        # except:
        #     raise "Missing key"
        

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

# def is_file_exist_mooc_true(path): return True
# def is_file_exist_mooc_false(path): return False

class add_ulco_pulse_csv_file_to_parse(Task):
    _need_keys = [ 'raw_folder', 'sample_name']
    _update_keys = [ 'csv_pulse']

    is_file_exist = tools.is_file_exist


    def run(self, data):
        self.test_need_keys(data)
        self.addcsv()
        self.remove_keys()
        return self._data

    def addcsv(self):
        filename = self.build_name()
        path = PurePath( self._data['raw_folder'], filename )
        if not self.is_file_exist(path): 
            raise "File " + str(path) + "do not exist"
        csv_item = { 'path': path, 'filename':  filename, 'mapping': pulse }
        self._data['csv_pulse']= csv_item 

    def build_name(self):
        return self._data['sample_name'] + "_Pulse.csv"





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
#         if not self.is_file_exist(path): raise "File " + str(path) + "do not exist"
#         csv_item = { 'path': path, 'filename':  filename, 'mapping': self._data['mapping'] }
#         csv_list = { self._data['file_type'] : csv_item }

#     def build_name(self):
#         # [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulse" , ".cvs" ]
#         pattern = self.filename_pattern.copy()
#         try:
#             name_index = pattern.index(NamePatternComponent.eSampleName)
#             pattern[name_index] = self._data['sample_name']
#         except:
#           raise "NamePatternComponent.eSampleName not found" 

#         path = "".join(pattern)
#         return path

#     # def build_name(self):
#     #     # [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulse" , ".cvs" ]
#     #     pattern = self.filename_pattern.copy()
#     #     try:
#     #         name_index = pattern.index(NamePatternComponent.eSampleName)
#     #         pattern[name_index] = self._data['sample_name']
#     #     except:
#     #         pass
#     #         #raise Exception("pattern " + )
#     #     path = "".join(pattern)
#     #     return path




NamePatternComponent = Enum('NamePatternComponent', ['eSampleName', 'eIndex', 'eImageType'])



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

# mapping = {}
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



class summarize_csv_pulse(Task):

    _need_keys = ['raw_folder', 'csv_pulse', 'sample_name']
    _update_keys = ['csv_pulse']


    import summarise_pulses
    save_dataframe_to_csv = summarise_pulses.save_dataframe_to_csv
    summarise_pulses_function = summarise_pulses.summarise_pulses

    # def __init__(self, summarise_pulses_function = summarise_pulses.summarise_pulses):
    #     # import summarise_pulses
    #     # self.summarise_pulses_function = summarise_pulses_function if summarise_pulses_function else summarise_pulses.summarise_pulses
    #     self.summarise_pulses_function = summarise_pulses_function

    def run(self, data):
        self.test_need_keys(data)
        self.process()
        self.remove_keys()
        return self._data

    def build_name(self):
        return PurePath( self._data['raw_folder'], str(self._data['sample_name'] + "_PolynomialPulse" + ".csv"))

    def process(self):

        pulses_filename = self._data['csv_pulse']['path']
        poly_dataframe = self.summarise_pulses_function(pulses_filename)
        poly_filename = self.build_name()
        self.save_dataframe_to_csv(poly_dataframe, poly_filename)
        self._data['csv_pulse']['path'] = poly_filename



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


 
class analyse_cvs(Task):
    pass


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
        ut.is_file_exist = lambda : False # is_file_exist_mooc_false

        self.assertRaises(Exception, ut.run,data)

        

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





class Pipeline():

    _tasks = [] 
    _data = {}

    def __init__(self, tasks):
        self._tasks = tasks
    

    def run(self):
        for task in self._tasks:
            self._data = task().run(self._data)



class Test_Pipeline(unittest.TestCase):

    def test_ulco_pipeline(self):

        ulco_cytosense_pipeline = [
            add_ulco_pulse_csv_file_to_parse(),
            #analyse_cvs(ulco_pulse_file_pattern, french_csv_configuration),
            #analyse_cvs(ulco_listmode_file_pattern, french_csv_configuration),
        ]
        ulco_sample_pipeline_tasks = [
            define_sample_pipeline_folder()] \
                .append(ulco_cytosense_pipeline)

        # tasks = ulco_sample_pipeline

        ut = Pipeline(ulco_sample_pipeline_tasks)
        ut.run()



if __name__ == '__main__':
    unittest.main()

