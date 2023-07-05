

import glob
from pathlib import PurePath

from debug_tools import dump


class mock_ulco_small_data_images():

    mock_path = "tests/cytosense/ULCO/mock_small_data"
    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    image_path = sample_name + "_Images"

    list_image_indexes = [29,3269,3543,4206,10104]

    def __init__(self) -> None:
        self.list_image_names = [self.sample_name+"_"+str(index)+".jpg" for index in self.list_image_indexes]


        self.image_list = {}

        for index in self.list_image_indexes:
            filename = self.sample_name+"_Cropped"+"_"+str(index)+".jpg"
            key = self.sample_name+"_"+str(index)

            # filename = key+".jpg"
            image_dict = {
                'key': key,
                'filename': filename,
                'path': PurePath(self.mock_path, self.image_path, filename)
            }

            self.image_list[key] = image_dict

            
    def list_files(self, from_path:PurePath, pattern="*") -> list:
        dir_path = PurePath(from_path, pattern)
        file_list = glob.glob(str(dir_path))
        return file_list



def test():
        mock = mock_ulco_small_data_images()

        # print("image_path: ", mock.image_path)
        # print("list_image_names: ", mock.list_image_names)
        # print("images_list: ", mock.image_list)

        path = PurePath(mock.mock_path, mock.image_path)
        strpath = str(path)

        print(strpath)

        l = mock.list_files(strpath)
        # print(l)
        dump(l,name=True)


if __name__ == '__main__':
    test()
