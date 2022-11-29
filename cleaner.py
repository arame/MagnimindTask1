import pandas as pd
import numpy as np

class CleanDS:
    def __init__(self, df_housing):
        self.df_housing = df_housing
        self.original_no_rows = len(self.df_housing)
        
    def f(self):
        print('hello world')
        
    def convert_objects_to_integers(self, column_names_to_reformat):
        # convert the sales price column from text to a nullable integer
        for name in column_names_to_reformat:
            self.df_housing[name] = self.df_housing[name].str.strip().replace('-', pd.NA).astype('Int64')
            
    def remove_unnecessary_columns(self, columns):
        self.df_housing.drop(columns, axis=1, inplace=True)
    
    def remove_duplicate_rows(self):
        no_duplicates = sum(self.df_housing.duplicated())
        self.df_housing.drop_duplicates(inplace=True)
        print(f"{no_duplicates} duplicate rows deleted")
        
    def remove_null_rows(self):
        prev_no_rows = len(self.df_housing)
        self.df_housing.dropna(inplace=True)
        curr_no_rows = len(self.df_housing)
        print(f"{prev_no_rows - curr_no_rows} null rows deleted")
        
    def remove_rows_value_zero(self, col_names):
        for col_name in col_names:
            prev_no_rows = len(self.df_housing)
            self.df_housing = self.df_housing[self.df_housing[col_name]!=0]
            new_no_rows = len(self.df_housing)
            print(f"{prev_no_rows - new_no_rows} rows were deleted where {col_name} is zero")
            
    def summary_rows_removed(self):
        curr_no_rows = len(self.df_housing)
        rows_deleted = self.original_no_rows - curr_no_rows
        percentage = (rows_deleted / self.original_no_rows) * 100
        print(f"There were originally {self.original_no_rows} rows. There are now {curr_no_rows}, a reduction of {round(percentage, 2)}%")   
        
    def make_sale_date_column_a_date(self):
        self.df_housing['SALE DATE'] = pd.to_datetime(self.df_housing['SALE DATE'])
        
    def add_new_columns(self):
        borough_names = {1:'Manhattan',2:'Bronx',3:'Brooklyn',4:'Queens',5:'Staten Island'}
        self.df_housing['BOROUGH_NAME'] = self.df_housing['BOROUGH'].map(borough_names)
        self.df_housing['SALE_PRICE_MILLIONS'] = self.df_housing['SALE PRICE'].astype(np.float64) / 1000000
        self.df_housing['SALE_MONTH']= self.df_housing['SALE DATE'].dt.month
        #create a new column for age of the unit
        self.df_housing['AGE'] = 2022 - self.df_housing['YEAR BUILT']
        
    def convert_data_type_to_categories(self, col_names):
        for col_name in col_names:
            self.df_housing[col_name] = self.df_housing[col_name].astype('category')