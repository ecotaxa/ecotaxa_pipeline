
import pandas as pd

Header = [(str,str)]

class ecotaxaDataframe():

    # header: Header = []
    header: pd.DataFrame = None
    data : pd.DataFrame = None

    def __init__(self, filename=None):
        if filename:
            self.filename = filename
            self.reac_csv(filename)
        else: 
            header: pd.DataFrame()
            data : pd.DataFrame()

    def reac_csv(self, filename):
        self.header = self.read_header(filename)
        self.data = self.read_data(filename)
    
    def read_header(self,filename):
        """
        Only read the two header lines
        """
        header_rows = [0,1]
        df = pd.read_csv(filename, skiprows = lambda x: x not in header_rows)
        return df

    def read_data(self,filename):
        """
        Read the cvs data with the header, 
        the function remove the line of type because it change the columns type to text
        """
        header_rows = [1]
        df = pd.read_csv(filename, skiprows = lambda x: x in header_rows)
        return df

    def save_cvs(self):
        """
        TO DO
        """
        pass

    def add_columns(self,header:Header,data:list=None):
        """
        TO DO
        """
        pass

    def add_rows(self,data:list,index:int=None):
        """
        TO DO
        """
        pass


