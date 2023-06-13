# Sebastien Galvagno 06/2023
import os
from tools import create_folder


class Project:
    def __init__(self, raw_data_path, data_to_export_base_path, model, title, instrument):
        self.raw_data_path = raw_data_path
        self.project_path = os.path.join(data_to_export_base_path, title)
        self.model = model
        self.title = title
        self.instrument = instrument
        # create _raw in destination project path and copy the entire raw folder from raw_data_path
        self.generate_project_architecture()

    def generate_project_architecture(self) :
        create_folder(self.project_path) 
        create_folder(os.path.join(self.project_path, "_raw"))
        create_folder(os.path.join(self.project_path, "_work"))


