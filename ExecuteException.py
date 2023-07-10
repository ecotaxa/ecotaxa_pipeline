
class ExecuteException(Exception):
    def __init__(self, className, functionName):
        self.className = className
        self.functionName = functionName
        
    def message(self) -> str:
        return "Class `{}` does not implement `{}`".format(self.className, self.functionName)
