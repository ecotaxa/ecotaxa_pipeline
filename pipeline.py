


class Pipeline():

    _tasks = [] 
    _data = {}

    def __init__(self, tasks):
        self._tasks = tasks
    

    def run(self):
        for task in self._tasks:
            self._data = task().run(self._data)



