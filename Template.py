# Sebastien Galvagno  06/2023


class Template:
    
    _mapping = {}
    
    @property
    def mapping(self) -> dict:
        return self._mapping
    
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
    