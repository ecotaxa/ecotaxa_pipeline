
from Pipeline.Exception.ExecuteException import ExecuteException
# from Template import Template


class MappingException(Exception):
    executeException: ExecuteException = None
    className = ""
    functionName = ""
    # line : tuple(str, list[str]) = (None, [])
    line = None
    # model : Template = None
    # model :  = None
    result : dict = None

    def __init__(self, **kwargs: object) -> None:
        if 'executeException' in kwargs:
            self.executeException = kwargs['executeException']
            self.className = self.executeException.className
            self.functionName = self.executeException.functionName
        # if 'line' in kwargs:
        #     self.line = kwargs['line']
        if 'model' in kwargs:
            self.model = kwargs['model']   
        if 'result' in kwargs:
            self.result = kwargs['result'] 
    
    def message(self) -> str:
        return "Mapping issue in model {}: Function `{}` called in mapping of `{}` is not implemented".format(self.model.name, self.functionNamefn, self.line[0])

