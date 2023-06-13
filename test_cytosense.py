# Sebastien Galvagno 06/2023


from cytosense import cytosense
from cytosenseModel import cytosenseModel ,  pulse,Listnode, Info, CefasListNode


model = cytosenseModel([pulse(), Listnode(), Info()])

modelCefas = cytosenseModel([pulse(), CefasListNode(), Info()])


message_project_creation = {
  "title" : "WORKSHOP_SMALL_CPICS_PROJECT",
  "cpics_raw_path" : "/home/sgalvagno/Test",
  "CpicsProcess_path" : "/home/sgalvagno/cpicsEcotaxa",
  "model" : cytosenseModel
}

