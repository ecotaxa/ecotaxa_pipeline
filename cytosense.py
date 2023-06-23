


import os
from ParserToTsv import ParserToTsv
from project import Project2
from enums import Instrument
from pathlib import Path
from filter import dynamic_filter, file_filter_composition, filter_extension, filter_folder, filter_hiddenFile
# from summarise_pulses import save_dataframe_to_csv, summarise_pulses

from tools import copy_to_file, expand_zip_in_folder
from tsv import Tsv



class CytoSense(Project2):

    # if use_pandas = True polynomial coeficient will be calculated 
    # else a mock file (pulse_fits.cvs) will be use
    use_pandas = True   # to remove when pandas install fixed
    # use_pandas = False   # to remove when pandas install fixed

    def pulse_fits_path(self):
        # return self.raw_data_path + "/../../"/+ "pulse_fits" + ".csv"
        return "/usr/src/app/tests/cytosense/pulse_fits.csv"


    # _read = []
    filename = ""
    data_filename = ""

    _tempTsv = {}
    _pulsesData = {}
    _listModeData = {}
    tsv = None

    delimiter = ","
    float_format="."

    def __init__(self, raw_data_path, data_to_export_base_path, cytoSense_model, title, type = "Cefas"):
    
        if type == "ULCO":
            self.delimiter = ";"
            self.float_format=","
            self.device = "ULCO"
        if type == "ULCO v1":
            self.delimiter = ";"
            self.float_format=","
            self.device = "ULCO v1"

        if type == "Cefas":
            self.delimiter = ","
            self.float_format=";"
            self.device = "Cefas"


        data_to_export_base_working_path = data_to_export_base_path
        super().__init__(raw_data_path, data_to_export_base_path, cytoSense_model, title, Instrument.CYTOSENSE)
        
    def copy_raw_data(self):
        #TODO
        pass

    def define_id(self, data):
        return self.folder['destFolder'] + data
    
    def extract_name(self, path):
        # print("extract_name() " + path)
        splitname = path.split("_")
        string_to_cut = splitname[len(splitname)-1]
        filename = path[:-len(string_to_cut)-1]
        #print("extract :" + filename)
        return str(filename)
        
    # def filter(self, path: Path):
    #     if not path.is_file():
    #         return False
    #     # print("hidden file: "+str(path.name)[0]+ " <== " + str(path.name))
    #     if str(path.name)[0]==".": return False
    #     # print("filter:"+str(path.name)[-4:])

    #     if extension == ".zip":
    #         name = self.extract_name(path.name)
    #         folder = self.raw_data_path + "/" + name + "_Images"
    #         expand_zip_in_folder(path,folder)

    #     # if extension == ".cyz" or extension == ".txt"  or extension == ".jpg":
    #     #     # print("eject")
    #     #     return False
    #     # return True

    #     extension = str(path.name)[-4:]
    #     return not self.filter_extension(extension, [".cyz", ".txt", ".jpg"])


    # def filter_extension(self, extension, extensions: list):
    #     if extension in extensions:
    #         return True
    #     return False

    # import filter

    filters = file_filter_composition([
                filter_hiddenFile(),
                filter_folder(),
                filter_extension([".cyz", ".txt", ".jpg"])
        ])
    
    zipFilter = filter_extension([".zip"])

    file_analyzed_filter = dynamic_filter()

    def process_project(self):  
        for path in os.scandir(self.raw_data_path):
            print("found file:" + path.name)
            if self.filters.filter(path):
                print("next "+ path.name)
                continue

            if self.zipFilter.filter(path):
                name = self.extract_name(path.name)
                folder = self.raw_data_path + "/" + name + "_Images"
                expand_zip_in_folder(path, folder)

            filename = self.extract_name(path.name)
            print("analysing filename = " + filename)

            if not self.file_analyzed_filter.filter(filename):
                self.file_analyzed_filter.add_new_filter_items(filename)
                self.analyse(filename)
            else:
                print("over: " + filename)
            
    def rois_path(self):
        return  os.path.join(self.raw_data_path, "/")


    def analyse_Pulse(self,filename,parser:ParserToTsv):
        self.filename = filename

        self.data_filename = "Pulses"

        if not self.use_pandas:

            pulses_filename = self.pulse_fits_path() 
            parser.read_csv_filecyto( pulses_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn2"})
        else:
            from summarise_pulses import save_dataframe_to_csv, summarise_pulses
            pulses_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
            poly = summarise_pulses(pulses_filename)
            poly_filename = self.raw_data_path +"/poly/"+filename + "_" + self.data_filename + ".csv"
            save_dataframe_to_csv(poly, poly_filename)
            parser.read_csv_filecyto( poly_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn2"})


    def analyse_Listmode(self, filename, parser:ParserToTsv):
        self.data_filename = "Listmode"
        listmode_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
        parser.read_csv_filecyto( listmode_filename, self.project_path,{"delimiter":self.delimiter , "fn":"listModeRowFn"})


    def analyse(self, filename):

        print("Analyse " + filename )

        self.filename = filename
        folder = self.define_folders(filename)

        self.data_filename = "Pulses"

        parser = ParserToTsv(self)
        # pulses_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
        # parser.read_csv_filecyto( pulses_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn"})

        # if not self.use_pandas:

        #     pulses_filename = self.pulse_fits_path() 
        #     parser.read_csv_filecyto( pulses_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn2"})
        # else:
        #     from summarise_pulses import save_dataframe_to_csv, summarise_pulses
        #     pulses_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
        #     poly = summarise_pulses(pulses_filename)
        #     poly_filename = self.raw_data_path +"/poly/"+filename + "_" + self.data_filename + ".csv"
        #     save_dataframe_to_csv(poly, poly_filename)
        #     parser.read_csv_filecyto( poly_filename, self.project_path,{"delimiter":"," , "fn":"pulseRowFn2"})

        self.analyse_Pulse(filename, parser)

        # self.data_filename = "Listmode"
        # listmode_filename = self.raw_data_path +"/"+filename + "_" + self.data_filename + ".csv"
        # parser.read_csv_filecyto( listmode_filename, self.project_path,{"delimiter":self.delimiter , "fn":"listModeRowFn"})

        self.analyse_Listmode(filename, parser)

        # move in analyse (do it after scan the 3 files)
        # self._tsv = self.init_tsv()
        # tsvName = self._tsv.tsv_format_name( folder['tsvName'] )
        # self._tsv.generate_tsv(folder['destFolder'] / tsvName)

        self.copy_images(folder)
        self.store_data_in_tsv(folder)
    

    def copy_images(self, folder):
        list_to_remove = []
        row_to_add = {}
        for object_id in self._tempTsv.keys():
            cytosense_id=object_id.split("_")[-1:][0]
            images = self.images(cytosense_id)
            nbImages = 0  # must be < 10
            nbImagesAdded = 0
            for i in images:
                r = copy_to_file(Path(self.raw_data_path +"/"+folder['tsvName']+"_Images"+"/"+i), folder['destFolder'])
                if not r:
                    # copy_to_file(Path("img/empty.jpg"), folder['destFolder'], True, i)
                    # if nbImages < 1:
                    # list_to_remove.append(object_id)
                    pass
                else:
                    if nbImages > 0:
                        row = self.add_rank(object_id, nbImages,images[nbImages])
                        row_to_add.update(row)
                    nbImages += 1
                    nbImagesAdded+=1
            else:
                if nbImagesAdded == 0:
                    list_to_remove.append(object_id)

        for k in list_to_remove:
            try:
                del self._tempTsv[k]
            #del row_to_add[k]
            except:
                pass
        for key in row_to_add:
            # //self._tempTsv.update(row_to_add[k])
            self._tempTsv[key]=row_to_add[key]
            # for k in row_to_add[key]:
            #     self._tempTsv[k]=row_to_add[key][k]

    def add_rank(self, index, rank, image):
        # add the id_rank in the feature
        dic = {}
        import copy
        row = self._tempTsv[index]
        rowcopy = copy.deepcopy(row)

        # print(hex(id({1:1,2:2})))

        # print(type(row))
        # rowid = id(row)
        # rowcopyid = id(rowcopy)

        # print("pointers "+hex(id(row))+' '+hex(id(rowcopy)))

        # print("    row[index]['img_rank'] :"   + str(row    [index]['img_rank']))
        # print("rowcopy[index]['img_rank'] :" + str(rowcopy[index]['img_rank']))


        rowcopy[index]['img_rank']=rank
        rowcopy[index]['img_file_name']=image

        # print("    row[index]['img_rank'] :"   + str(row    [index]['img_rank']))
        # print("rowcopy[index]['img_rank'] :" + str(rowcopy[index]['img_rank']))


        # self._tempTsv[id+"_"+ str(rank)] = row
        #return { id+"_"+ str(rank) : row }
        dic[index+"_"+ str(rank)] = rowcopy
        return dic

    def store_data_in_tsv(self, folder):
        tsv = self.init_tsv()
        tsvName = tsv.tsv_format_name( folder['tsvName'] )
        # work_object_id is just a stupid id to store the different rank use in the temporary TempTsv
        # it will be better to use true_id : [  { id_rank:0}, { id_rank:1} ]
        for work_object_id in self._tempTsv.keys():
            row = self._tempTsv[work_object_id]
            self.data_to_tsv_format2(tsv, row)
            #tsv.addData(row)
        tsv.generate_tsv(folder['destFolder'] / tsvName , self._tempTsv)

    def listModeRowFn(self, data: dict):
        id = data['object_id']
        self._listModeData[id] = data

    def pulseRowFn2(self, data: dict):
        id = data['object_id']
        self._pulsesData[id] = data

    def pulseRowFn(self, data: dict):
        id = data['object_id']
        if id in self._pulsesData:
            pulse = self._pulsesData[data['object_id']]
        else:
            pulse = { 'object_fws':[],"object_sws":[],"object_fl_erllow":[],"object_fl_orange":[],"object_fl_red":[],"object_curvature":[]}
        #pulse[]
        #concat signal

        # index = ['object_fws',"object_sws","object_fl_erllow","object_fl_orange","object_fl_red","object_curvature"]

        for i in pulse.keys():
            
            pulse[i].append(data[i])

        # update the pulse
        self._pulsesData[id] = pulse
    
    def store(self, name):
        if name == "Pulse":
            # if self._pulsesData['object_id'] in self._tempTsv:
            #     self._tempTsv[self._pulsesData['object_id']].update(self._pulsesData)
            # else:
            #     self._tempTsv[self._pulsesData['object_id']] = self._pulsesData
            for k in self._pulsesData:
                # self._tempTsv[self._listModeData['object_id']] = self._listModeData
                if k in self._tempTsv:
                    self._tempTsv[k].update(self._pulsesData)
                else:    
                    self._tempTsv[k] = self._pulsesData

        if name == "Mode":
            # if self._listModeData['object_id'] in self._tempTsv:
            #     self._tempTsv[self._listModeData['object_id']].update(self._listModeData)
            # else:
            for k in self._listModeData:
                print("store: "+k)
                # self._tempTsv[self._listModeData['object_id']] = self._listModeData
                if k in self._tempTsv:
                    self._tempTsv[k].update(self._listModeData)
                else:
                    self._tempTsv[k] = self._listModeData
            self._listModeData={}

    def images(self, index):
        if self.device == "ULCO":
            return [
                self.filename +  "_" + index + "_" + "cropped" +".jpg",
                self.filename +  "_" + index + "_" + "pulse" +".jpg",
            ]
        else:
            if self.device == "Cefas" or self.device == "ULCO v1" :
                return [
                    self.filename + "_" + "Cropped" + "_" + index + ".jpg",
                    # self.filename + "_" + "Uncropped" + "_" + index + ".jpg",
                    self.filename +  "_" + "Pulse" + "_" + index + ".jpg",
                ]
            else:
                raise("Your device is unknown")

    def rank(self, r):
        return 0

    def image(self, index):
        return self.images(index)[0]
        #return self.filename + "_" + "Cropped" + "_" + index + ".jpg"


    def define_folders(self, name):
        imageName = Path(self.raw_data_path) / (name + "_Images") / (name + "_Cropped") # missing "_" + id + ".jpg"
        destFolder = Path(self.project_path) / "_work"
        return { 'destFolder': destFolder, 'imageName': imageName , 'tsvName': name }

    # def data_to_tsv_format(self, data):
    #     self.model.data_to_tsv_format(data)

    def data_to_tsv_format(self, data):
        # insert data in an array following mapping
        tsvrow = {}
        mapping = self.model.mapping
        
        # build the row
        for tsvkey in mapping:
            map = mapping[tsvkey]
            if tsvkey != 'object_id':
                if map['file'] != None:
                    if map['file'] != self.data_filename: continue

            index = map['index']

            result = self.apply_fn(map['fn'], data[index])

            if self.float_format == ',':
                if map['type']=='[f]':
                    # result = self.change_to_point(result)
                    result = str(result).replace(",", "." )
            
            #tsvrow.append(result)

            # print("data_to_tsv_format - add row: " + str(data[0]))
            tsvrow[tsvkey]=result

        # keyorder = self.model.keyorder()
        # rowResult = order_dict(tsvrow, keyorder )

        return tsvrow
        # return rowResult

    # def change_to_point(data):


    def data_to_tsv_format2(self, tsv: Tsv, data):
    # def data_to_tsv_format2(self, tsv: Tsv, dataKey):
        # insert data in an array following mapping
        # tsvrow = {}
        # result = []
        mapping = self.model.mapping
        print("data_to_tsv_format2 - data len ", len(data))
        #for dataKey in data:
        dataKey = list(data.keys())[0]    
        # if not dataKey in data:
        result = []
        for tsvkey in mapping:
            d = data[dataKey]
            if tsvkey in d:
                result.append(d[tsvkey])
            else:
                print('missing key:' + tsvkey)
        
        #result.append(data[])
        print("data_to_tsv_format - add row: " +result[0])
        tsv.addData(result)
        
        #tsvrow.append(result)
        #tsvrow[tsvkey]=result

        # keyorder = self.model.keyorder()
        # rowResult = order_dict(tsvrow, keyorder )

        #return tsvrow
        #return rowResult



    def define_id(self, data):
        return self.filename + "_" + data

    def sample_id(self, data):
        return self.filename