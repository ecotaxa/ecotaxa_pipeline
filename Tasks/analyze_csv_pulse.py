
import pandas as pd
from Pipeline.Exception.ExecuteException import ExecuteException
from Pipeline.Exception.MappingException import MappingException

from Parser.Template import Template
from Pipeline.task import Task
import Tools.tools as tools

class analyse_csv(Task):
    
    def _init_df(self) -> pd.DataFrame:
        df = pd.DataFrame(columns=[key for key in self._model._mapping])
        # for key in self._model._mapping :
        #     # if key:
        #     df[key] =  self._model._mapping[key]['type']
        return df

    def _add_type(self):
        """
        the second header line: the line indicating types
        """
        row = {}
        print("len:", len(self._model._mapping))
        for key in self._model._mapping:
            print("mapping["+key+"]=" + str(self._model._mapping[key]['type']))
            row[key] = self._model._mapping[key]['type']
        self._df.loc[0]=row

    def map_row(self, model: Template, line_as_array: list[str]) -> dict:
        row = {}
        # raised = False
        for key, value in model._mapping.items():
            if 'index' in value:
                index = value['index']
                if 'fn' in value:
                    try:
                        result = self.apply_fn(value['fn'], line_as_array[index])
                        # row[key] = model.cast_value(key, result)
                        row[key] = model.cast_value( model, key=key, value=result, decimal=self._analysing['csv_configuration']['decimal'])
                    except ExecuteException as e:
                        # tools.eprint("Mapping issue: Function `{}` called in mapping `{}` is not implemented".format(e.functionNamefn, self._mapping))
                        row[key] = line_as_array[index]
                        # raise MappingException(excuteException=e, mapping = self._model, line=(key,value))
                        raise MappingException(executeException=e, model=model, line=(key,value), result=row)
                        # raised = True
                    except IndexError as e:
                        tools.eprint("caught exception: index '"+ str(index) +"' issue on key: " + key , str(e))
                        print(index)
                    except Exception as e:
                        tools.eprint("caught exception: " , str(e))
                        print(index)
                else:
                    # row[key] = model.cast_value(key, line_as_array[index])
                    row[key] = model.cast_value( model, key=key, value=line_as_array[index], decimal=self._analysing['csv_configuration']['decimal'])

        # if raised:
        #     raise MappingException(executeException=e, model=self._model, line=(key,value), result=row)
        return row

    def build_invert_key(self):

        self._dict_csv_ecotaxa = {}
        for ecotaxa_key in self._model._mapping:
            ecotaxa_value = self._model._mapping[ecotaxa_key]
            csv_key = ecotaxa_value['header']
            self._dict_csv_ecotaxa[csv_key]=ecotaxa_key

    def council_headers(self, header):

        line_as_array = header.split(self._analysing['csv_configuration']['delimiter'])
        # line_as_array = list(map(string.strip,line_as_array))
        line_as_array = [item.strip() for item in line_as_array] 

        self.build_invert_key()

        for cvs_key in line_as_array:
            try:
                # search_csv_key = self._model._mapping[ecotaxa_key]['header']
                # search_ecotaxa_key = {i for i in self._model._mapping if self._model._mapping[i]['header']=="cvs_key"}
                ecotaxa_key = self._dict_csv_ecotaxa[cvs_key]

                index_in_csv_header = int(line_as_array.index(cvs_key))
                self._model._mapping[ecotaxa_key]['index']= index_in_csv_header
                print("changed {} ".format(ecotaxa_key))
            except:
                print(cvs_key)
                tools.eprint("Cannot find ", cvs_key)

            #     print(ecotaxa_key)
            #     tools.eprint("Cannot find ",cvs_key," in mapping of ", ecotaxa_key)
            #     tools.eprint("\t", self._model._mapping[ecotaxa_key])
    
        print(self._model._mapping)

    def map_csv_to_df(self) -> pd.DataFrame:
            lines: list[str] = []
        # try :
            with open(self._analysing['path']) as f:
                lines = f.readlines()
            # new_rows=[]
            for line_number, line in enumerate(lines) : 
                print("{}: {}".format(line_number,line) )
                # avoid empty or comments lines
                line = line.rstrip('\n')

                if self.line_filter(line):
                    line_as_array = line.split(self._analysing['csv_configuration']['delimiter'])
                    line_as_array = [item.strip() for item in line_as_array] 
                     #list(map(string.strip,line_as_array))

                    new_row={}
                    try:
                        new_row = self.map_row(self._model, line_as_array)
                    except MappingException as e:
                        tools.eprint("Mapping issue: line number {} - Function `{}` called in mapping is not implemented\n{}".format(line_number, e.functionName, e.line))
                        # if e.result:
                        #     new_row = e.result
                        continue

                    # new_rows.append(new_row)
                    self._df.loc[len(self._df)]= new_row
            # if len(new_rows)>0:
            #     self._df = pd.concat([self._df, pd.DataFrame(new_rows)], ignore_index=True)
        # except UnicodeDecodeError as ude :
        #     print(ude)
        # except KeyError as key:
        #     keyValue = key.args[0]
        #     if keyValue == 'index':
        #         raise Exception("Your cvs ")

        # except Exception as e:
        #     print(e)
        
        # print(df)
        # return df


    def apply_fn(self, fn, data):
        if fn is None: 
                return data
        # cls = self
        cls = self._model
        try:
            method = getattr(cls, fn)
            return method(self._model, data, self)
        except AttributeError:
            # raise 
            # raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))
            # tools.eprint("Function `{}` called in mapping `{}` is not implemented".format(fn, self._mapping))
            raise ExecuteException(cls.__class__.__name__, fn)
            # return data

    # def cast_value(self,key,value:str):
    #     if self._model._mapping[key]['type'] == "[t]":
    #         return str(value)

    #     if self._model._mapping[key]['type'] == "[f]":
    #         if self._analysing['csv_configuration']['decimal'] == ',':
    #             value = value.replace(',','.')
    #         if '.' in value or 'E' in value:
    #             return float(value)
    #         else:
    #             return int(value)
        
    #     raise Exception("Unknow type: {} for key: {} mapping", self._model._mapping[key]['type'], key)



class analyse_csv_cytosense_file(analyse_csv):
    def line_filter(self, line: str):
        # remove the header line
        # processing to verify mapping could be done when the header line has been found
        # and/or simply fill the index column in mapping dict
        if line.startswith("Particle ID"): 
            self.council_headers(line)
            return False
        return True


class analyze_csv_pulse(analyse_csv_cytosense_file):

    _need_keys = [ 'csv_pulse']
    _update_keys = ['tsv_list']
    _model = Template

    _df: pd.DataFrame

    def run(self):
        
        self._fileType = 'csv_pulse'
        self._analysing = self._data[self._fileType]   # self._analysing = self._data['csv_pulse']
        self._model = self._analysing['mapping']       # self._model     = self._data['csv_pulse']['mapping']
        self._df = self._init_df()
        self._add_type() # add type line after processing the data

        self.map_csv_to_df()


        self._data['tsv_pulse']={}
        self._data['tsv_pulse']['dataframe']= self._df

        # self.df.to_csv("tests/cytosense/result/test_analyze_csv_pulse.csv")
        self._df.to_csv("tests/test_analyze_csv_pulse.csv")


    # def _add_type(self):
    #     """
    #     the second header line: the line indicating types
    #     """
    #     row = {}
    #     print("len:", len(self._model._mapping))
    #     for key in self._model._mapping:
    #         print("mapping["+key+"]=" + str(self._model._mapping[key]['type']))
    #         row[key] = self._model._mapping[key]['type']
    #     self._df.loc[0]=row


    # def _init_df(self) -> pd.DataFrame:
    #     df = pd.DataFrame(columns=[key for key in self._model._mapping])
    #     for key in self._model._mapping :
    #         # if key:
    #         df[key] =  self._model._mapping[key]['type']
    #     return df


    # def line_filter(self, line: str):
    #     # remove the header line
    #     # processing to verify mapping could be done when the header line has been found
    #     # and/or simply fill the index column in mapping dict
    #     if line.startswith("Particle ID"): 
    #         self.council_headers(line)
    #         return False
    #     return True




    # marche pas , SUR JE CHERCHE SUR LA CLEF alors qu'il faut chercher sur la donnée
    # def council_headers_booo(self, header):

    #     line_as_array = header.split(self._analysing['csv_configuration']['delimiter'])

    #     for ecotaxa_key in self._model._mapping:
    #         try:
    #             search_csv_key = self._model._mapping[ecotaxa_key]['header']
    #             search_csv_key = {i for i in self._model._mapping if self._model._mapping[ecotaxa_key]['header']=="_______"}

    #             index = int(line_as_array.index(search_csv_key))
    #             self._model._mapping[ecotaxa_key]['index']= index
    #             print("changed {} ".format(ecotaxa_key))
    #         except:
    #             print(ecotaxa_key)
    #             print(search_csv_key)
    #             tools.eprint("Cannot find ",search_csv_key," in mapping of ", ecotaxa_key)
    #             tools.eprint("\t", self._model._mapping[ecotaxa_key])
    
    #     print(self._model._mapping)




