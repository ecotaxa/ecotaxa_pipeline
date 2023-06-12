# Sebastien Galvagno 06/2023



from cpics import CPICsProject 
from cpicsModel import cpicsModel, CTD_sbe37

# def __main__():
ctdModel=CTD_sbe37()
roisModel = cpicsModel(ctdModel)

# c = CPICsProject("/home/share/cpics_test_data/cpics/data_test/CPICSM160/cpics",roisModel)
# c.generateProject("/home/sgalvagno/cpicsEcotaxa")
