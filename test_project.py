
# from ... import  Project

# import sys
# sys.path.insert(0, '..')

# import sys
# from pathlib import Path
# sys.path.append(str(Path('.').absolute().parent))

# import os
# import sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

# from ...project import Project



# if __name__ == "__main__":
#     p = Project()
#     print("Everything passed")

# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import Project
# import os
# import shutil
# import sys
# from os.path import join, dirname, realpath
# from pathlib import Path

# import pytest
import os
from pathlib import Path

import unittest
from unittest import mock

# from unittest.mock import patch
# from unittest.mock import MagicMock
# from unittest.mock as mock


# # Import services under test as a library
# sys.path.extend([join("", "..", "..", "py")])

# HERE = Path(dirname(realpath(__file__)))

# target = __import__("Project.py")

# from pipeline.project import Project
from project import Project
# from tools import create_folder
import tools

from tools import create_folder

class TestProject(unittest.TestCase):

    project = {
            'name':'name',
            'path':'path',
            'work_data_folder':'work_data_folder',
            'pipeline':'pipeline',
            'metadata':{},
    }

    def test_creation_fail_no_argument(self):
        self.assertRaises(Exception, Project)
    
    def test_creation_fail_missing_argument(self):
        project = {
            'name':'name',
        }
        self.assertRaises(Exception, Project, project)

    def test_creation(self):
        p = Project(self.project)

        # strange os.path don't exist
        # assert(p.raw_data_folder == os.path.join(self.project.path, "_raw").name )
        # assert(p.work_data_folder == os.path.join(self.project.path, "_work").name )

        self.assertEquals(p.raw_data_folder, "path/_raw")
        self.assertEquals(p.work_data_folder, "path/_work")



    # @patch('tools.create_folder')
    # @mock.patch('tools.create_folder')
    @mock.patch('create_folder')
    # @unittest. .mock.patch('tools.create_folder')
    def test_create_folder(self, create_folder_mock):
        create_folder_mock.return_value = 'path'

        # tools.create_folder('otot')
        create_folder('toto')

        # self._folder = []
        utp = Project(self.project)
        utp.generate_project_architecture()
        self.assertTrue(create_folder_mock.called)
        create_folder_mock.assert_called()
        create_folder_mock.assert_called_with("path")
        print(self._folder)
        # self.assertIn("path", )
        # assert( "path" in create_folder.folder)
        # assert(len(create_folder.folder) == 3)


if __name__ == '__main__':
    unittest.main()


    # # @patch('tools.create_folder')
    # def create_folder(path:Path):
    #     raise("you call me")
    #     create_folder.folder.append(path.name)
    # create_folder.folder = []

