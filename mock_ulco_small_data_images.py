

import glob
from pathlib import PurePath

from debug_tools import dump

import pandas as pd

from mock_polynomial_pulses_ulco_small_data import mock_ulco_dataframe

class mock_ulco_small_data_images():

    mock_path = "tests/cytosense/ULCO/mock_small_data"
    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    image_path = sample_name + "_Images"
    sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
    image_folder = sample_name + "_Images"
    list_image_indexes = [29,3269,3543,4206,10104]

    img_rank = 1

    def __init__(self,img_rank = 1) -> None:
    # def __init__(self,img_rank = 1) -> None:
        # self.img_rank = img_rank

        self.list_image_names = [self.sample_name+"_"+str(index)+".jpg" for index in self.list_image_indexes]

        self.image_list = {}
        for index in self.list_image_indexes:
            filename = self.sample_name+"_Cropped"+"_"+str(index)+".jpg"
            key = self.sample_name+"_"+str(index)

            # filename = key+".jpg"
            image_dict = {
                'object_id': key,
                'img_file_name': filename,
                'img_rank': self.img_rank,
                'path': PurePath(self.mock_path, self.image_path, filename)
            }

            self.image_list[key] = image_dict
        
        self.result_image_path = self.save_df()


    def save_df(self):
        self.df = pd.DataFrame.from_dict(self.image_list, orient='index')
        image_result_filename = self.image_folder + "__mock_" + self.__class__.__name__ + ".csv"
        result_path = "tests/cytosense/result/"
        result_image_path = PurePath(result_path,image_result_filename)
        self.df.to_csv(PurePath(result_image_path), index=False)
        return result_image_path

    def list_files(self, from_path:PurePath, pattern="*") -> list:
        dir_path = PurePath(from_path, pattern)
        file_list = glob.glob(str(dir_path))
        return file_list



class mock_trunc:
    local_path = "tests/cytosense/ULCO/mock_small_data"
    mock_path = "tests/cytosense/ULCO/DataFrame"
    result_folder = "tests/cytosense/result/"

    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    # csv_filename = sample_name + "__mock_merge_trunc.csv"
    csv_filename = sample_name + "__mock_trunc.csv"
    # csv_filename = sample_name + "__mock_" + self.__class__.__name__ + ".csv"

    # pulse_filename = sample_name + "__pulses__" + ".csv"
    # listmode_filename = sample_name + "__listmode__" + ".csv"
    # result_filename = sample_name + "__merge_p_l__" + ".csv"
    
    # pulse_path = PurePath(mock_path , pulse_filename)
    # listmode_path = PurePath(mock_path , listmode_filename)
    # result_path = PurePath(mock_path, result_filename)

    def __init__(self):

        mock_merge = mock_ulco_dataframe()
        mock_images = mock_ulco_small_data_images()
        # df_merge = pd.read_csv(mock_merge.csv_path)
        # df_images = pd.read_csv(mock_images.result_image_path)
        df_merge = mock_merge.df
        df_images = mock_images.df

        self.df = self.merge(df_merge, df_images)

        # result_path = "tests/cytosense/result/"
        # self.result_mock_merge_trunc_path = PurePath(result_path, mock_merge_trunc)
        # self.dfmock.to_csv(PurePath(self.result_mock_merge_trunc_path), index=False)

        self.csv_path = self.save_csv(self.csv_filename, self.df)

        self.data = self.build_data(df_merge, df_images)


    def merge(self, df_merge, df_images) -> pd.DataFrame:
        dfmock = pd.merge(df_merge, df_images, how="inner", on=['object_id'])
        # dfmock = pd.merge(df_merge, df_images, how="inner", left_on=['object_id'], right_on=['key'])
        # dfmock = pd.merge(df_merge, df_images, how="inner", left_on=['object_id'], right_on=['object_id'])
        # del dfmock["key"]
        del dfmock["path"]
        return dfmock

    def save_csv(self,filename,df) -> PurePath:
        path = PurePath(self.result_folder, filename)
        # path = PurePath(self.result_mock_merge_trunc_path)
        self.df.to_csv(path, index=False)
        return path


    def build_data(self, df_merge, df_images) -> dict:

        data = {
            'raw_folder': PurePath(self.local_path),
            'sample_name': self.sample_name,
            'dataframe':{
                'images': df_images
            },
            'tsv_list':{
                'df_result':{
                    'dataframe': df_merge
                }
            }
        }

        return data



class mock_trunc_data_farom_cvs_file:
    local_path = "tests/cytosense/ULCO/mock_small_data"
    mock_path = "tests/cytosense/ULCO/DataFrame"
    result_folder = "tests/cytosense/result/"

    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    # csv_filename = sample_name + "__mock_merge_trunc.csv"
    csv_filename = sample_name + "__mock_trunc.csv"
    # csv_filename = sample_name + "__mock_" + self.__class__.__name__ + ".csv"

    # pulse_filename = sample_name + "__pulses__" + ".csv"
    # listmode_filename = sample_name + "__listmode__" + ".csv"
    # result_filename = sample_name + "__merge_p_l__" + ".csv"
    
    # pulse_path = PurePath(mock_path , pulse_filename)
    # listmode_path = PurePath(mock_path , listmode_filename)
    # result_path = PurePath(mock_path, result_filename)

    def __init__(self):

        mock_merge = mock_ulco_dataframe()
        mock_images = mock_ulco_small_data_images()
        df_merge = pd.read_csv(mock_merge.csv_path)
        df_images = pd.read_csv(mock_images.result_image_path)

        self.df = self.merge(df_merge, df_images)

        # result_path = "tests/cytosense/result/"
        # self.result_mock_merge_trunc_path = PurePath(result_path, mock_merge_trunc)
        # self.dfmock.to_csv(PurePath(self.result_mock_merge_trunc_path), index=False)

        self.csv_path = self.save_csv(self.csv_filename, self.df)

        self.data = self.build_data(df_merge, df_images)


    def merge(self, df_merge, df_images) -> pd.DataFrame:
        dfmock = pd.merge(df_merge, df_images, how="inner", on=['object_id'])
        # dfmock = pd.merge(df_merge, df_images, how="inner", left_on=['object_id'], right_on=['key'])
        # dfmock = pd.merge(df_merge, df_images, how="inner", left_on=['object_id'], right_on=['object_id'])
        # del dfmock["key"]
        del dfmock["path"]
        return dfmock

    def save_csv(self,filename,df) -> PurePath:
        path = PurePath(self.result_folder, filename)
        # path = PurePath(self.result_mock_merge_trunc_path)
        self.df.to_csv(path, index=False)
        return path


    def build_data(self, df_merge, df_images) -> dict:

        data = {
            'raw_folder': PurePath(self.local_path),
            'sample_name': self.sample_name,
            'dataframe':{
                'images': df_images
            },
            'tsv_list':{
                'df_result':{
                    'dataframe': df_merge
                }
            }
        }

        return data


def generate_data():
     m = mock_ulco_small_data_images()
     m.save_df()

def test():
        mock = mock_ulco_small_data_images()

        path = PurePath(mock.mock_path, mock.image_path)
        strpath = str(path)
        dump(strpath)

        l = mock.list_files(strpath)
        dump(l,name=True)


if __name__ == '__main__':
    generate_data()
    test()
