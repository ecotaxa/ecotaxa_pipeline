

from enum import Enum


# NamePatternComponent = Enum('NamePatternComponent', ['eSampleName' , 'eIndex', 'eImageType'])


class NamePatternComponent(str, Enum):
    eSampleName='eSampleName' 
    eIndex='eIndex'
    eImageType='eImageType'



# FileExtension = Enum ( 'FileExtension', [] )

cefas_pulse_file_pattern = [ NamePatternComponent.eSampleName , "_Pulses" , ".csv" ]
cefas_pulse_file_pattern_extra_info = [ NamePatternComponent.eSampleName , "_All_images\ Particles" , "_Pulses" , ".csv" ]
cefas_listmode_file_pattern = [ NamePatternComponent.eSampleName , "_Listmode" , ".csv" ]
cefas_listmode_file_pattern_extra_info = [ NamePatternComponent.eSampleName , "_All_images\ Particles" , "_Listmode" , ".csv" ]

cefas_image_file_pattern = [ NamePatternComponent.eSampleName ,
                             "_" , NamePatternComponent.eImageType, "_" , NamePatternComponent.eIndex  , ".csv" ]

ulco_pulse_file_pattern = cefas_pulse_file_pattern
ulco_listmode_file_pattern = cefas_listmode_file_pattern

