


from Project import Project
from enums import Instrument


class CytoSense(Project):

    def __init__(self, raw_data_path, data_to_export_base_path, cytoSense_model, title):
        super().__init__(raw_data_path, data_to_export_base_path, cytoSense_model, title, Instrument.CYTOSENSE)
        

    def copy_raw_data(self):
        #TODO
        pass

        def define_id(self, data):
            return self.folder['destFolder'] + data
        
    