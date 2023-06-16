# Sebastien Galvagno 

import os
from pathlib import Path
import shutil

from Project import Project
from tsv import Tsv 
#from cpicsModel import cpicsModel
from tools import create_folder, copy_to_file, add_folder
from enums import Instrument
from image_processing import get_features
import pandas as pd

# ../../aux2/20191125.aux.dat  
# 20191125.roicoords.txt 
# ../../logs/20191125.syslog.txt

class CPICsProject(Project):
    def __init__(self, message_project_creation):
        message_project_creation["instrument"] = Instrument.CPICS
        # sample_level = message_project_creation["sample_level"]
        # subsample_level = message_project_creation["subsample_level"]
        super().__init__(message_project_creation)
    
    def copy_raw_data(self):
        #TODO
        pass

    def process_project(self):
        dfs={}
        # Read ROI
        dfs["df_ROI"] = self.parse_ROIs_to_df()

        # extract objid and sample id subsample id sample/subsample

        # Read geolocation
        # TODO fill it
        #dfs["df_GPS"] = self.parse_GPS_files_to_df()
          
        # Read sysLOG
        # TODO fill it
       # dfs["df_sysLOG"] = self.parse_sysLOG_to_df()
        
        # create architectue
        #self.split_by_sample_and_subsample()
        
        # Read images features (!) handle missing or empty images and propagate to df
        # Copy images (!) handle missing or empty images and propagate to df
        errors_images, dfs["df_images"] = self.process_images(dfs["df_ROI"])
        
        # merge everythings
        df_final = self.merge_metadata(dfs, errors_images)
        
        # Save tsv
        self.save_tsv(df_final)

        # Zip folder
        self.zip_folder(self.get_zip_path(), self.get_zip_path())

    def parse_ROIs_to_df(self) :
        df = self.init_df()
        rois_path = self.rois_path()
        for path in os.scandir(rois_path):
            if path.is_file():
                filename = path.name
                df = pd.concat([self.parse_ROI_to_df(filename)], ignore_index=True)
        return df

    def parse_ROI_to_df(self, filename):
        print ("parsing : " + filename)
        df = self.init_df()
        path = self.rois_path()+filename
        mapping = self.model.mapping

        try :
            # try to read the roicoords file
            with open(path) as f:
                lines = f.readlines()
            new_rows=[]
            #fore each line
            for l in lines : 
                # avoid empty or comments lines
                if l.startswith("ROI"):
                    line_as_array = l.split(",")
                    new_row={}
                    # create row using mapping and add it to list of rows
                    for key, value in mapping.items():
                        index = value['index']
                        result = self.apply_fn(value['fn'], line_as_array[index])
                        new_row[key] = result
                    new_rows.append(new_row)
            df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
        except UnicodeDecodeError as ude :
            print(ude)
        except Exception as e:
            print(e)
        print(df)
        return df
    
    def split_by_sample_and_subsample(self) : 
        #TODO
        pass

    def parse_sysLOG_to_df(self) : 
        #TODO
        pass

    def parse_GPS_files_to_df(self) : 
        #TODO
        pass

    def process_images(self, df) : 
        # TODO
        errors_images = []
        df_images = pd.DataFrame()
        # save image in new folder
        for image_file_name in df["img_file_name"] :
            # read image
            img_path = self.get_image_raw_path(image_file_name)
            dest_path = self.get_work_dest_path()
            add_folder(dest_path)
            try :
                image_size = os.stat(img_path).st_size
                if image_size<=0 : 
                    raise Exception(image_file_name+" "+ str(image_size))
                shutil.copy2(img_path, dest_path)
                # process feature
                df_features = get_features(dest_path, image_file_name)
                df_images = pd.concat([df_images, df_features], ignore_index=True)

            except Exception as e:
                errors_images.append(image_file_name)
                #TODO remove row if no image
                print(e)

        return errors_images, df_images
    
    def add_masked_images(self, df):
        # double all lines       
        # list all unique file name
        img_file_names = df["img_file_name"]
        # for eatch of theses names
        for file in img_file_names :
            # construct new image name
            new_name = "masked_"+file
            new_image_row = df.loc[df.img_file_name == file]
            # replace the name of the imag for the masked image
            new_image_row["img_file_name"] = new_name
            new_image_row["img_rank"] = 0
            # replace the rank for the not masked image
            df.loc[df.img_file_name == file, 'img_rank'] = 1
            df = pd.concat([df,new_image_row])
        return df

    def save_tsv(self, df) : 
        dest_path = self.get_work_dest_path()
        # order cols
        # assert on type
        mapping = self.model.mapping
        mapping.update(self.model.mapping_img)
        types = {}
        for col in df.columns:
            types[col] = mapping[col]['type']

        new_row = pd.DataFrame(types, index=[0])
        
        df2 = pd.concat([new_row,df.loc[:]]).reset_index(drop=True)
        df2.to_csv(dest_path+'ecotaxa_'+self.title+'.tsv', sep="\t", index=False)

        pass

    def zip_folder(self, base_name, root_dir) :
        shutil.make_archive(base_name, 'zip', root_dir)

    def import_in_ecotaxa(self):
        #TODO
        pass
    
    def merge_metadata(self, dfs, to_remove) :
        df_ROI = dfs["df_ROI"]
        # df_GPS = dfs["df_GPS"]
        # df_sysLOG = dfs["df_sysLOG"]
        df_images = dfs["df_images"].add_prefix("object_")
        df_final = df_ROI[~ df_ROI['img_file_name'].isin(to_remove)]
        df_final = df_final.merge(df_images, left_on ='img_file_name', right_on = 'object_img_file_name')
        df_final = self.add_masked_images(df_final)
        #drop
        df_final = df_final.drop(columns=['object_img_file_name'])
        return df_final 

####################### File system #######################

    def rois_path(self):
        return  os.path.join(self.raw_data_path, "cpics/rois/ROICoord/")
    
    def get_image_raw_path(self, image_file_name) :
        file_name_obj = self.deconstruct_cpics_file_name(image_file_name)
        folder =  file_name_obj["year"]+file_name_obj["month"]+file_name_obj["day"]
        subfolder =  folder+"_"+file_name_obj['hour'] +"00"
        img_path = os.path.join(self.raw_data_path, "cpics/rois/", folder, subfolder, image_file_name)
        return img_path
    
    def get_work_dest_path(self) :
        folder_sample = "sampleid/"
        img_dest = os.path.join(self.project_path, "_work/", folder_sample)
        return img_dest
    
    def get_zip_path(self) :
        folder_sample = "sampleid"
        img_dest = os.path.join(self.project_path, "_work/", folder_sample)
        return img_dest

    def extract_sub_number(self, name):
        suf = name.split('_',1)[1]
        return suf.split(".",1)[0]
    
    def define_sub_folder(self,name):
        return name[0]+name[1]+"00"

    def define_folders(self, name):
        dateFolder = name.split('_',1)[0]
        subNumber = self.extract_sub_number(name)
        subFolder = dateFolder + "_" + self.define_sub_folder(subNumber)
        imageName = Path(self.raw_data_path) / "cpics" / "rois" / dateFolder / subFolder / name
        destFolder = Path(self.project_path)/ "_work" / dateFolder
        return { 'destFolder':destFolder, 'imageName':imageName , 'tsvName':dateFolder }

    ####################### Mapping #######################

    def apply_fn(self, fn, data):
        if fn is None: 
                return data
        cls = self
        try:
            method = getattr(cls, fn)
            return method(data)
        except AttributeError as a:
            print(a)
            raise NotImplementedError("Class `{}` does not implement `{}`".format(cls.__class__.__name__, fn))

    ####################### Inits with mapped attributs #######################

    def init_tsv(self):
        tsv = Tsv()
        mapping = self.model.mapping
        for k in mapping:
            t = mapping[k]['type'] #todo add function in model to do that
            tsv.add_feature("",k,t) # TODO: replace "" by None
        return tsv

    def init_df(self) :
        mapping = self.model.mapping
        df = pd.DataFrame(columns=[key for key in mapping])
        for key in mapping :
            df[key] =  mapping[key]['type']
        return df
    
    ####################### Callback functions of mapped attributs #######################
    def depth_min(self, depth):
        return abs(float(depth))
    
    def depth_max(self, depth):
        return abs(float(depth))

    def date(self, filename):
        dict = self.deconstruct_cpics_file_name(filename)
        return dict['year']+dict['month']+dict['day']

    def time(self, filename):
        dict = self.deconstruct_cpics_file_name(filename)
        return dict['hour']+dict['minute']+dict['second']
 
    def rank(self, filename):
        return 0

    def id(self, name):
        return name[:-4]
    
    def filename(self, filename):
        return str(filename)

    def deconstruct_cpics_file_name(self, filename):
        #returns a dictonaring with the deconstructed filename
        #20190726_121131.773.1.png
        year = filename[:4]
        month = filename[4:6]
        day  = filename[6:8]
        hour  = filename[9:11]
        minute = filename[11:13]
        second = filename[13:15]
        millisecond = filename[16:19]
        imageNumber = filename[20:-4]
        d_filename = dict([('year',year), ('month', month), ('day', day), 
                        ('hour', hour), ('minute', minute),('second', second),
                        ('millisecond', millisecond),
                        ('imageNumber', imageNumber)])
        return d_filename


