

from pathlib import PurePath
import unittest
from Template import Template
from cytosense import NamePatternComponent
from cytosenseModel import UlcoListmode, pulse
from tasks import add_ulco_listmode_csv_file_to_parse, add_ulco_pulse_csv_file_to_parse, analyze_csv_pulse, define_sample_pipeline_folder, summarize_csv_pulse

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


    def test_change_function(self):

        myLambda = lambda : True # is_file_exist_mooc_true

        ut = add_ulco_pulse_csv_file_to_parse()
        ut.is_file_exist = myLambda
        self.assertEqual(myLambda , ut.is_file_exist)

    # test have an issue, cannot mock is_file_exist()
    def test_add_ulco_pulse_csv_file_to_parse(self):
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
    def test_process_pulse_generic(self):
        data = {
                'raw_folder': PurePath('/_raw'),
                'sample_name': 'mySample',
                'csv_pulse':  {'filename': 'mySample_Pulses.csv',
                                'mapping': pulse,
                                'path': PurePath('/_raw/mySample_Pulses.csv')
                            }
            }
        # ut = summarize_csv_pulse()
        ut = summarize_csv_pulse_test()
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
        polynomail_filename = sample_name +  '_Polynomial_Pulses.csv'
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
        self.assertEqual( result['csv_pulse']['filename'], polynomail_filename , "Different filename" )
        self.assertEqual( result['csv_pulse']['path'],  PurePath( local_path , polynomail_filename ), "Different path" ) 
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
        utlabmda = lambda : ut._run(data)

        self.assertRaises(Exception, utlabmda )
 

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

        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        polynomial_filename = sample_name +  '_Polynomial_Pulses.csv'
        
        corrupted_model = pulse 
        # cannot test, because model is not force to take all columns
        # del corrupted_model._mapping['object_id']

        data = {
                'raw_folder': PurePath(local_path),
                'sample_name': sample_name,
                'csv_pulse':  {'filename': polynomial_filename,
                                'mapping': corrupted_model,
                                'path': PurePath(local_path , polynomial_filename),
                                'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                            }
            }
        
        headerCSV = ["Particle ID","FWS_coef_0","FWS_coef_1","FWS_coef_2","FWS_coef_3","FWS_coef_4","FWS_coef_5","FWS_coef_6","FWS_coef_7","FWS_coef_8","FWS_coef_9","SWS_coef_0","SWS_coef_1","SWS_coef_2","SWS_coef_3","SWS_coef_4","SWS_coef_5","SWS_coef_6","SWS_coef_7","SWS_coef_8","SWS_coef_9","FL Yellow_coef_0","FL Yellow_coef_1","FL Yellow_coef_2","FL Yellow_coef_3","FL Yellow_coef_4","FL Yellow_coef_5","FL Yellow_coef_6","FL Yellow_coef_7","FL Yellow_coef_8","FL Yellow_coef_9","FL Orange_coef_0","FL Orange_coef_1","FL Orange_coef_2","FL Orange_coef_3","FL Orange_coef_4","FL Orange_coef_5","FL Orange_coef_6","FL Orange_coef_7","FL Orange_coef_8","FL Orange_coef_9","FL Red_coef_0","FL Red_coef_1","FL Red_coef_2","FL Red_coef_3","FL Red_coef_4","FL Red_coef_5","FL Red_coef_6","FL Red_coef_7","FL Red_coef_8","FL Red_coef_9","Curvature_coef_0","Curvature_coef_1","Curvature_coef_2","Curvature_coef_3","Curvature_coef_4","Curvature_coef_5","Curvature_coef_6","Curvature_coef_7","Curvature_coef_8","Curvature_coef_9"]

        header = [
            'object_id',  
            'object_coef_0_FWS', 'object_coef_1_FWS', 'object_coef_2_FWS', 'object_coef_3_FWS', 'object_coef_4_FWS', 'object_coef_5_FWS', 'object_coef_6_FWS', 'object_coef_7_FWS',  'object_coef_8_FWS', 'object_coef_9_FWS', 
            'object_coef_0_SWS', 'object_coef_1_SWS', 'object_coef_2_SWS', 'object_coef_3_SWS','object_coef_4_SWS', 'object_coef_5_SWS','object_coef_6_SWS', 'object_coef_7_SWS','object_coef_8_SWS', 'object_coef_9_SWS',
            'object_coef_0_FL_Yellow', 'object_coef_1_FL_Yellow', 'object_coef_2_FL_Yellow', 'object_coef_3_FL_Yellow','object_coef_4_FL_Yellow','object_coef_5_FL_Yellow',  'object_coef_6_FL_Yellow', 'object_coef_7_FL_Yellow', 'object_coef_8_FL_Yellow', 'object_coef_9_FL_Yellow',
            'object_coef_0_FL_Orange', 'object_coef_1_FL_Orange', 'object_coef_2_FL_Orange', 'object_coef_3_FL_Orange', 'object_coef_4_FL_Orange', 'object_coef_5_FL_Orange',  'object_coef_6_FL_Orange', 'object_coef_7_FL_Orange', 'object_coef_8_FL_Orange', 'object_coef_9_FL_Orange', 
            'object_coef_0_FL_Red', 'object_coef_1_FL_Red', 'object_coef_2_FL_Red', 'object_coef_3_FL_Red', 'object_coef_4_FL_Red', 'object_coef_5_FL_Red', 'object_coef_6_FL_Red',  'object_coef_7_FL_Red', 'object_coef_8_FL_Red', 'object_coef_9_FL_Red',
            'object_coef_0_curvature', 'object_coef_1_Curvature', 'object_coef_2_Curvature', 'object_coef_3_Curvature', 'object_coef_4_Curvature', 'object_coef_5_Curvature','object_coef_6_Curvature', 'object_coef_7_Curvature', 'object_coef_8_Curvature', 'object_coef_9_Curvature',
        ]    

        type_header=["[f]" for _ in range(len(header))]

        dest = [
            [0,-68.04754805517467,170.0141493931962,-103.1316447602405,29.596328167863966,-4.03996672486493,0.298463038013299,-0.012738856779690094,0.00031511120820561066,-4.202159571690249e-06,2.339972032248827e-08,-12.268580334705911,21.251139563742033,-11.216311216723625,2.6785118950851046,-0.31771238058569834,0.020995654211594085,-0.0008162421317762789,1.8621908198765924e-05,-2.311953790125044e-07,1.2075778859829984e-09,1.8811309009657804,-1.2156615289293073,0.6377312527859975,-0.14230439166742187,0.01690194501963563,-0.0011700045284822234,4.855372686315206e-05,-1.1880964728526058e-06,1.5794023326397032e-08,-8.794527414015224e-11,0.4787292001760408,0.41191530664708703,-0.39032631189160605,0.15185519167238415,-0.02258010551023266,0.001696587617100022,-7.189117237027885e-05,1.7502358824879186e-06,-2.2913650467506653e-08,1.2527475792832748e-10,-0.9894049579900819,3.506640470330078,-1.8784838030464424,0.5521080044545936,-0.07338391569421437,0.005145379667917397,-0.00020649175625426895,4.7922951465235416e-06,-6.002581061950583e-08,3.1477256589659894e-10,-0.04681117509893093,-0.14694233887777908,0.07206825782553343,-0.012868837037907121,0.001192081174480416,-6.41546738733492e-05,2.0753671106896203e-06,-3.961062419913173e-08,4.0843949179365186e-10,-1.7381832174903998e-12],
            [1,160.19119195047253,-286.09868022470226,228.07354447238112,-86.03596463339086,18.455134518894557,-2.3036212782897127,0.16978010663557128,-0.007290442639826719,0.00016889041922082815,-1.6335019533570842e-06,6.626103715168874,-9.44110577054712,6.538832979567237,-1.9856579821497977,0.3223137936483027,-0.022238348036304638,-1.8894179822981794e-05,8.217072628400408e-05,-3.963450214115317e-06,5.965759246856086e-08,0.16956749225997858,1.1925702712165134,-0.9237935877185861,0.3618918438082599,-0.07652162162106012,0.009534501581088737,-0.0007215413579637583,3.2519417365950426e-05,-8.011369360075277e-07,8.29468422755171e-09,2.0399009287926013,-1.9785053921333366,1.6715046908722941,-0.6692789384943116,0.14595319141663113,-0.018040579583949407,0.0012996668295356235,-5.409511183562201e-05,1.2053390821597312e-06,-1.1117284013575295e-08,0.7735580495353407,2.1835146702123023,-1.597605147694461,0.6868033062165819,-0.14206108473251483,0.017674480352976668,-0.0014054329107636996,6.868073255908877e-05,-1.8511715003430167e-06,2.089945358638368e-08,0.01754952399380441,-0.12523873363563956,0.0533746850295197,-0.010144465106239266,0.0012436765698012847,-0.00012116008433596569,9.519033019646833e-06,-5.193997316121304e-07,1.624904230774717e-08,-2.1331706280896722e-10],
            [2,96.81589626241993,-169.27122551281087,114.25624901934184,-35.34135583950736,5.997896015363872,-0.564085617503418,0.0297274224133677,-0.0008547403579370158,1.1955083552100815e-05,-5.615256002146967e-08,3.2277515255547016,-4.021300770204839,2.2953581741097624,-0.4850386326347379,0.021759456220065483,0.007859107889356575,-0.0012486843174860625,7.533431478517207e-05,-2.088108511332875e-06,2.219683936981322e-08,0.6927224256293694,-0.12959628233737353,-0.03917707288512781,0.07653999462176653,-0.026021223564060746,0.004073670293733698,-0.0003410911202399483,1.5742844476525992e-05,-3.7805124575447775e-07,3.6933881342950844e-09,2.4157010869567985,-3.9253995404023434,2.8656958350431934,-0.9937021433235225,0.18835546875779802,-0.0203882553012097,0.0012978091640555472,-4.817689383465123e-05,9.666647179057516e-07,-8.111194334384088e-09,2.1254757818464682,-2.1875842946068262,1.4000299788403117,-0.35583447313132,0.06125278986919644,-0.006037758094735724,0.0003223053143248557,-8.888260271603064e-06,1.0660629482128864e-07,-2.4338463282950166e-10,0.16844666990846663,-0.16111268233201206,0.03629640611142444,-0.003762431821941539,0.0003356107589018647,-3.839439476747628e-05,3.3878169981765115e-06,-1.7221985513032618e-07,4.541360061283899e-09,-4.850420149805663e-11],
            [3,87.25124613003015,-165.5859542186256,127.68193388761091,-46.102817041994484,9.357272260376913,-1.0761961934763686,0.07106343218363267,-0.0026523274938349338,5.142060591542531e-05,-3.9412455525837384e-07,-0.098479876163033,2.2469525881586074,-2.3215307272601846,1.229352264621881,-0.35356840009827784,0.060950902819874433,-0.006046194677343353,0.0003348673127234852,-9.63059291156446e-06,1.1221068100366737e-07,0.1891498452011504,0.8984546624861437,-0.7634007953689952,0.30625912749063927,-0.06782961038208167,0.008833847255355513,-0.0006883333149939859,3.1467115352796395e-05,-7.77500384847609e-07,8.011591646857876e-09,1.792964396284817,-2.3523444874640718,1.788334626367846,-0.6332436389193469,0.12347123562286666,-0.013843800183896707,0.0009139074052585819,-3.510005888868798e-05,7.253899157356212e-07,-6.230775390839122e-09,1.0672577399377818,-0.30662018316772044,0.2768571354020154,-0.07737514724622882,0.018377412825638744,-0.0013063324021242101,-6.999075999945464e-05,1.2961020916715635e-05,-5.749332358076772e-07,8.522532321643362e-09,0.39808215170278327,-0.45393536457761074,0.18098914395310775,-0.040748727996311074,0.0060227021435502615,-0.0006084078188255376,4.145115661209652e-05,-1.8106920296291622e-06,4.5520709778778296e-08,-4.977209131010229e-10],
            [29,167.63803182075088,-285.13913950946034,163.48557806082334,-43.58269059022846,6.247198208117836,-0.5020004412717721,0.023362250972442856,-0.0006266543702649454,9.004175321666755e-06,-5.3722448873497215e-08,8.758454457447314,-13.741044694641564,7.780776420645863,-2.0258206233890106,0.27399573541710764,-0.020139877517058785,0.0008340084952403479,-1.9289952875520287e-05,2.2881045300599347e-07,-1.0506892055226045e-09,0.7630973926342697,-0.42964110885791196,0.22186511944778337,-0.048121940127435425,0.004367494987886956,-7.239367141692905e-05,-1.2511317992711592e-05,8.335643990503596e-07,-2.0186244507019104e-08,1.7623059340300567e-10,2.29384374415565,-2.8366046197368577,1.7851808898119526,-0.5351601567868325,0.08473186467723226,-0.007250366222782847,0.0003513200411885568,-9.697294626894115e-06,1.425506417034541e-07,-8.678552453892432e-10,1.4044218923793963,-1.5206088864767824,1.023030774761746,-0.39930990694197366,0.08480800398566561,-0.00817793499044534,0.00040425669716958516,-1.0721023307439035e-05,1.4467732061901095e-07,-7.732094578250166e-10,0.7090471197445706,-0.04734871821790856,-0.1258835308401218,0.039303908689241634,-0.005397323566360818,0.0004162341129207915,-1.9243945756555243e-05,5.300061547395002e-07,-8.02378630175771e-09,5.142858169920372e-11],
            [3269,199.379570374963,-295.842360665635,140.19659307842613,-30.0190594174841,3.353557848906983,-0.2079933736315469,0.007428290199580921,-0.0001517932218032946,1.6444753076721615e-06,-7.292717948317964e-09,47.06234259392744,-67.63908118822174,31.82129602740207,-6.678634255263537,0.7076082326480992,-0.03862374223088996,0.0010909314067093319,-1.4327688405124872e-05,4.2836112147451035e-08,4.6173346173509475e-10,3.5018717351283275,-4.246933446075114,2.0079303687443386,-0.43235189190472423,0.0486610871194474,-0.0030113418338406153,0.00010630987117339006,-2.1305043424318793e-06,2.2461768685413656e-08,-9.603481619900653e-11,12.513117269853055,-18.998455611388966,9.797203954313552,-2.3129030284254313,0.28527781738059,-0.019422084876482892,0.000761345431277292,-1.7177798571858748e-05,2.077568228439444e-07,-1.0452522156669114e-09,43.72201104412085,-64.27137551597012,31.497753171893617,-7.086720593219816,0.8396640441710989,-0.05481033199464663,0.002049132142050755,-4.381371566452414e-05,4.986776925578978e-07,-2.3430520469086337e-09,0.1376695640924506,0.5209526461397347,-0.2385296630717405,0.04209032835952636,-0.003885611355464286,0.00020822133637437917,-6.710668386967188e-06,1.2810666534947057e-07,-1.3315443038903759e-09,5.786060647658829e-12],
            [3543,37.847569090516345,-29.340105497158753,10.712732563350352,-1.9102841421941048,0.18748999275343342,-0.008999542077002121,0.00022862098960593617,-3.173048105037512e-06,2.2790784858371306e-08,-6.628971577584796e-11,-74.6667578620079,234.57362076284835,-71.71795706971744,9.390308562417065,-0.6245154365728449,0.023932231683686668,-0.0005508270382330387,7.494325720626853e-06,-5.5394856898160856e-08,1.7110262962592224e-10,-1.4824618790619795,1.9332217787637243,-0.3911956108841608,0.017468048033809917,0.001815983321124831,-0.000167930706912399,5.500898648033854e-06,-9.00542191229958e-08,7.454073745464397e-10,-2.4991900109418458e-12,-5.108823769568062,6.855689305486504,-2.0011201039875655,0.2037672913210812,-0.006288019171394909,4.8252682086761257e-05,1.2187490871461698e-07,1.8761745831639127e-08,-4.855625537927231e-10,2.987419856848487e-12,-27.3941805818514,32.56027571666022,-8.259119555103268,0.6861242720382932,-0.005800911657911928,-0.000906628525481631,3.265889362698931e-05,-4.4361914814518423e-07,2.453579088906172e-09,-3.3941069739216956e-12,-0.2737353841507535,0.11273130563935911,-0.03951827527260601,0.005640423745298455,-0.00040780572099579,1.6723897122812394e-05,-4.0586335864432183e-07,5.777638180609396e-09,-4.463052729154384e-11,1.4454904070134359e-13],
            [4206,4.184095020222003,66.70123869227936,-23.722892814372173,3.4511100848986187,-0.1958399765478837,0.005537462968436103,-8.45999530273397e-05,6.896251590765643e-07,-2.649882443132145e-09,3.104573646300617e-12,80.08383883531188,-2.6994869368735954,1.7066064194498296,-0.29541996621926825,0.021494348461736736,-0.0008118053772317628,1.7324320763379463e-05,-2.110318971996032e-07,1.3697500646352577e-09,-3.67758677817544e-12,-0.5599543878771875,1.09174193886297,-0.3082130952388093,0.03542674363534289,-0.0019479298864734614,5.884427484164022e-05,-1.0355944163996354e-06,1.0606677969301862e-08,-5.871199395539507e-11,1.359987304123782e-13,1.504850036938418,-0.6290732560791779,0.06790282218864835,0.003981389907039526,-0.00024586602936311585,-2.416979879366261e-06,3.3485640983649725e-07,-7.2991358416571606e-09,6.555357671234982e-11,-2.1695209078049766e-13,-1.5943385030893467,4.630464630473345,-1.4708602797207706,0.20108220997980544,-0.010993551015975465,0.00029743602640290784,-4.2507755397668896e-06,3.068626580992862e-08,-8.690510837397552e-11,-1.2390670300540023e-14,0.10093478980377572,-0.073945481497039,0.01615877106066168,-0.001582094811447267,8.303946936429822e-05,-2.544861024953992e-06,4.699545988863857e-08,-5.151274771779635e-10,3.0870263524935436e-12,-7.79033542864106e-15],
            [10104,353.4019785902075,-300.50931124670495,67.71309692164564,-6.3758394578206135,0.33132366891136916,-0.01046566725372772,0.00020679093809992325,-2.5013152435630283e-06,1.6928594519914215e-08,-4.901584089912509e-11,26.090913261916,-22.07568855758994,5.154580293526573,-0.4626215646533751,0.023941796919992604,-0.0008065653015955101,1.8016289634409706e-05,-2.5334784780286304e-07,1.9942623796099706e-09,-6.619596882806372e-12,4.951394564185177,-3.520267574814959,0.6675485216852344,-0.042865630759796644,0.0010165325415657477,5.203658381861246e-06,-7.275603612060069e-07,1.445114574440913e-08,-1.2318028457964825e-10,3.994020874205287e-13,21.30064543375171,-17.16480767701125,3.628977777248023,-0.28484484820816686,0.01088688348075027,-0.0002142850303209622,1.953507906776608e-06,-2.134279408179647e-09,-8.599981475889998e-11,4.2576628167386866e-13,81.64559528643373,-65.47911883286196,13.578212339050005,-1.0233017256433508,0.03610004176099255,-0.0005826251731129589,1.8055342389544937e-06,6.846950231792823e-08,-8.776414566590535e-10,3.247947434329225e-12,0.6664085145046472,0.14553228475715788,-0.08238443314215625,0.010964723844340715,-0.0007066894848787671,2.5727686836543392e-05,-5.556492080593385e-07,7.0567090820806274e-09,-4.868450681666122e-11,1.4079473222906686e-13]
        ]

        print("header len:" + str(len(header)))
        dftest = pd.DataFrame(columns=[key for key in header])
        dftest.to_csv("tests/cytosense/result/" + sample_name + "__test_1__" + ".csv", index=False)

        # df = df.reindex(sorted(df.columns), axis=1)

        dftest.loc[len(dftest)]=type_header
        for values in dest:
            d = {}
            for index,key in enumerate(header):
                d[key]= values[index]
            print("append row")
            dftest.loc[len(dftest)]=d

        dftest.to_csv("tests/cytosense/result/" + sample_name + "__test_2__" + ".csv", index=False)

        ut = analyze_csv_pulse()
        result = ut._run(data)

        from pandas.testing import assert_frame_equal        
        
        df: pd.DataFrame = result['tsv_pulse']['dataframe']
        print ("df:" + str(df.values))
        # to have a human view
        df.to_csv("tests/cytosense/result/" + sample_name + ".csv", index=False)

        assert_frame_equal( df, dftest )

if __name__ == '__main__':
    unittest.main()

