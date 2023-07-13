
import pandas as pd

Header = [(str,str)]

class ecotaxaDataframe: pass

class ecotaxaDataframe():

    # header: Header = []
    header: pd.DataFrame = None
    data : pd.DataFrame = None

    def __init__(self, filename=None):
        if filename:
            self.filename = filename
            self.read_csv(filename)
        else: 
            self.header: pd.DataFrame()
            self.data : pd.DataFrame()

    def read_csv(self, filename):
        self.header = self.read_header(filename)
        self.data = self.read_data(filename)
    
    def read_header(self,filename) -> pd.DataFrame:
        """
        Only read the two header lines
        """
        header_rows = [0,1]
        df = pd.read_csv(filename, skiprows = lambda x: x not in header_rows, sep="\t")
        return df

    def read_data(self,filename) -> pd.DataFrame:
        """
        Read the cvs data with the header, 
        the function remove the line of type because it change the columns type to text
        """
        header_rows = [1]
        df = pd.read_csv(filename, skiprows = lambda x: x in header_rows, sep="\t")
        return df

    def concat(self) -> pd.DataFrame:
        df = pd.concat([self.header, self.data], ignore_index=True, sort=False)
        return df

    # def save_cvs(self,*args,**kwargs):
    def to_cvs(self,filename):
        df = self.concat()
        # df.to_csv( args , kwargs )
        df.to_csv( filename , index=False )

    def to_tsv(self,filename):
        df = self.concat()
        df.to_csv( filename , index=False , sep="\t")

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

    #, how="inner", on=["object_id"]
    def merge_with(self, ecodf:ecotaxaDataframe):
        self.header = pd.merge(self.header, ecodf.header, how="inner", on=["object_id"])
        self.data = pd.merge(self.data, ecodf.data, how="inner", on=["object_id"])

def merge(left: ecotaxaDataframe, right: ecotaxaDataframe, *args, **kwargs) -> ecotaxaDataframe:

    df = ecotaxaDataframe()
    df.header = pd.merge(left.header, right.header, args, kwargs)
    df.data = pd.merge(left.data, right.data, args, kwargs)

    return df

