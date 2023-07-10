# test_read_infos_file_task

from pathlib import PurePath
from unittest import TestCase

import cytosenseModel
from debug_tools import dump
from read_Infos_file_Task import parse_Infos

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


    info_mock2 = {
         "acq_trigger_level": 15.94 ,
         "acq_cytousb_block_size": "Auto (maxTimeOut: 45s )" ,
         "acq_instrument": "ULCO" ,
         "acq_beam_width": 5 ,
         "acq_core_speed": 2 ,
         "sample_measurement_date": "2022-09-14 12:28:42" ,
         "acq_user_comments": None,
         "sample_measurement_duration": 602 ,
         "sample_flow_rate": 2.1 ,
         "sample_channel_1": "Trigger1",
         "sample_channel_2": "FWS L",
         "sample_channel_3": "FWS R" ,
         "sample_channel_4": "SWS" ,
         "sample_channel_4_pmt_level": 80 ,
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

    info_mock = {
         "acq_trigger_level": [15.94] ,
         "acq_cytousb_block_size": ["Auto (maxTimeOut: 45s )"] ,
         "acq_instrument": ["ULCO"] ,
         "acq_beam_width": [5] ,
         "acq_core_speed": [2] ,
         "sample_measurement_date": ["2022-09-14 12:28:42"] ,
         "acq_user_comments": [None],
         "sample_measurement_duration": [602] ,
         "sample_flow_rate": [2.1] ,
         "sample_channel_1": ["Trigger1"],
         "sample_channel_2": ["FWS L"],
         "sample_channel_3": ["FWS R"] ,
         "sample_channel_4": ["SWS"] ,
         "sample_channel_4_pmt_level": [80] ,
         "sample_channel_5": ["FL Yellow"] ,
         "sample_channel_5_pmt_level": [80],
         "sample_channel_6": ["FL Orange"],
         "sample_channel_6_pmt_level": [80],
         "sample_channel_7": ["FL Red  - TRIGGER"],
         "sample_channel_7_pmt_level": [80],
         "sample_total_number_of_particles": [11003],
         "sample_smart_triggered_number_of_particles": [11003],
         "sample_concentration": [9.4915805316013] ,
         "sample_volume": [1159.2379123125],
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

    def headers(self) -> list:
        l = self.info_mock
        header = [h for h in self.info_mock]
        return header

    def __init__(self) -> None:
        headers = self.headers()
        row = [self.info_mock[key] for key in headers]
        # self.df = pandas.DataFrame.from_dict(self.info_mock, orient='index', columns=headers)
        self.df = pandas.DataFrame(self.info_mock)
        # .from_dict(self.info_mock, orient='index', columns=headers)
        pass


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

        assert "Need to" == "finish this test"



def test():
    m = mock_ulco_infos_file()
    headers = m.headers()
    dump(headers)
    m.save_csv()



if __name__ == '__main__':
    test()
