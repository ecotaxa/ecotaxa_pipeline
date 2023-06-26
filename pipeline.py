
from task import Task


class Pipeline():
    '''
        task pipeline grammar : tasks = [ Task | [ Task ] ]
    '''

    _tasks = [] # list(Task) 
    _data = {}

    def __init__(self, tasks):
        self._tasks = tasks
    

    # run the tasks
    def run(self, data):
        self._data = data
        self._run_tasks(self._tasks)
        return self._data

    # recursive function to execute the task pipeline
    def _run_tasks(self, tasks):
        for task in tasks:

            if type(task) == list:
                self._run_tasks(task)
            else:
                print("running task: " + task.__class__.__name__)
                self._data = task.run(self._data)
            
    