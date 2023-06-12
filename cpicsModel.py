# Sebastien Galvagno 


class cpicsModel:

    model = { 'ROI':0,
              'Date':1, # Date
              'Time':1, # Time
              'Name':2, # Name  -> img_file_name    &	object_id
              'leftx':3,  # Position upper leftx
              'lefty':4,  # Position upper lefty,
              'rightx':5,  # Position lower rightx,
              'righty':6,  # Position lower rightY,
            }

    mapping = {
        'object_date':{ 'file' : "ROI" , 'header' :'Date', 'index' : 1 , 'fn' : "date" , 'type' : '[t]'},
        'object_time':{ 'file' : "ROI" , 'header' :'Time', 'index' : 1 , 'fn' : "time" , 'type' : '[t]'},       
        'img_file_name':{ 'file' : "ROI" , 'header' :'Name', 'index' : 2 , 'fn' : None , 'type' : '[t]'},
        'object_id':{ 'file' : "ROI" , 'header' :'Name', 'index' : 2 , 'fn' : "id" , 'type' : '[t]'},
        'object_leftx':{ 'file' : "ROI" , 'header' :'leftx', 'index' : 3 , 'fn' : None , 'type' : '[f]'},
        'object_lefty':{ 'file' : "ROI" , 'header' :'lefty', 'index' : 4 , 'fn' : None , 'type' : '[f]'},
        'object_rightx':{ 'file' : "ROI" , 'header' :'rightx', 'index' : 5 , 'fn' : None , 'type' : '[f]'},
        'object_righty':{ 'file' : "ROI" , 'header' :'righty', 'index' : 6 , 'fn' : None , 'type' : '[f]'}
     }
    
    def __init__(self, ctd=""):
        self.ctd = ctd

    def addCtd(self):
        ctd = { 'Temperature':7,  # Temperature,
              'Conductivity':8,  # Conductivity,
              'Pressure':9, # Pressure,
              'Depth':10, # Depth,
              'Salinity':11, # Salinity,
              'Sound_Velocity':12, # Sound Velocity,
              'local_density':13, # local density
             }
        
        ctdMapping = {
            'object_temperature':{ 'file' : "ROI" , 'header' :'Temperature', 'index' : 7 , 'fn' : None , 'type' : '[f]'},
            'object_conductivity':{ 'file' : "ROI" , 'header' :'Conductivity', 'index' : 8 , 'fn' : None , 'type' : '[f]'},
            'object_pressure':{ 'file' : "ROI" , 'header' :'Pressure', 'index' : 9 , 'fn' : None , 'type' : '[f]'},
            'object_depth':{ 'file' : "ROI" , 'header' :'Depth', 'index' : 10 , 'fn' : None , 'type' : '[f]'},
            'object_salinity':{ 'file' : "ROI" , 'header' :'Salinity', 'index' : 11 , 'fn' : None , 'type' : '[f]'},
            'object_sound_velocity':{ 'file' : "ROI" , 'header' :'Sound_Velocity', 'index' : 12 , 'fn' : None , 'type' : '[f]'},
            'object_local_density':{ 'file' : "ROI" , 'header' :'local_density', 'index' : 13 , 'fn' : None, 'type' : '[f]'}
        }
        # merge dictionaries
        self.model = { **self.model , **ctd } 
        self.mapping = { **self.mapping , **ctdMapping }

    def printmodel(self):
        print("-= Model =-")
        for k in self.model:
            index = self.model[k]
            print( k + " -> " + str(index))

    def printmapping(self):
        print("-= Mapping =-")
        for k in self.mapping:
            s = ""
            for v in self.mapping[k]:
                s = s + v + ":" + str(self.mapping[k][v]) + ","
            print( k + " -> " + s)

    def getModel(self):
        return self.model


    def getMapping(self):
        return self.mapping
    
