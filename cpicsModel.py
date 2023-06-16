# Sebastien Galvagno  06/2023


# from tools import print_dict
from Template import Template


class CTD_sbe37(Template):
        
    #ROI, Date Time,Name,Position upper leftx,Position upper lefty,Position lower rightx,Position lower rightY,Temperature,Conductivity,Pressure,Depth,Salinity,Sound Velocity,local density
    _mapping = {
        'object_temperature':{ 'file' : "ROI" , 'header' :'Temperature', 'index' : 7 , 'fn' : None , 'type' : '[f]', 'comment': 'Temperature'},
        'object_conductivity':{ 'file' : "ROI" , 'header' :'Conductivity', 'index' : 8 , 'fn' : None , 'type' : '[f]', 'comment': 'Conductivity'},
        'object_pressure':{ 'file' : "ROI" , 'header' :'Pressure', 'index' : 9 , 'fn' : None , 'type' : '[f]', 'comment': 'Pressure'},
        'object_depth_min':{ 'file' : "ROI" , 'header' :'Depth min', 'index' : 10 , 'fn' : "depth_min" , 'type' : '[f]', 'comment': 'Depth_min'},
        'object_depth_max':{ 'file' : "ROI" , 'header' :'Depth max', 'index' : 10 , 'fn' : "depth_max" , 'type' : '[f]', 'comment': 'Depth_max'},
        'object_salinity':{ 'file' : "ROI" , 'header' :'Salinity', 'index' : 11 , 'fn' : None , 'type' : '[f]', 'comment': 'Salinity'},
        'object_sound_velocity':{ 'file' : "ROI" , 'header' :'Sound_Velocity', 'index' : 12 , 'fn' : None , 'type' : '[f]', 'comment': 'Sound Velocity'},
        'object_local_density':{ 'file' : "ROI" , 'header' :'local_density', 'index' : 13 , 'fn' : None, 'type' : '[f]', 'comment': 'local density'}
    }


class cpicsModel(Template):
    #ROI, Date Time,Name,Position upper leftx,Position upper lefty,Position lower rightx,Position lower rightY,Temperature,Conductivity,Pressure,Depth,Salinity,Sound Velocity,local density
    _mapping = {
        'img_file_name':{ 'file' : "ROI" , 'header' :'Name', 'index' : 2 , 'fn' : "filename" , 'type' : '[t]', 'comment': 'img_file_name'},# Name  -> img_file_name    &	object_id
        'img_rank':{ 'file' : "ROI" , 'header' :'Rank', 'index' : 2 , 'fn' : "rank" , 'type' : '[f]', 'comment': 'img_rank'},
        'object_id':{ 'file' : "ROI" , 'header' :'Name', 'index' : 2 , 'fn' : "id" , 'type' : '[t]', 'comment': 'object_id'},
        'object_date':{ 'file' : "ROI" , 'header' :'Date', 'index' : 2 , 'fn' : "date" , 'type' : '[f]', 'comment': 'Date'},
        'object_time':{ 'file' : "ROI" , 'header' :'Time', 'index' : 2 , 'fn' : "time" , 'type' : '[f]', 'comment': 'Time'},       
        'object_leftx':{ 'file' : "ROI" , 'header' :'leftx', 'index' : 3 , 'fn' : None , 'type' : '[f]', 'comment': 'Position upper leftx'},
        'object_lefty':{ 'file' : "ROI" , 'header' :'lefty', 'index' : 4 , 'fn' : None , 'type' : '[f]', 'comment': 'Position upper lefty'},
        'object_rightx':{ 'file' : "ROI" , 'header' :'rightx', 'index' : 5 , 'fn' : None , 'type' : '[f]', 'comment': 'Position lower rightx'},
        'object_righty':{ 'file' : "ROI" , 'header' :'righty', 'index' : 6 , 'fn' : None , 'type' : '[f]', 'comment': 'Position lower rightY'}
    }
    _mapping_img = {
        'object_area' :{ 'file' : "extracted" , 'header' :'area', 'index' : 0 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_area_filled' : { 'file' : "extracted" , 'header' :'area_filled', 'index' : 1 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_axis_major_length':{ 'file' : "extracted" , 'header' :'axis_major_length', 'index' : 2 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_axis_minor_length':{ 'file' : "extracted" , 'header' :'axis_minor_length', 'index' : 3 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_orientation':{ 'file' : "extracted" , 'header' :'orientation', 'index' : 4 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_eccentricity':{ 'file' : "extracted" , 'header' :'eccentricity', 'index' : 5 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_feret_diameter_max':{ 'file' : "extracted" , 'header' :'feret_diameter_max', 'index' : 6 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_centroid_local-0':{ 'file' : "extracted" , 'header' :'centroid_local-0', 'index' : 7 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_local-1':{ 'file' : "extracted" , 'header' :'centroid_local-1', 'index' : 8 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_weighted_local-0-0':{ 'file' : "extracted" , 'header' :'centroid_weighted_local-0-0', 'index' : 9 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_weighted_local-0-1':{ 'file' : "extracted" , 'header' :'centroid_weighted_local-0-1', 'index' : 10 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_weighted_local-0-2':{ 'file' : "extracted" , 'header' :'centroid_weighted_local-0-2', 'index' : 11 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_weighted_local-1-0':{ 'file' : "extracted" , 'header' :'centroid_weighted_local-1-0', 'index' : 12 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_weighted_local-1-1':{ 'file' : "extracted" , 'header' :'centroid_weighted_local-1-1', 'index' : 13 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_centroid_weighted_local-1-2':{ 'file' : "extracted" , 'header' :'centroid_weighted_local-1-2', 'index' : 14 , 'fn' : None, 'type' : '[f]', 'comment': ''},
        'object_moments_hu-0':{ 'file' : "extracted" , 'header' :'moments_hu-0', 'index' : 15 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_hu-1':{ 'file' : "extracted" , 'header' :'moments_hu-1', 'index' : 16 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_hu-2':{ 'file' : "extracted" , 'header' :'moments_hu-2', 'index' : 17 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_hu-3':{ 'file' : "extracted" , 'header' :'moments_hu-3', 'index' : 18 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_hu-4':{ 'file' : "extracted" , 'header' :'moments_hu-4', 'index' : 19 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_hu-5':{ 'file' : "extracted" , 'header' :'moments_hu-5', 'index' : 20 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_hu-6':{ 'file' : "extracted" , 'header' :'moments_hu-6', 'index' : 21 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-0-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-0-0', 'index' : 22 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-0-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-0-1', 'index' : 23 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-0-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-0-2', 'index' : 24 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-1-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-1-0', 'index' : 25 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-1-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-1-1', 'index' : 26 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-1-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-1-2', 'index' : 27 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-2-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-2-0', 'index' : 28 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-2-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-2-1', 'index' : 29 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-2-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-2-2', 'index' : 30 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-3-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-3-0', 'index' : 31 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-3-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-3-1', 'index' : 32 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-3-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-3-2', 'index' : 33 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-4-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-4-0', 'index' : 34 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-4-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-4-1', 'index' : 35 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-4-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-4-2', 'index' : 36 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-5-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-5-0', 'index' : 37 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-5-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-5-1', 'index' : 38 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-5-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-5-2', 'index' : 39 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-6-0':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-6-0', 'index' : 40 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-6-1':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-6-1', 'index' : 41 , 'fn' : None , 'type' : '[f]', 'comment': ''},
        'object_moments_weighted_hu-6-2':{ 'file' : "extracted" , 'header' :'moments_weighted_hu-6-2', 'index' : 42 , 'fn' : None , 'type' : '[f]', 'comment': ''},

    }
    
    def __init__(self, ctd: Template=""):
        map_ctd = ctd.mapping
        self.append(map_ctd)
        super().__init__()


    
