


from Cytosense.define import NamePatternComponent
from Pipeline.Exception.missing_argument import MissingArgumentException



class build_file_name():

    def __init__(self, pattern):
        self.pattern = pattern

    def get_name(self, **kwargs ):

        #TODO change this O(n2)
        updatePattern = True
        while updatePattern == True:
            updatePattern = False    
            for component in NamePatternComponent:
                try:
                    name_index = self.pattern.index(str(component.value))
                    self.pattern[name_index] = str(kwargs[str(component.value)])
                    updatePattern = True
                except ValueError:            
                    print("no " + str(component.value) + " pattern")
                except KeyError:
                    raise MissingArgumentException(str(component.value))

        path = "".join(self.pattern)

        return path
    
    # def transfoorm(self, e:NamePatternComponent):
    #     if e == NamePatternComponent.e 

    # def get_path_pattern(self, **kwargs):

    #     pattern_list = []
    #     for i in range(self.pattern):
    #         if type(self.pattern[i]) == type(NamePatternComponent):
    #             pattern_list.append( self.transfoorm(self.pattern[i]) )
    #         else:
    #             pattern_list.append( self.pattern[i])

    #     pattern = "".join(pattern_list)
    #     return pattern
    

