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
    return iris_df.drop(columns='species')

def prep_titanic(titanic_df):
    '''
    Takes the titanic dataset and returns it after doing the following:
    - drops the unnecessary, unhelpful, or duplicated columns
    - encodes the categorical columns, creates dummy variables for them, and concats them to titanic_df
    '''
    titanic_df.drop_duplicates(inplace=True)
    titanic_df = titanic_df.drop(columns= ['deck', 'age', 'embarked', 'class', 'passenger_id'])
    titanic_df['embark_town'] = titanic_df.embark_town.fillna('Southampton')
    dummy_df = pd.get_dummies(titanic_df[['sex', 'embark_town']], dummy_na = False, drop_first = [True, True])
    titanic_df = pd.concat([titanic_df, dummy_df], axis=1)
    return titanic_df.drop(columns=['sex', 'embark_town'])



