# Sebastien Galvagno 06/2023


from cytosense import CytoSense
from cytosenseModel import cytosenseModel ,  pulse,Listnode, Info, CefasListNode
from tools import print_dict


model = cytosenseModel([pulse(), Listnode(), Info()])

modelCefas = cytosenseModel([pulse(), CefasListNode()]) #, Info()])



print_dict(modelCefas.mapping)
# print_dict(modelCefas.key['object_id'])

message_project_creation = {
  "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) Cefas III device_PROJECT",
  "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/Pond_NA",
  "CpicsProcess_path" : "/home/sgalvagno/Test/cytosense_cefas_result",
  "model" : modelCefas
}


c = CytoSense(message_project_creation["cpics_raw_path"], message_project_creation["CpicsProcess_path"], message_project_creation["model"] , message_project_creation["title"])



# TODO allow to copy all or sync or juste add if new 
# Copy raw data in export folder
#c.copy_raw_data()

# Process data to generate TSV and vignette to export
c.process_project()

# Import in ecotaxa
# c.import_in_ecotaxa()
