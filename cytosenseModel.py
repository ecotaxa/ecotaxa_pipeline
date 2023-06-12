# Sebastien Galvagno  06/2023



from Template import Template


class cpicsModel(Template):

    _mapping = {
        #'object_date':{ 'file' : "ROI" , 'header' :'Date', 'index' : 1 , 'fn' : "date" , 'type' : '[t]', 'comment': 'Date'},
    }
    
    def __init__(self, pulse: Template="", listMode: Template="", info: Template=""):
        self.append(pulse.mapping)
        self.append(listMode.mapping)
        self.append(info.mapping)
        super().__init__()




# head -1 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Pulses.csv' | sed 's/;/\n/g' | sed 's/^/"object_date":{ "file" : "ROI" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}'
class pulse(Template):

    #'object_date':{ 'file' : "ROI" , 'header' :'Date', 'index' : 1 , 'fn' : "date" , 'type' : '[t]', 'comment': 'Date'},
    _mapping = {            
            "object_date":{ "file" : "ROI" , "header" :"Particle ID","index":0, "fn": None, "type":"[t]", "comment":""},
            "object_date":{ "file" : "ROI" , "header" :"FWS","index":1, "fn": None, "type":"[t]", "comment":""},
            "object_date":{ "file" : "ROI" , "header" :"SWS","index":2, "fn": None, "type":"[t]", "comment":""},
            "object_date":{ "file" : "ROI" , "header" :"FL Yellow","index":3, "fn": None, "type":"[t]", "comment":""},
            "object_date":{ "file" : "ROI" , "header" :"FL Orange","index":4, "fn": None, "type":"[t]", "comment":""},
            "object_date":{ "file" : "ROI" , "header" :"FL Red","index":5, "fn": None, "type":"[t]", "comment":""},
            'object_date':{ 'file' : "ROI" , 'header' :'Curvature','index':6, 'fn': None, 'type':'[t]', 'comment':''}
   }


# head -1 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Listmode.csv' | sed 's/;/\n/g' | sed 's/^/"object_date":{ "file" : "ROI" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}' > listnode.txt
class Listnode(Template):
    _mapping = {
        "object_date":{ "file" : "ROI" , "header" :"Particle ID","index":0, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Sample Length","index":1, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Arrival Time","index":2, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Length","index":3, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Total","index":4, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Maximum","index":5, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Average","index":6, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Inertia","index":7, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Center of gravity","index":8, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Fill factor","index":9, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Asymmetry","index":10, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Number of cells","index":11, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS First","index":12, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Last","index":13, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS Minimum","index":14, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FWS SWS covariance","index":15, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Length","index":16, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Total","index":17, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Maximum","index":18, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Average","index":19, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Inertia","index":20, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Center of gravity","index":21, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Fill factor","index":22, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Asymmetry","index":23, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Number of cells","index":24, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS First","index":25, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Last","index":26, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS Minimum","index":27, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"SWS SWS covariance","index":28, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Length","index":29, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Total","index":30, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Maximum","index":31, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Average","index":32, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Inertia","index":33, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Center of gravity","index":34, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Fill factor","index":35, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Asymmetry","index":36, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Number of cells","index":37, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow First","index":38, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Last","index":39, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow Minimum","index":40, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Yellow SWS covariance","index":41, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Length","index":42, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Total","index":43, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Maximum","index":44, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Average","index":45, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Inertia","index":46, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Center of gravity","index":47, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Fill factor","index":48, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Asymmetry","index":49, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Number of cells","index":50, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange First","index":51, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Last","index":52, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange Minimum","index":53, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Orange SWS covariance","index":54, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Length","index":55, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Total","index":56, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Maximum","index":57, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Average","index":58, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Inertia","index":59, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Center of gravity","index":60, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Fill factor","index":61, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Asymmetry","index":62, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Number of cells","index":63, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red First","index":64, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Last","index":65, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red Minimum","index":66, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"FL Red SWS covariance","index":67, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Length","index":68, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Total","index":69, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Maximum","index":70, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Average","index":71, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Inertia","index":72, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Center of gravity","index":73, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Fill factor","index":74, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Asymmetry","index":75, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Number of cells","index":76, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature First","index":77, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Last","index":78, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature Minimum","index":79, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Curvature SWS covariance","index":80, "fn": None, "type":"[t]", "comment":""},
    }

cat 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Info.txt'| sed 's/^([^:]*)/"object_date":{ "file" : "ROI" , "header" :"\1/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}' > info.txt
# head -1 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_info.txt' | sed 's/^/"object_date":{ "file" : "ROI" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}' > info.txt


sed 's/:.*//g' 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Info.txt' | sed 's/^/"object_date":{ "file" : "ROI" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}' > info.txt


class Info(Template):
   
   _mapping = {
        "object_date":{ "file" : "ROI" , "header" :"﻿Trigger level (mV)","index":0, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"CytoUSB Block size","index":1, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"
        "object_date":{ "file" : "ROI" , "header" :"Instrument","index":3, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Beam width","index":4, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Core speed","index":5, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"User Comments","index":6, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"
        "object_date":{ "file" : "ROI" , "header" :"Measurement date","index":8, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Measurement duration","index":9, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Flow rate (μL/sec)","index":10, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"
        "object_date":{ "file" : "ROI" , "header" :"Channel 1","index":12, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Channel 2","index":13, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Channel 3","index":14, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Channel 4","index":15, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"  - sensitivity level","index":16, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Channel 5","index":17, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"  - sensitivity level","index":18, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Channel 6","index":19, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"  - sensitivity level","index":20, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Channel 7","index":21, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"  - sensitivity level","index":22, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"
        "object_date":{ "file" : "ROI" , "header" :"Total number of particles","index":24, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Smart triggered number of particles","index":25, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Concentration (part/μL)","index":26, "fn": None, "type":"[t]", "comment":""},
        "object_date":{ "file" : "ROI" , "header" :"Volume (μL)","index":27, "fn": None, "type":"[t]", "comment":""},
    }