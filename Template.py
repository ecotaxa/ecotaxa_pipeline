# Sebastien Galvagno  06/2023


class Template:
    
    _mapping = {}
    _keyorder = []
    
    # def __init__(self, mapping):
    def __init__(self):
        # self._mapping = mapping
        self._keyorder = self._mapping.keys()

    @property
    def mapping(self) -> dict:
        return self._mapping

    # @property 
    def keyorder(self):
        return self._keyorder

    def append(self, template):
        #dict = template.mapping()
        #self.mapping = { **self._mapping , **template }
        self.mapping.update(template)
        self._keyorder = self._mapping.keys()



    def _order(self):
        self._keyorder = self._mapping.keys()

    def key(self,key):
        return self._mapping[key]

    def printmapping(self):
        print("-= Mapping =-")
        for k in self.mapping:
            s = ""
            for v in self.mapping[k]:
                s = s + v + ":" + str(self.mapping[k][v]) + ","
            print( k + " -> " + s)

    def additionnal_process(path):
        pass
            
    # def data_to_tsv_format(data: dict):
    #     pass  

    def data_to_tsv_format(self, data):
        # insert data in an array following mapping
        tsvrow = []
        mapping = self.model.mapping
        for tsvkey in mapping:
            map = mapping[tsvkey]
            index = map['index']
            result = self.apply_fn(map['fn'], data[index])
            tsvrow.append(result)
        return tsvrow

    def search_header(self,text):
        for k in self.mapping:
            if text == k['header']:
                return k
        
        return None
    