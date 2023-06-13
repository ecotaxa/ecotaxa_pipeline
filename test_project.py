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

ctdModel=CTD_sbe37()
# ctdModel.printmapping()
roisModel = cpicsModel(ctdModel)

# roisModel.printmapping()

# Create new project in CpicsProcess
# POST /project/
message_project_creation = {
  "title" : "WORKSHOP_SMALL_CPICS_PROJECT",
  "cpics_raw_path" : "/Users/jcoustenoble/Desktop/CPICS_RAW/WORKSHOP_SMALL_CPICS_PROJECT",
  "CpicsProcess_path" : "/Users/jcoustenoble/Desktop/CPICS_EXPORT",
  "model" : roisModel
}

# Create project instance and folder
c = CPICsProject(message_project_creation["cpics_raw_path"], message_project_creation["CpicsProcess_path"], message_project_creation["model"] , message_project_creation["title"])

# TODO allow to copy all or sync or juste add if new 
# Copy raw data in export folder
c.copy_raw_data()

# Process data to generate TSV and vignette to export
c.process_project()

# Import in ecotaxa
c.import_in_ecotaxa()
