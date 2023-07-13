from enum import Enum

class Instrument(str, Enum):
    ZOOSCAN = "ZooScan"
    CPICS = "CPICS"
    CYTOSENSE = "CytoSense"

