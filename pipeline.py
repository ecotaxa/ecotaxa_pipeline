


class Task():

    _data = {}
    naem : str

    def __init__(self, name: str, data):
        self.name = name
        self._data = data

    def run(self):
        return self._data


class Pipeline():

    _tasks = [] 
    _data = {}

    def __init__(self, tasks):
        self._tasks = tasks
    

    def run(self):
        for task in self._tasks:
            self._data = task(self._data).run()



