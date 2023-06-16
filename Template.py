# Sebastien Galvagno  06/2023


class Template:
    
    _mapping = {}
    _mapping_img = {}
    
    @property
    def mapping(self) -> dict:
        return self._mapping
    @property
    def mapping_img(self) -> dict:
        return self._mapping_img
    
    def append(self,template):
        #dict = template.mapping()
        #self.mapping = { **self._mapping , **template }
        self.mapping.update(template)

    def printmapping(self):
        print("-= Mapping =-")
        for k in self.mapping:
            s = ""
            for v in self.mapping[k]:
                s = s + v + ":" + str(self.mapping[k][v]) + ","
            print( k + " -> " + s)

            
