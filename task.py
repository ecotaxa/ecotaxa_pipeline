
class Task():

    _need_keys = []
    _update_keys = []
    _create_keys = []

    _data = {}
    name : str = "Task"

    # def __init__(self) #, name: str):
        # self.name = name

    def run(self, data):
        self._data = data
        return self._data

    def test_need_keys(self, data):
        try:
            for key in self._need_keys:
                # _ = self._data[key]
                self._data[key] = data[key]
        except:
            raise("Missing key: " + key + " in data argument")



