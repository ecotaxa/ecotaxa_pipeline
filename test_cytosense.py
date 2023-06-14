# Sebastien Galvagno 06/2023


from cytosense import CytoSense
from cytosenseModel import cytosenseModel ,  pulse, UlcoListnode, Info, CefasListNode
from tools import print_dict


ulcoModel = cytosenseModel([pulse(), UlcoListnode()]) #, Info()])
#ulcoModel = cytosenseModel([ UlcoListnode()]) #, Info()])
# print_dict(ulcoModel.mapping)

modelCefas = cytosenseModel([pulse(), CefasListNode()]) #, Info()])
# print_dict(modelCefas.mapping)
#print_dict(modelCefas.key['object_id'])

message_project_creation = {
  "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) Cefas III device_PROJECT",
  "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/Pond_NA",
  "CpicsProcess_path" : "/home/sgalvagno/Test/cytosense_cefas_result",
  "model" : modelCefas
}


message_project_creation = {
  "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) Cefas III device_PROJECT",
  "cpics_raw_path" : "tests/cytosense/Cefas/mock",
  "CpicsProcess_path" : "tests/cytosense/result",
  "model" : modelCefas
}
c = CytoSense(message_project_creation["cpics_raw_path"], message_project_creation["CpicsProcess_path"], message_project_creation["model"] , 
              message_project_creation["title"] )


# message_project_creation = {
#   "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) ULCO device_PROJECT",
#   "cpics_raw_path" : "tests/cytosense/ULCO/mock_small_data",
#   "CpicsProcess_path" : "tests/cytosense/result",
#   "model" : ulcoModel
# }

# c = CytoSense(message_project_creation["cpics_raw_path"], message_project_creation["CpicsProcess_path"], message_project_creation["model"] , 
#               message_project_creation["title"] , "ULCO" )



# TODO allow to copy all or sync or juste add if new 
# Copy raw data in export folder
#c.copy_raw_data()

# Process data to generate TSV and vignette to export
c.process_project()

# Import in ecotaxa
# c.import_in_ecotaxa()
