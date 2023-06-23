
from task import Task


class Pipeline():

    _tasks = [] # list(Task) 
    _data = {}

    def __init__(self, tasks):
        self._tasks = tasks
    

    def run(self, data):
        self._data = data
        for task in self._tasks:
            # if isinstance(task, Task) :
            #     # raise "Not instatiate"
            #     task = task.__init__()

            print("running task: " + task.__class__.__name__)

            self._data = task.run(self._data)
            pass

