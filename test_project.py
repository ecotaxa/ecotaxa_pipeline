# Sebastien Galvagno 06/2023



from cpics import CPICsProject 
from cpicsModel import cpicsModel, CTD_sbe37

#def __init__():

ctdModel=CTD_sbe37()
# ctdModel.printmapping()
roisModel = cpicsModel(ctdModel)

# roisModel.printmapping()

c = CPICsProject("/home/sgalvagno/Test/cpics", roisModel)
c.generateProject("/home/sgalvagno/Test/cpicsEcotaxa")