

class MissingArgumentException(Exception):

    def __init__(self, argument_name):
        self.argument = argument_name
        self.message = 'You need "' + self.argument + '" argument'
        super().__init__(self.message)

        