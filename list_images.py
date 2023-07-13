

import glob
import os
from pathlib import PurePath
from build_file_name import build_file_name
from debug_tools import dump
from task import Task
import pandas as pd

class list_images(Task):
    """
    list all the image found in the 'images' folder
    """
    _need_keys = ['raw_folder', 'sample_name', 'images_folder']
    _create_keys = ['image_list']
    _update_keys = ['dataframe']

    def __init__(self, **kwargs):
        if 'pattern_name' in kwargs:
            self.image_name_pattern = kwargs['pattern_name']
        else:
            raise Exception("Argument missing 'pattern_name'")
        
    def filter(self,filename) -> bool:
        
        

        return True
    
    def make_key_from_image_name(self, filename:str) -> str:
        filename_less_extension = os.path.splitext(filename)[0]
        key = filename_less_extension.replace('_Cropped','')
        return key
    
    def img_rank(self):
        if not 'img_rank' in self._data: self._data['img_rank'] = 0
        self._data['img_rank'] = self._data['img_rank'] + 1

    def run(self):
        self.img_rank()

        image_list = {}
        image_path = self._data['images_folder']
        image_file_list = self.list_files(image_path, self.image_name_pattern)

        for image in image_file_list:
            # image_data={}
            filename=PurePath(image).name
            
            # key=os.path.splitext(filename)[0]  # Bad key 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_Cropped_4206' must be 'R4_photos_flr16_2uls_10min 2022-09-14 12h28_4206'
            key = self.make_key_from_image_name(filename)    

            # image_data["key"]= key
            # image_data["filename"]= str(filename)
            # image_data["path"]= PurePath(image)

            image_data = {
                'object_id': key,
                'img_file_name': str(filename),
                'img_rank': self._data['img_rank'],
                'path': PurePath(image)
            }

            image_list[key]= image_data

        # dump(image_file_list)
        self._data['image_list']=image_list

        df = pd.DataFrame.from_dict(image_list, orient='index')
        # result_path = "tests/cytosense/result/"
        
        # self.result_image_path = PurePath(result_path,"_images_.csv")
        # df.to_csv(PurePath(self.result_image_path), index=False)

        if not 'dataframe' in self._data:
            self._data['dataframe'] = {}
        self._data['dataframe']['images'] = df

    def list_files(self, from_path:PurePath, pattern=[]) -> list:
        path_pattern = "*"
        if len(pattern) != 0:
            ut = build_file_name(pattern)
            path_pattern = ut.get_name(eSampleName=self._data['sample_name'], eIndex="*")
        dir_path = PurePath(from_path, path_pattern)
        dump(dir_path)
        file_list = glob.glob(str(dir_path))
        return file_list
