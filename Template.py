# Sebastien Galvagno  06/2023

from typing import List
from ExecuteException import ExecuteException

# from analyze_csv_pulse import ExecuteException
from task import Task


EcotaxaKey = str

class Template:
    
    _mapping = {}
    _keyorder = []
    _name = ""
    
    # def __init__(self, mapping):
    def __init__(self):
        # self._mapping = mapping
        self._keyorder = self._mapping.keys()

    @property
    def mapping(self) -> dict: return self._mapping

    # @property 
    def keyorder(self): return self._keyorder

    @property
    def name(self): return self._name

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
        """
        a debug function to search issue in mapping template
        """
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

    def csv_row_to_ecotaxa_format(self, data):
        """
        insert data in an array following mapping
        map the data from a list copying the 'csv' header format 
        to a list liking the ecotaxa header format
        using the mapping Template
        """
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
    
    invertKey = None
    def invert_key(self):
        self.invertKey = {}
        for key in self._mapping:
            value = self.mapping[key]
            local_header = value['header']
            if not local_header in self.invertKey:
                self.invertKey[local_header] = []
            self.invertKey[local_header].append(key)            

    def searchKeyFromFileHeader(self,header) -> List[EcotaxaKey]:
        if not self.invertKey:
            self.invert_key()

        if not header in self.invertKey:
            raise Exception("Your header '" + header + "' don't exist")
        
        return self.invertKey[header]

    def fn(self, header:EcotaxaKey):
        return self._mapping[header]['fn']
    

    def _apply_fn(self, caller:Task, fn, data):
    # def apply_fn(self, fn, data):
        if fn is None: 
                return data
        # cls = self
        # cls = self._model
        try:
            method = getattr(self, fn)
            return method(self, data, caller)
        except AttributeError:
            # raise 
            # raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))
            # tools.eprint("Function `{}` called in mapping `{}` is not implemented".format(fn, self._mapping))
            raise ExecuteException(self.__class__.__name__, fn)
            # return data
        except Exception as e:
            raise Exception("feature "+e.xx+" use in function "+ fn +" don't exist in "+ caller.__class__.__name__)

    # def cast_value(self,key,value):
    #     if self._mapping[key]['type'] == "[f]":
    #         return 

    def cast_value(self, key: str, value: str, decimal='.'):
        # if self._model._mapping[key]['type'] == "[t]":
        if self._mapping[key]['type'] == "[t]":
            return str(value)

        # if self._model._mapping[key]['type'] == "[f]":
        if self._mapping[key]['type'] == "[f]":
            try:
                # if self._analysing['csv_configuration']['decimal'] == ',':
                if decimal == ',':
                    value = value.replace(',','.')
                if '.' in value or 'E' in value:
                    return float(value)
                else:
                    return int(value)
            except ValueError as e:
                # raise Exception("Cannot cast to numeric value: {} for key: {} mapping", self._model._mapping[key]['type'], key)
                raise Exception(f"Cannot cast to numeric value: for key: '{key}' mapping")

        
        raise Exception("Unknow type: {} for key: {} mapping", self._model._mapping[key]['type'], key)
    

