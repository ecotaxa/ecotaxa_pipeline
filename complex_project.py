# Sebastien Galvagno 06/2023



from cpics import CPICsProject 
from cpicsModel import cpicsModel

def __main__():
    roisModel = cpicsModel()
    roisModel.addCtd()

    c = CPICsProject("/home/share/cpics_test_data/cpics/data_test/CPICSM160/cpics",roisModel)
    c.generateProject("/home/sgalvagno/cpicsEcotaxa")
