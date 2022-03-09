import pandas as pd
import numpy as np

def prep_iris(iris_df):
    '''
    This function takes in the untransofmred iris data and modifies it by:
    - dropping the species_id and measurement_id columns
    - renaming the species_name column to species
    - creating dummy variables for the species name, and concatenates them to the iris_df
    '''
    iris_df = iris_df.drop(columns=['species_id', 'measurement_id'])
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    dummy_df = pd.get_dummies(iris_df['species'], drop_first = True)
    iris_df = pd.concat([iris_df, dummy_df], axis=1)
    return iris_df #.drop(columns='species')

def prep_titanic(titanic_df):
    '''
    Takes the titanic dataset and returns it after doing the following:
    - drops the unnecessary, unhelpful, or duplicated columns
    - encodes the categorical columns, creates dummy variables for them, and concats them to titanic_df
    '''
    titanic_df.drop_duplicates(inplace=True)
    titanic_df = titanic_df.drop(columns= ['deck', 'embarked', 'class', 'passenger_id'])
    titanic_df['embark_town'] = titanic_df.embark_town.fillna('Southampton')
    dummy_df = pd.get_dummies(titanic_df[['sex', 'embark_town']], dummy_na = False, drop_first = [True, True])
    titanic_df = pd.concat([titanic_df, dummy_df], axis=1)
    return titanic_df.drop(columns=['sex', 'embark_town'])

def prep_telco(telco_df):
    '''
    Takes the telco dataset and returns it after cleaning data. 
    - drops unnecessary columns
    - modifies total_charges column to address string issue and change to proper type
    - encodes the categorical columns, creates dummy variables for them, and concats them to telco_df
    '''
    telco_df.drop_duplicates(inplace=True)
    telco_df = telco_df.drop(columns= ['customer_id', 'internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    telco_df.total_charges = telco_df.total_charges.replace(' ', np.nan).astype(float)
    dummy_df = pd.get_dummies(telco_df[['gender', 'senior_citizen', 'partner', 'dependents', 'tenure', 'phone_service', 
                                  'multiple_lines', 'online_security', 'online_backup', 'device_protection', 
                                  'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 
                                  'churn', 'internet_service_type', 'contract_type', 'payment_type']], drop_first=[True, True, True,
                                                                                                                  True, True, True,
                                                                                                                  True, True, True,
                                                                                                                  True, True, True,
                                                                                                                  True, True, True,
                                                                                                                  True, True, True])
    telco_df = pd.concat([telco_df, dummy_df], axis=1)
    telco_df = telco_df.drop(columns=['gender', 'senior_citizen', 'partner', 'dependents', 'tenure', 'phone_service', 
                                  'multiple_lines', 'online_security', 'online_backup', 'device_protection', 
                                  'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 
                                  'churn', 'internet_service_type', 'contract_type', 'payment_type'])
    # Dropping the NaN values (11 cases due to tenure < 0 and total_charges being NaN as a result)
    telco_df.dropna(inplace = True)
    return telco_df

# Example (below) of doing these prepare functions with cleaner looping
'''
def prep_telco(df):
    # drop duplicate rows, if present
    df = df.drop_duplicates()
    # drop columns:
    # *_type_id columns are simply foreign key columns that have corresponding string values
    # customer_id is a primary key that is not useful for our analysis
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])
    # encode categorical columns with dummy variables
    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
    for col in categorical_columns:
        dummy_df = pd.get_dummies(df[col],
                                  prefix=df[col].name,
                                  drop_first=True,
                                  dummy_na=False)
        df = pd.concat([df, dummy_df], axis=1)
        df = df.drop(columns=col)
    return df
'''


