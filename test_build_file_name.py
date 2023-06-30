

from unittest import TestCase
from Cytosense.define import NamePatternComponent

from build_file_name import build_file_name
from Pipeline.Exception.missing_argument import MissingArgumentException


class Test_Build_file_name(TestCase):

    def test_exception_missing_argument(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        
        ut = build_file_name(pattern)
        
        self.assertRaises(MissingArgumentException , ut.get_name )

    def test_exception_missing_argument(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        
        ut = build_file_name(pattern)
        ut.get_name (eSampleName="toto")
        # self.assertRaises(MissingArgumentException , ut.get_name, eSampleName="toto" )


    def test_exception_no_enum_in_pattern(self):
        pattern = [ "blabla" , "_", "NamePatternComponent.eIndex", "_Pulses" , ".cvs" ]
        name = "blabla" + "_" + "NamePatternComponent.eIndex" + "_Pulses" + ".cvs"
        
        ut = build_file_name(pattern)
        r = ut.get_name()

        self.assertEqual(r,name)
                         
    def test_build_name(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        name = "mySample" + "_" + "42" + "_Pulses" + ".cvs"

        ut = build_file_name(pattern)
        r = ut.get_name(eSampleName="mySample", eIndex=42 )

        self.assertEqual(r,name)

