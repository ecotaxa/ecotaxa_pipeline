
from debug_tools import dump, dump_structure
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
                # self._data = task._run(self._data)
                # self._data = self._run(task, self._data)
                self._run(task)
            
    # to use in pipeline 
    # TODO need to use decorator or descriptor
    def _run(self, task):
        self.test_need_keys(task)
        task._data = self._data
        task.run()
        self._data = task._data
        self.remove_keys(task)
        return self._data


    # def test_need_keys(self, data):
    def test_need_keys(self, task):
        try:
            for key in task._need_keys:
                _ = self._data[key]
                # self._data[key] = data[key]
        except:
            raise Exception("Missing key: " + key + " in data argument")

    def remove_keys(self, task):
        # for key in self._delete_keys:
        for key in task._delete_keys:
            self._data[key] = None


    # functions to debug pipeline

    def verify(self):
        self._verify_tasks(self._tasks)

    def _verify_tasks(self, tasks):
        for task in tasks:
            if type(task) == list:
                self._verify_tasks(task)
            else:
                print("running task: " + task.__class__.__name__)
                # self._data = task._run(self._data)
                # self._data = self._run(task, self._data)
                self._verify(task)

    def _verify(self, task:Task):
        # dump(task._need_keys)
        # dump(task._update_keys)
        # dump(task._create_keys)
        # dump(task._delete_keys)

        print("\t_need_keys: [" + ", ".join(task._need_keys) + "]")
        print("\t_create_keys: [" + ", ".join(task._create_keys) + "]")
        print("\t_update_keys: [" + ", ".join(task._update_keys) + "]")
        print("\t_delete_keys: [" + ", ".join(task._delete_keys) + "]")

        # self.test_need_keys(task)
        # self.remove_keys(task)
        return self._data

# run the tasks
    def show_data(self, data):
        self._data = data
        self.print_data(data)
        self._show_data_tasks(self._tasks)
        return self._data

    # recursive function to execute the task pipeline
    def _show_data_tasks(self, tasks):
        for task in tasks:

            if type(task) == list:
                self._show_data_tasks(task)
            else:
                print("running task: " + task.__class__.__name__)
                # self._data = task._run(self._data)
                # self._data = self._run(task, self._data)
                self._run(task)
                self.print_data(self._data)
    
    def print_data(self, data):
        dump_structure(data)
