
from pathlib import PurePath
from task import Task


class define_sample_pipeline_folder(Task):

    _need_keys = ['pipeline_folder', 'sample_name']
    # _update_keys = []
    _create_keys = ['raw_folder', 'work_folder', 'images_folder']

    def _run(self, data):
        if  type(data['pipeline_folder']) == str:
            data['pipeline_folder'] = PurePath(data['pipeline_folder'])
            self._data = super()._run(data)
            return self._data

    def run(self):
    #     if  type(data['pipeline_folder']) == str:
    #         data['pipeline_folder'] = PurePath(data['pipeline_folder'])


    #     self.test_need_keys(data)
    #     # try:
    #     #     self._data['pipeline_folder'] = data['pipeline_folder']
    #     #     self._data['sample_name'] = data['sample_name']
    #     # except:
    #     #     raise Exception( "Missing key")
        

    #     self._define_keys()
    #     return self._data

    # def _define_keys(self):
        # self._data['raw_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_raw")
        # self._data['work_folder'] = PurePath(self._data['pipeline_folder'], self._data['sample_name'], "_work")
        # self._data['images_folder'] = PurePath(self._data['raw_folder'], str(self._data['sample_name'] + "_Images"))
        self._data['raw_folder'] = PurePath(self._data['pipeline_folder'])
        self._data['work_folder'] = PurePath(self._data['pipeline_folder'], "_work" ,self._data['sample_name'])
        self._data['images_folder'] = PurePath(self._data['raw_folder'], str(self._data['sample_name'] + "_Images"))
