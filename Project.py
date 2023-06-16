# Sebastien Galvagno 06/2023
import os
from tools import create_folder


class Project:
    def __init__(self,message_project_creation):
        self.raw_data_path = message_project_creation["raw_data_path"]
        self.project_path = os.path.join(message_project_creation["dest_data_path"], message_project_creation["title"])
        self.model = message_project_creation["model"]
        self.title = message_project_creation["title"]
        self.instrument = message_project_creation["instrument"]
        # create _raw in destination project path and copy the entire raw folder from raw_data_path
        self.generate_project_architecture()

    def generate_project_architecture(self) :
        create_folder(self.project_path) 
        create_folder(os.path.join(self.project_path, "_raw"))
        create_folder(os.path.join(self.project_path, "_work"))


