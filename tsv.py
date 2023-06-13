# Sebastien Galvagno 

import csv


class Tsv:
    """class to generate ecotaxa tsv"""

    def __init__(self):
        self.header = [] #["img_file_name", "object_id"]
        self.unit = [] # ["[t]", "[t]"]
        self.data = []

    # type : img, object, process, acq, sample

    def add_feature(self,type,label,unit):
        key = label
        if type != "":
            key = type+"_"+label

        if not key in self.header:
            self.header.append(key)
            self.unit.append(unit)

    def add_data(self, img, id, data = []):
        if self.check(data):
            dat=[img,id]+data
            self.data.append(dat)
        else:
            raise Exception("missing data in the array",img,id,data)

    def addData(self, data = []):
        if self.check(data):
            self.data.append(data)
        else:
            self.showHeader(self)
            raise Exception("missing data in the array", data)


    # def addData(self, data = []):
    #     if data == []: return
    #     id = data['object_id']

    #     if id in self.data:
    #         self.data.append(data)
    #     else:
    #         self.data = data
            
    #     if self.check(data):
    #         self.data.append(data)
    #     else:
    #         self.showHeader(self)
    #         raise Exception("missing data in the array", data)
        

    def check(self, data):
        #return len(data)+2 == len(self.header)
        return len(data) == len(self.header)

    def generate_tsv(self,filename):
        print("write " + str(filename))
        with open(filename, 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(self.header)
            tsv_writer.writerow(self.unit)
            for data in self.data:
                tsv_writer.writerow(data)

    def showHeader(self):
        print(', '.join(map(str, self.header))) 

    def tsv_format_name(self,name):
        return "ecotaxa_" + name + ".tsv"
