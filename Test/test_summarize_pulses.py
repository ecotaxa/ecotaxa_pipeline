
from pathlib import PurePath
import unittest

from Cytosense.summarise_pulses import CSVException, summarise_pulses




class Test_Summarize_pipeline(unittest.TestCase):

    def test_bad_configuration(self):

        filename = 'nofile'
        utlambda = lambda : summarise_pulses( filename, csv_configuration={ 'wrong_key' : ',' , 'decimal' : '.' } )

        self.assertRaises( CSVException , utlambda )

    def test_bad_configuration_file_not_exist(self):

        filename = 'nofile'
        utlambda = lambda : summarise_pulses( filename )

        self.assertRaises( CSVException , utlambda )

    def test_with_true_file_and_wrong_delimiter(self):
        local_path = 'tests/cytosense/ULCO/mock_small_data'
        sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
        filename = local_path + '/' + sample_name +  '_Pulses.csv'
        # pfilename = PurePath ( local_path , filename)

        utlambda = lambda : summarise_pulses( PurePath(filename) )
        self.assertRaises(CSVException, utlambda)
        #TODO build an Exception class, to didn't mask


