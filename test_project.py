# Sebastien Galvagno 06/2023



from cpics import CPICsProject 
from cpicsModel import cpicsModel

#def __main__():
roisModel = cpicsModel()
roisModel.addCtd()
#roisModel.printmodel()
#roisModel.printmapping()

c = CPICsProject("/home/sgalvagno/Test/cpics",roisModel)
c.generateProject("/home/sgalvagno/Test/cpicsEcotaxa")