from pathlib import PurePath
import unittest
import pandas as pd

from ecotaxaDataframe import ecotaxaDataframe


class Test_ecotaxaDataframe(unittest.TestCase):

    # fail because pd.DataFrame() return None
    # def test_create_ecotaxaDataframe(self):

    #     ut = ecotaxaDataframe()

    #     self.assertIsInstance(ut.header,pd.DataFrame)
    #     self.assertIsInstance(ut.data,pd.DataFrame)
        
    def test_load_ecotaxa_csv(self):
        folder = "tests/misc/"
        result_folder = "tests/cytosense/result/misc"
        filename = "images.tsv"

        headers=['img_file_name','object_id']
        types=["[t]","[t]"]
        data={
            0:["20110911_06_a_1_937.jpg", "id_1"],
            1:["20110911_06_a_1_938.jpg", "id_2"],
            2:["20110911_06_a_1_939.jpg", "id_3"],
        }

        mockfdf_header = pd.DataFrame(columns=headers)
        last_index = len(mockfdf_header)
        mockfdf_header.loc[last_index]=types

        mockfdf_data = pd.DataFrame(columns=headers)
        for index in data:
            last_index = len(mockfdf_data)
            mockfdf_data.loc[last_index]=data[index]
        
        df = pd.concat([mockfdf_header, mockfdf_data], ignore_index=True, sort=False)

        path = PurePath(result_folder, "mock_"+filename)
        df.to_csv(path,index=False,sep="\t")


        path = PurePath(folder, filename)
        ut = ecotaxaDataframe(path)
        # ut.save_cvs(PurePath(result_folder,filename),index=False)
        path = PurePath(result_folder,filename)
        ut.to_tsv(path)


        from pandas.testing import assert_frame_equal        
        assert_frame_equal(ut.header, mockfdf_header,obj="headers")
        assert_frame_equal(ut.data, mockfdf_data,obj="data")


    def test_merge(self):

        folder = "tests/misc/"
        result_folder = "tests/cytosense/result/misc"

        filename1 = "ecotaxa_tsv.tsv"
        filename2 = "images.tsv"

        mock_filename = "mock_" + filename1
        mock_path = PurePath(folder, mock_filename)
        mock = ecotaxaDataframe(mock_path)

        path1 = PurePath(folder, filename1)
        ecodf = ecotaxaDataframe(path1)
        path2 = PurePath(folder, filename2)
        ut = ecotaxaDataframe(path2)

        ut.merge_with(ecodf)

        path = PurePath(result_folder, "merge_" + filename1)
        ut.to_tsv(path)

        from pandas.testing import assert_frame_equal        
        assert_frame_equal(ut.header, mock.header,obj="headers")
        assert_frame_equal(ut.data, mock.data,obj="data")