from pathlib import PurePath
from Pipeline.task import Task
import Tools.tools as tools
import pandas as pd


class generate_tsv(Task):

    _need_keys = ['tsv_list','work_folder','sample_name'] # ['tsv_list|df_result|dataframe']

    def run(self):
        
        df_result: pd.DataFrame = self._data['tsv_list']['df_result']['dataframe']
        work_path = PurePath(self._data['work_folder'])
        filename = self._data['sample_name'] + ".tsv"
        
        tools.create_folder(work_path)
        
        path = PurePath(work_path, filename )
        df_result.to_csv(path, index=False,sep="\t")

