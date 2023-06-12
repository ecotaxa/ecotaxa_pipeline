# Sebastien Galvagno 06/2023

import csv
from tools import eprint


class ParserToTsv:

    def __init__(self, project):
        self._model = project
        self._tsv = self._model.initTsv()


    def readCVSFile(self,filename, destPath):
        print ("processing: " + filename)
        with open(filename,"r") as roiFile:
            reader = csv.reader( roiFile )

            #for data in reader:
            line = -1
            while True:
                line +=1
                try:
                    data = next(reader)
                except StopIteration:
                    break
                except csv.Error:
                    eprint("Cannot read file \"" + filename + "\" at line " + str(line))
                    continue
                except IOError:
                    continue
                else:
                    # to filtering the commented line, 
                    # in the sample data we have a file named 20191202.roicoordswithheader.txt 
                    # that contain the header
                    if data[0][0] == "#" or data[0][0] == "^@":
                        continue
                    imageName = data[2]
                    folder = self._model.defineFolders(imageName, destPath)
                    
                    self._model.createFolder(folder['destFolder'])

                    additionaldata = self._model.additionnalProcess(folder['imageName']) #TODO change function name

                    status = self._model.copyFileTo( folder['imageName'], folder['destFolder'])
                    #print("status:" + str(status) )

                    if status:
                        tsvrow = self._model.dataToTsvFormat(data)
                        self._tsv.addData(tsvrow)

            #tsvName = self.id(name) + ".tsv"
            tsvName = self._tsv.tsvFormatName( folder['tsvName'] )
            self._tsv.generate_tsv(folder['destFolder'] / tsvName)


