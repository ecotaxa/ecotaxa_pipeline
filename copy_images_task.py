

from task import Task
import pandas as pd

class copy_images_task(Task):

    _need_keys = ['raw_folder', 'sample_name', 'work_folder', 'images_folder', 'image_list']
    
    def run(self):

        images: pd.DataFrame = self._data['image_list']
        destination_folder = self._data['work_folder']
        image_folder = self._data['images_folder']

        # df = images.pivot_table(columns='img_file_name')
        # df = images.pivot(columns='img_file_name')
        

        for image in images:
            # path = PurePath(image_folder , images)
            print(f"copy image {image}")
            # print(f"copy image {image['path']}")
        
    

    