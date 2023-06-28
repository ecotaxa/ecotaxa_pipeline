
class Task():

    _need_keys = []
    _update_keys = []
    _create_keys = []
    _delete_keys = []

    _data = {}
    name : str = None

    # def __init__(self) #, name: str):
        # self.name = name

    def run(self, data):
        self._data = data
        return self._data

    def test_need_keys(self, data):
        self._data = data
        try:
            for key in self._need_keys:
                _ = self._data[key]
                # self._data[key] = data[key]
        except:
            raise Exception("Missing key: " + key + " in data argument")

    def remove_keys(self):
        for key in self._delete_keys:
            self._data[key] = None

