

from unittest import TestCase
from Cytosense.define import NamePatternComponent

from Tools.build_file_name import build_file_name
from Pipeline.Exception.missing_argument import MissingArgumentException


class Test_Build_file_name(TestCase):

    def test_exception_missing_argument(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        
        ut = build_file_name(pattern)
        
        self.assertRaises(MissingArgumentException , ut.get_name )

    def test_exception_missing_second_argument(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        
        ut = build_file_name(pattern)
        self.assertRaises(MissingArgumentException , ut.get_name, eSampleName="toto" )


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

    def test_build_name_twice_patternComponent(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eSampleName, "_Pulses" , ".cvs" ]
        name = "mySample" + "_" + "mySample" + "_Pulses" + ".cvs"

        ut = build_file_name(pattern)
        r = ut.get_name(eSampleName="mySample", eIndex=42 )

        self.assertEqual(r, name)


    def test_path(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eSampleName, "_Pulses" , ".cvs" ]
        name = "mySample" + "_" + "mySample" + "_Pulses" + ".cvs"

        ut = build_file_name(pattern)
        r = ut.get_name(eSampleName="mySample", eIndex="*")
        self.assertEqual(r, name)

    def test_index_path(self):
        pattern = [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        name = "mySample" + "_" + "*" + "_Pulses" + ".cvs"

        ut = build_file_name(pattern)
        r = ut.get_name(eSampleName="mySample", eIndex="*")

        print(r)
        self.assertEqual(r, name)

    def test_image_path(self):
        pattern = [NamePatternComponent.eSampleName,"_Cropped_",NamePatternComponent.eIndex,".jpg"]
        name = "mySample" + "_Cropped_" + "*" + ".jpg"

        ut = build_file_name(pattern)
        r = ut.get_name(eSampleName="mySample", eIndex="*")

        print(r)
        self.assertEqual(r, name)
