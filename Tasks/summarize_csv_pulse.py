from pathlib import PurePath
from Pipeline.task import Task
from Localization.csv_configuration import french_csv_configuration

class summarize_csv_pulse(Task):

    _need_keys = ['raw_folder', 'csv_pulse', 'sample_name']
    _update_keys = ['csv_pulse']


    import Cytosense.summarise_pulses as summarise_pulses
    save_dataframe_to_csv = summarise_pulses.save_dataframe_to_csv
    summarise_pulses_function = summarise_pulses.summarise_pulses

    # def __init__(self, summarise_pulses_function = summarise_pulses.summarise_pulses):
    #     # import summarise_pulses
    #     # self.summarise_pulses_function = summarise_pulses_function if summarise_pulses_function else summarise_pulses.summarise_pulses
    #     self.summarise_pulses_function = summarise_pulses_function

    _filename = lambda self: str(self._data['sample_name'] + "_Polynomial_Pulses" + ".csv")

    def build_name(self):
        return PurePath( self._data['raw_folder'], self._filename() )

    def run(self):
        #     self.test_need_keys(data)
        #     self.process()
        #     self.remove_keys()
        #     return self._data

        # def process(self):
        import Cytosense.summarise_pulses as summarise_pulses

        pulses_filename = self._data['csv_pulse']['path']
        # poly_dataframe = self.summarise_pulses_function(pulses_filename)
        poly_dataframe = summarise_pulses.summarise_pulses(pulses_filename, csv_configuration=self._data['csv_pulse']['csv_configuration'])
        poly_filename = self.build_name()
        self._data['csv_pulse']['filename'] = self._filename()
        # self.save_dataframe_to_csv(poly_dataframe, poly_filename)
        summarise_pulses.save_dataframe_to_csv(poly_dataframe, poly_filename, csv_configuration=french_csv_configuration)
        self._data['csv_pulse']['path'] = poly_filename
