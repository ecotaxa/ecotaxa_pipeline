# test_read_infos_file_task

from pathlib import PurePath
from unittest import TestCase

import Cytosense.cytosenseModel as cytosenseModel
from DebugTools.debug_tools import dump
from Test.Mock.mock_ulco_small_data_images import mock_trunc
from Tasks.read_Infos_file_Task import add_info_file_task, cross_merge_task, parse_Infos

import pandas

class mock_ulco_infos_file():


    local_path = 'tests/cytosense/ULCO/mock_small_data'
    result_folder = "tests/cytosense/result/"

    sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'

    filename = sample_name +  "_Info" + ".txt"
    csv_filename = sample_name +  "_Info" + ".csv"
    mock_filename = "mock_" + sample_name +  "_Info" + ".csv"

    path = PurePath(result_folder, mock_filename)
    model = cytosenseModel.Info()


    # info_mock2 = {
    #      "acq_trigger_level": 15.94 ,
    #      "acq_cytousb_block_size": "Auto (maxTimeOut: 45s )" ,
    #      "acq_instrument": "ULCO" ,
    #      "acq_beam_width": 5 ,
    #      "acq_core_speed": 2 ,
    #      "sample_measurement_date": "2022-09-14 12:28:42" ,
    #      "acq_user_comments": None,
    #      "sample_measurement_duration": 602 ,
    #      "sample_flow_rate": 2.1 ,
    #      "sample_channel_1": "Trigger1",
    #      "sample_channel_2": "FWS L",
    #      "sample_channel_3": "FWS R" ,
    #      "sample_channel_4": "SWS" ,
    #      "sample_channel_4_pmt_level": 80 ,
    #      "sample_channel_5": "FL Yellow" ,
    #      "sample_channel_5_pmt_level": 80,
    #      "sample_channel_6": "FL Orange",
    #      "sample_channel_6_pmt_level": 80,
    #      "sample_channel_7": "FL Red  - TRIGGER",
    #      "sample_channel_7_pmt_level": 80,
    #      "sample_total_number_of_particles": 11003,
    #      "sample_smart_triggered_number_of_particles": 11003,
    #      "sample_concentration": 9.4915805316013 ,
    #      "sample_volume": 1159.2379123125,
    # }

    info_mock = {
         "acq_trigger_level": 15.94 ,
         "acq_cytousb_block_size": "Auto (maxTimeOut: 45s )" ,
         "acq_instrument": "ULCO" ,
         "acq_beam_width": 5 ,
         "acq_core_speed": 2 ,
         "acq_user_comments": "",
         "sample_measurement_date": "2022-09-14 12:28:42" ,
         "sample_measurement_duration": 602 ,
         "sample_flow_rate": 2.1 ,
         "sample_channel_1": "Trigger1",
         "sample_channel_2": "FWS L",
         "sample_channel_3": "FWS R" ,
         "sample_channel_4": "SWS" ,
         "sample_channel_4_pmt_level": 50 ,
         "sample_channel_5": "FL Yellow" ,
         "sample_channel_5_pmt_level": 80,
         "sample_channel_6": "FL Orange",
         "sample_channel_6_pmt_level": 80,
         "sample_channel_7": "FL Red  - TRIGGER",
         "sample_channel_7_pmt_level": 80,
         "sample_total_number_of_particles": 11003,
         "sample_smart_triggered_number_of_particles": 11003,
         "sample_concentration": 9.4915805316013 ,
         "sample_volume": 1159.2379123125,
    }

    data = {
        'raw_folder': PurePath(local_path),
        'sample_name': sample_name,
        'txt_infos':  {'filename': filename,
                        'mapping': model,
                        'path': PurePath(local_path , filename),
                        'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                    }
    }

    df : pandas.DataFrame = None

    def _init_df(self) -> pandas.DataFrame:
        df = pd.DataFrame(columns=[key for key in self._model._mapping])
        # for key in self._model._mapping :
        #     # if key:
        #     df[key] =  self._model._mapping[key]['type']
        return df

    def headers(self) -> list:
        l = self.info_mock
        header = [h for h in self.info_mock]
        return header

    def __init__(self) -> None:
        headers = self.headers()
        # self.df = pandas.DataFrame.from_dict(self.info_mock, orient='index', columns=headers)
        # self.df = pandas.DataFrame(self.info_mock)
        # .from_dict(self.info_mock, orient='index', columns=headers)

        self.df = pandas.DataFrame(columns=headers)
        row = [self.info_mock[key] for key in headers]
        self.df.loc[len(self.df)]= row


    def save_csv(self):
        self.df.to_csv(self.path, index=False)




class test_read_infos_file_task(TestCase):

    def test_read_file(self):
        
        mock = mock_ulco_infos_file()

        ut = parse_Infos()
        result = ut._run(mock.data)

        self.assertIn('df_list', result, " -- 'df_list' don't exist")
        self.assertIn('txt_infos', result['df_list'], " -- 'txt_infos' don't exist")

        df_result = result['df_list']['txt_infos']
        df_result.to_csv("tests/cytosense/result/" + mock.csv_filename, index=False)


        from pandas.testing import assert_frame_equal        
        assert_frame_equal( df_result, mock.df )

        # assert "Need to" == "finish this test"




class mock_add_info_file():


    local_path = 'tests/cytosense/ULCO/mock_small_data'
    result_folder = "tests/cytosense/result/"

    sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'

    filename = sample_name +  "_Info" + ".txt"

    path = PurePath( local_path , filename )

    data = {
        'raw_folder': PurePath(local_path),
        'sample_name': sample_name,
    }
   
from Localization.csv_configuration import french_csv_configuration

class test_add_info_file(TestCase):

    def test_arguments(self):
        mock = mock_add_info_file()

        # args = {model= cytosenseModel.Info()  , localisation= french_csv_configuration }
        ut = add_info_file_task(model= cytosenseModel.Info()  , localisation=french_csv_configuration)            
        # self.assertIn("__model",ut)
        ut._run(mock.data)

        self.assertIn( 'txt_infos', ut._data, " -- 'txt_infos' don't exist" )
        self.assertIn( 'path', ut._data['txt_infos'] , " -- 'path' don't exist" )
        self.assertIn( 'csv_configuration', ut._data['txt_infos'] , " -- 'csv_configuration' don't exist" )

        self.assertEqual( ut._data['txt_infos']['path'] , mock.path , " path are different")



class mock_cross_merge():

    local_path = 'tests/cytosense/ULCO/mock_small_data'
    result_folder = "tests/cytosense/result/"

    sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'

    csv_filename = sample_name +  "_Cross_merge" + ".csv"
    mock_filename = "mock_" + csv_filename

    path = PurePath(result_folder, mock_filename)

    data = {}

    def __init__(self) -> None:
        mock_info = mock_ulco_infos_file()
        mock_result = mock_trunc()
    
        self.df = pandas.merge(mock_result.df, mock_info.df, how="cross")

        self.data = {
            'tsv_list':{
                'df_result':{
                    'dataframe':mock_result.df
                    }
                },
            'df_list':{
                'txt_infos':mock_info.df
            }
        }

    def to_csv(self):
        self.df.to_csv(self.path, index=False)


class test_cross_merge(TestCase):

    def test_cross_merge(self):

        mock = mock_cross_merge()
        mock.to_csv()

        ut = cross_merge_task()
        result = ut._run(mock.data)
        df_result: pandas.DataFrame = result['tsv_list']['df_result']['dataframe']

        path = PurePath(mock.result_folder, mock.csv_filename )
        df_result.to_csv(path, index=False)

        from pandas.testing import assert_frame_equal        
        assert_frame_equal( df_result, mock.df )


class test_generate_tsv():

    def test_generate_tsv(self):
        
        pass


def test():
    m = mock_ulco_infos_file()
    headers = m.headers()
    dump(headers)
    m.save_csv()



if __name__ == '__main__':
    test()
