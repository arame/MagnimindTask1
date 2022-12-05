import pandas as pd

# Every time this file is opened the columns must be set to the correct datatype
class OpenCleanFile:
    def __init__(self):
        file_path = "Files\\"
        dataset_name = "cleaned_nyc-rolling-sales.csv"
        path = file_path + dataset_name
        self.df_housing = pd.read_csv(path, header=0)
        #delete_columns = ['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.2', 'Unnamed: 0.3', 'Unnamed: 0.4', 'Unnamed: 0.5']
        delete_columns = ['Unnamed: 0']
        self.df_housing.drop(delete_columns, axis=1, inplace=True)
        self.df_housing['SALE DATE'] = pd.to_datetime(self.df_housing['SALE DATE'])
        self.alpha_names = [
            'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT', 'Tax Block',
            'BUILDING CLASS AT TIME OF SALE', "BOROUGH_NAME", 'TAX CLASS AT TIME OF SALE']

        for col_name in self.alpha_names:
            self.df_housing[col_name] = self.df_housing[col_name].astype('category')

        


