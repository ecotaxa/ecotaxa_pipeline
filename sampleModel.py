

from Parser.Template import Template

class sampleModel(Template):

    _mapping = {
        'sample_id':{ 'file' : None , 'header' :'Sample Name', 'index' : 1 , 'fn' : None , 'type' : '[t]', 'comment': 'Sample Name'},
        'sample_field1':{ 'file' : None , 'header' :'Sample Field', 'index' : 2 , 'fn' : None , 'type' : '[t]', 'comment': 'Sample field'},
    }

class processModel(Template):

    _mapping = {
        'sample_id':{ 'file' : None , 'header' :'Sample Name', 'index' : 1 , 'fn' : None , 'type' : '[t]', 'comment': 'Sample Name'},
        'sample_field1':{ 'file' : None , 'header' :'Sample Field', 'index' : 2 , 'fn' : None , 'type' : '[t]', 'comment': 'Sample field'},
    }

