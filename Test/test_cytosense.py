# Sebastien Galvagno 06/2023


from cytosense import CytoSense
from Cytosense.cytosenseModel import cytosenseModel,  pulse, UlcoListmode, Info, CefasListmode
from Tools.tools import print_dict


ulcoModel = cytosenseModel([pulse(), UlcoListmode()]) #, Info()])
#ulcoModel = cytosenseModel([ UlcoListnode()]) #, Info()])
# print_dict(ulcoModel.mapping)




# message_project_creation = {
#   "title" : "mock_small_data",
#   "cpics_raw_path" : "tests/cytosense/ULCO/mock_small_data",
#   "CpicsProcess_path" : "tests/cytosense/result",
#   "model" : ulcoModel
# }
# c = CytoSense(message_project_creation["cpics_raw_path"], 
#               message_project_creation["CpicsProcess_path"], 
#               message_project_creation["model"] , 
#               message_project_creation["title"] , "ULCO v1" )


# message_project_creation = {
#   "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) mock ULCO device_PROJECT",
#   "cpics_raw_path" : "tests/cytosense/ULCO/mock",
#   "CpicsProcess_path" : "tests/cytosense/result",
#   "model" : ulcoModel
# }
# c = CytoSense(message_project_creation["cpics_raw_path"], message_project_creation["CpicsProcess_path"], message_project_creation["model"] , 
#               message_project_creation["title"] , "ULCO" )

# message_project_creation = {
#   "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) mock ULCO device_PROJECT",
#   "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/fichiers_cytometres",
#   "CpicsProcess_path" : "/home/sgalvagno/Test/CytoSense/result",
#   "model" : ulcoModel
# }


# message_project_creation = {
#   "title" : "WORKSHOP_SMALL_CYTOSENSE  ULCO device_PROJECT",
#   "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/ulco",
#   "CpicsProcess_path" : "/home/sgalvagno/Test/CytoSense/result",
#   "model" : ulcoModel
# }

# message_project_creation = {
#   "title" : "R1_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 14h17 PROJECT",
#   "cpics_raw_path" :"/run/user/1004/gvfs/smb-share:server=poseidon.obs-vlfr.fr,share=student/JERICO/Cytosense/export images_pulses_listomode/R1_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 14h17",
#   "CpicsProcess_path" :"/run/user/1004/gvfs/smb-share:server=poseidon.obs-vlfr.fr,share=student/JERICO/Cytosense/result/",
#   "model" : ulcoModel
# }


# message_project_creation = {
#   "title" : "R0_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 15h43_PROJECT",
#   "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/R0_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 15h43",
#   "CpicsProcess_path" : "/home/sgalvagno/Test/CytoSense/result",
#   "model" : ulcoModel
# }



# message_project_creation = {
#   "title" : "R1_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 14h17_PROJECT",
#   "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/R1_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 14h17",
#   "CpicsProcess_path" : "/home/sgalvagno/Test/CytoSense/result",
#   "model" : ulcoModel
# }


# message_project_creation = {
#   "title" : "R2_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 13h29_PROJECT",
#   "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/R2_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 13h29",
#   "CpicsProcess_path" : "/home/sgalvagno/Test/CytoSense/result",
#   "model" : ulcoModel
# }


# message_project_creation = {
#   "title" : "R0_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 15h43_PROJECT",
#   "cpics_raw_path" : "tests/cytosense/ULCO/R0_010421_photos_flr26_5ul_10min_LOWER_PMT 2021-04-01 15h43",
#   "CpicsProcess_path" : "tests/cytosense/result",
#   "model" : ulcoModel
# }

# c = CytoSense(message_project_creation["cpics_raw_path"], 
#               message_project_creation["CpicsProcess_path"], 
#               message_project_creation["model"] , 
#               message_project_creation["title"] , "ULCO" )



# TODO allow to copy all or sync or juste add if new 
# Copy raw data in export folder
#c.copy_raw_data()

# Process data to generate TSV and vignette to export
# c.process_project()

# Import in ecotaxa
# c.import_in_ecotaxa()


modelCefas = cytosenseModel([pulse(), CefasListmode()]) #, Info()])
# print_dict(modelCefas.mapping)
#print_dict(modelCefas.key['object_id'])



import unittest

class Test_Tasks(unittest.TestCase):

  def test_cytosense(self):
    message_project_creation = {
      "title" : "mock_small_data",
      "cpics_raw_path" : "tests/cytosense/ULCO/mock_small_data",
      "CpicsProcess_path" : "tests/cytosense/result",
      "model" : ulcoModel
    }
    ut = CytoSense(message_project_creation["cpics_raw_path"], 
                  message_project_creation["CpicsProcess_path"], 
                  message_project_creation["model"] , 
                  message_project_creation["title"] , "ULCO v1" )
    self.run(ut)

  def test_cefas_cytosense(self):
    message_project_creation = {
      "title" : "WORKSHOP_SMALL_CYTOSENSE (data from) Cefas III device_PROJECT",
      "cpics_raw_path" : "/home/sgalvagno/Test/CytoSense/Pond_NA",
      "CpicsProcess_path" : "/home/sgalvagno/Test/CytoSense/result",
      "model" : modelCefas
    }
    ut = CytoSense(message_project_creation["cpics_raw_path"], 
              message_project_creation["CpicsProcess_path"], 
              message_project_creation["model"] , 
              message_project_creation["title"] )
    self.run(ut)


  def run(self ,c):
    # TODO allow to copy all or sync or juste add if new 
    # Copy raw data in export folder
    #c.copy_raw_data()

    # Process data to generate TSV and vignette to export
    c.process_project()

    # Import in ecotaxa
    # c.import_in_ecotaxa()

if __name__ == '__main__':
    unittest.main()
