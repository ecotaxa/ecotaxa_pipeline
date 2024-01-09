
class Task():

    _need_keys = []
    _update_keys = []
    _create_keys = []
    _delete_keys = []

    _data = {}
    name : str = None

    # def __init__(self) #, name: str):
        # self.name = name

    def run(self):
        pass


    # TODO need this function only for test -> need to do a class an inherit from twice
    # TO TEST  put code below in test class
    # # to use in pipeline 
    # # we cannot be use in a single task, but in that case not need to test input keys
    # # TODO need to use decorator or descriptor
    def _run(self, data):
        self._data = data
        self.test_need_keys(data)
        # self._data = 
        self.run()
        self.remove_keys()
        return self._data

    def test_need_keys(self, data):
        try:
            for key in self._need_keys:
                _ = self._data[key]
                # self._data[key] = data[key]
        except:
            raise Exception("Missing key: " + key + " in data argument")

    def remove_keys(self):
        for key in self._delete_keys:
            self._data[key] = None

