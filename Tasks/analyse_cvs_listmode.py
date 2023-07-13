
from Parser.Template import Template
from Tasks.analyze_csv_pulse import analyse_csv_cytosense_file


class analyse_cvs_listmode(analyse_csv_cytosense_file):
    import pandas as pd

    _need_keys = [ 'csv_listmode']
    _update_keys = ['tsv_list']
    _model = Template

    _df: pd.DataFrame

    def run(self):
        self._fileType = 'csv_listmode'
        self._analysing = self._data[self._fileType]
        self._model = self._analysing['mapping']
        self._df = self._init_df()
        self._add_type() # add type line after processing the data

        self.map_csv_to_df()


        self._data['tsv_listmode']={}
        self._data['tsv_listmode']['dataframe']= self._df

        # self.df.to_csv("tests/cytosense/result/test_analyze_csv_pulse.csv")
        self._df.to_csv("tests/test_analyze_csv_listmode.csv")
