

from task import Task
import pandas as pd

class trunc_data(Task):
    """
    trunc the listmode and pulses data from image list
    if image don't exist we don't need the data. Ecotaxa need an image.
    """
    _need_keys = ['dataframe','tsv_list'] # ['dataframe|images', 'tsv_list|df_result|dataframe']
    _update_keys = ['tsv_list|df_result|dataframe']

    def run(self):
        df_images = self._data['dataframe']['images']
        df_result = self._data['tsv_list']['df_result']['dataframe']

        # df = pd.merge(df_result, df_images, how="inner", left_on=['object_id'], right_on=['key'])
        df = pd.merge(df_result, df_images, how="inner", on=['object_id'])
        # del df["key"]
        del df["path"]

        self._data['tsv_list']['df_result']['dataframe'] = df

