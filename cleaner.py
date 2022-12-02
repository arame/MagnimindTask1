import pandas as pd
import numpy as np

class CleanDS:
    def __init__(self, df_housing):
        self.df_housing = df_housing
        self.original_no_rows = len(self.df_housing)
        self.no_rows_before_deletion = 0
        
    def print_rows_deleted(self, text):
        perc_text = self.get_percentage_text()
        print(f"{self.no_rows_before_deletion - len(self.df_housing)} rows were deleted {text}, {perc_text}")
        
    def get_percentage_text(self):
        rows_deleted = self.no_rows_before_deletion - len(self.df_housing)
        percentage = (rows_deleted / self.original_no_rows) * 100
        return f"a reduction of {round(percentage, 2)}%"
        
    def convert_objects_to_integers(self, column_names_to_reformat):
        # convert the sales price column from text to a nullable integer
        for name in column_names_to_reformat:
            self.df_housing[name] = self.df_housing[name].str.strip().replace('-', pd.NA).astype('Int64')
            
    def remove_unnecessary_columns(self, columns):
        self.df_housing.drop(columns, axis=1, inplace=True)
    
    def remove_duplicate_rows(self):
        self.no_rows_before_deletion = len(self.df_housing)
        no_duplicates = sum(self.df_housing.duplicated())
        if no_duplicates > 0:
            self.df_housing.drop_duplicates(inplace=True)
            self.print_rows_deleted("as duplicates")
        
    def remove_null_rows(self):
        self.no_rows_before_deletion = len(self.df_housing)
        self.df_housing.dropna(inplace=True)
        self.print_rows_deleted("with null values")
        
    def remove_rows_value_zero(self, col_names):
        for col_name in col_names:
            self.no_rows_before_deletion = len(self.df_housing)
            self.df_housing = self.df_housing[self.df_housing[col_name]!=0]
            self.print_rows_deleted(f"where {col_name} is zero")
            
    def remove_impossible_land_areas(self):
        self.no_rows_before_deletion = len(self.df_housing)
        self.df_housing = self.df_housing[self.df_housing['GROSS SQUARE FEET'] > self.df_housing['LAND SQUARE FEET']]
        self.print_rows_deleted(f"where the Land Square Feet is greater than the Gross Square Feet")
        
    def remove_outliers(self, col_name, lower_limit, upper_limit):
        self.no_rows_before_deletion = len(self.df_housing)
        self.df_housing = self.df_housing[self.df_housing[col_name] > lower_limit]
        self.df_housing = self.df_housing[self.df_housing[col_name] < upper_limit]
        self.print_rows_deleted(f"for {col_name} that were outside the limits of {lower_limit} to {upper_limit}")
                
    def summary_rows_removed(self):
        curr_no_rows = len(self.df_housing)
        rows_deleted = self.original_no_rows - curr_no_rows
        percentage = (rows_deleted / self.original_no_rows) * 100
        print(f"There were originally {self.original_no_rows} rows. There are now {curr_no_rows}, a reduction of {round(percentage, 2)}%")   
        
    def make_sale_date_column_a_date(self):
        self.df_housing['SALE DATE'] = pd.to_datetime(self.df_housing['SALE DATE'], format:('%Y-%m-%d'))
        #self.df_housing['SALE DATE'] = pd.to_datetime(self.df_housing['SALE DATE'])
        
    def add_new_columns(self):
        borough_names = {1:'Manhattan',2:'Bronx',3:'Brooklyn',4:'Queens',5:'Staten Island'}
        self.df_housing['BOROUGH_NAME'] = self.df_housing['BOROUGH'].map(borough_names)
        self.df_housing.drop('BOROUGH', axis=1, inplace=True)
        self.df_housing['SALE_MONTH']= self.df_housing['SALE DATE'].dt.month
        #create a new column for age of the unit
        self.df_housing['AGE'] = 2022 - self.df_housing['YEAR BUILT']
        
    def convert_data_type_to_categories(self, col_names):
        for col_name in col_names:
            self.df_housing[col_name] = self.df_housing[col_name].astype('category')
            
    def filter_less_than(self, col_name, limit):
        df_new_housing = self.df_housing[self.df_housing[col_name] < limit]
        return df_new_housing
    
    def filter_greater_than(self, col_name, limit):
        df_new_housing = self.df_housing[self.df_housing[col_name] > limit]
        return df_new_housing
    
    def filter_between(self, col_name, lower_limit, upper_limit):
        df_new_housing = self.df_housing[self.df_housing[col_name] > lower_limit]
        df_new_housing = df_new_housing[df_new_housing[col_name] < upper_limit]
        return df_new_housing