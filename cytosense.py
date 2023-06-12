

from Project import Project
from enums import Instrument


class SytoSence(Project):

    def __init__(self, path, roisModel):
        super().__init__(path,roisModel, Instrument.CYTOSENSE)


        