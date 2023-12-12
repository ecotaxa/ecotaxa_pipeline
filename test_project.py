# Sebastien Galvagno 06/2023
from cpics import CPICsProject 
from cpicsModel import cpicsModel, CTD_sbe37

'''
paths on complex
"/home/share/cpics_test_data/cpics/data_test/CPICSM160"
"/home/sgalvagno/cpicsEcotaxa"
'''
'''
paths for sebastien
"/home/sgalvagno/Test/"
"/home/sgalvagno/Test/cpicsEcotaxa"
'''

raw_data_path="/Users/jcoustenoble/Desktop/CPICS_RAW/WORKSHOP_SMALL_CPICS_PROJECT"
dest_data_path="/Users/jcoustenoble/Desktop/CPICS_EXPORT"

ctdModel=CTD_sbe37()
# ctdModel.printmapping()
roisModel = cpicsModel(ctdModel)

# roisModel.printmapping()

# Create new project in CpicsProcess
# POST /project/
message_project_creation = {
  "title" : "WORKSHOP_SMALL_CPICS_PROJECT",
  "raw_data_path" : raw_data_path,
  "dest_data_path" : dest_data_path,
  "model" : roisModel,
  "sample_level" : {    
                        "Type" : "CAST", #cast or time
                        "bin" : ""
                   },
  "subsample_level" : {   
                        "Type" : "DEPTH", #depth or time
                        "bin_m" : 5
                      },
  "GPS_coord" : {   
                    "method" : "", #Path to file, CTD, Const
                    "value" : ""
                }
}
# Fix latitude longitude / or path to file
# sample
# subsample



# Create project instance and folder
c = CPICsProject(message_project_creation)

# TODO allow to copy all or sync or juste add if new 
# Copy raw data in export folder
c.copy_raw_data()

# Process data to generate TSV and vignette to export
c.process_project()

# Import in ecotaxa
c.import_in_ecotaxa()
