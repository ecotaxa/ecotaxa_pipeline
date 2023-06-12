# Sebastien Galvagno  06/2023


# from tools import printDict
from Template import Template


class CTD_sbe37(Template):
        
    #ROI, Date Time,Name,Position upper leftx,Position upper lefty,Position lower rightx,Position lower rightY,Temperature,Conductivity,Pressure,Depth,Salinity,Sound Velocity,local density
    _mapping = {
        'object_temperature':{ 'file' : "ROI" , 'header' :'Temperature', 'index' : 7 , 'fn' : None , 'type' : '[f]', 'comment': 'Temperature'},
        'object_conductivity':{ 'file' : "ROI" , 'header' :'Conductivity', 'index' : 8 , 'fn' : None , 'type' : '[f]', 'comment': 'Conductivity'},
        'object_pressure':{ 'file' : "ROI" , 'header' :'Pressure', 'index' : 9 , 'fn' : None , 'type' : '[f]', 'comment': 'Pressure'},
        'object_depth':{ 'file' : "ROI" , 'header' :'Depth', 'index' : 10 , 'fn' : None , 'type' : '[f]', 'comment': 'Depth'},
        'object_salinity':{ 'file' : "ROI" , 'header' :'Salinity', 'index' : 11 , 'fn' : None , 'type' : '[f]', 'comment': 'Salinity'},
        'object_sound_velocity':{ 'file' : "ROI" , 'header' :'Sound_Velocity', 'index' : 12 , 'fn' : None , 'type' : '[f]', 'comment': 'Sound Velocity'},
        'object_local_density':{ 'file' : "ROI" , 'header' :'local_density', 'index' : 13 , 'fn' : None, 'type' : '[f]', 'comment': 'local density'}
    }


class cpicsModel(Template):


    #ROI, Date Time,Name,Position upper leftx,Position upper lefty,Position lower rightx,Position lower rightY,Temperature,Conductivity,Pressure,Depth,Salinity,Sound Velocity,local density
    _mapping = {
        'object_date':{ 'file' : "ROI" , 'header' :'Date', 'index' : 1 , 'fn' : "date" , 'type' : '[t]', 'comment': 'Date'},
        'object_time':{ 'file' : "ROI" , 'header' :'Time', 'index' : 1 , 'fn' : "time" , 'type' : '[t]', 'comment': 'Time'},       
        'img_file_name':{ 'file' : "ROI" , 'header' :'Name', 'index' : 2 , 'fn' : None , 'type' : '[t]', 'comment': 'img_file_name'},# Name  -> img_file_name    &	object_id
        'object_id':{ 'file' : "ROI" , 'header' :'Name', 'index' : 2 , 'fn' : "id" , 'type' : '[t]', 'comment': 'object_id'},
        'object_leftx':{ 'file' : "ROI" , 'header' :'leftx', 'index' : 3 , 'fn' : None , 'type' : '[f]', 'comment': 'Position upper leftx'},
        'object_lefty':{ 'file' : "ROI" , 'header' :'lefty', 'index' : 4 , 'fn' : None , 'type' : '[f]', 'comment': 'Position upper lefty'},
        'object_rightx':{ 'file' : "ROI" , 'header' :'rightx', 'index' : 5 , 'fn' : None , 'type' : '[f]', 'comment': 'Position lower rightx'},
        'object_righty':{ 'file' : "ROI" , 'header' :'righty', 'index' : 6 , 'fn' : None , 'type' : '[f]', 'comment': 'Position lower rightY'}
    }
    
    def __init__(self, ctd: Template=""):
        map = ctd.mapping
        # printDict(map,"MAP")
        self.append(map)
        super().__init__()


    
