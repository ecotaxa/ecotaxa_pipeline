
import pandas as pd

from Pipeline.task import Task

class merge_files(Task):

    _need_keys = ['tsv_pulse', 'tsv_listmode']
    _update_keys = ['tsv_list']

    def run(self):
        df_pulse = self._data['tsv_pulse']['dataframe']
        df_listmode = self._data['tsv_listmode']['dataframe']

        df : pd.DataFrame = pd.merge(df_pulse, df_listmode, how="inner", on=["object_id"])


        if not 'tsv_list' in self._data:  self._data['tsv_list'] = {}
        if not 'df_result' in self._data:  self._data['tsv_list']['df_result'] = {}
        self._data['tsv_list']['df_result']['dataframe'] = df
