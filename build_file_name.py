


from Cytosense.define import NamePatternComponent
from Pipeline.Exception.missing_argument import MissingArgumentException



class build_file_name():

    def __init__(self, pattern):
        self.filename_pattern = pattern

    def get_name(self, **kwargs ):
        # def build_name(self):
        # [ NamePatternComponent.eSampleName , "_", NamePatternComponent.eIndex, "_Pulses" , ".cvs" ]
        pattern = self.filename_pattern #.copy()

        try:
            name_index = pattern.index(str(NamePatternComponent.eSampleName.value))
            pattern[name_index] = kwargs['eSampleName']
        except ValueError:            
            print("no eSampleName pattern")
        except KeyError:
            raise MissingArgumentException("eSampleName")

        try:
            name_index = pattern.index(NamePatternComponent.eIndex)
            pattern[name_index] = str(kwargs['eIndex'])
        except ValueError:
            pass
            print("no eIndex pattern")
        except KeyError:
            raise MissingArgumentException(NamePatternComponent.eIndex.value)

        path = "".join(pattern)
        return path
    

