import pandas as pd
import numpy as np

def clean_dataframe(path):
    df =pd.read_excel(path, sheet_name=1)
    df.drop(['Unnamed: 0'], axis=1, inplace = True)
    cols = ['Name', 'Activity_Code', 'Zip_Code', 'Province', 
    'Revenue(k)', 'EBITDA(k)', 'Net_Income(k)', 'Total_Assets(k)', 'Equity(k)', 'Employees']
    df.columns = cols
    df.dropna(axis = 0, inplace = True)
    df['Revenue(k)'] = df['Revenue(k)'].astype('int64')
    df['EBITDA(k)'] = df['EBITDA(k)'].astype('int64')
    df['Net_Income(k)'] = df['Net_Income(k)'].astype('int64')
    df['Total_Assets(k)'] = df['Total_Assets(k)'].astype('int64')
    df['Equity(k)'] = df['Equity(k)'].astype('int64')
    df['Zip_Code'] = df['Zip_Code'].astype('int64')
    df['Liabilities(k)'] = df['Total_Assets(k)'] - df['Equity(k)']
    df['Net_Income_Margin(%)'] = df['Net_Income(k)'] / df['Revenue(k)'] * 100
    df['EBITDA_Margin(%)'] = df['EBITDA(k)'] / df['Revenue(k)'] * 100
    df['Debt_Ratio(%)'] = df['Liabilities(k)'] / df['Total_Assets(k)'] * 100
    df.dropna(axis = 0, inplace = True)
    
    #Classify Activity Code with Broader Classification
    conditions = [
    (df['Activity_Code'] < 400),
    (df['Activity_Code'] > 500) & (df['Activity_Code'] < 1000),
    (df['Activity_Code'] > 1000) & (df['Activity_Code'] < 3400),
    (df['Activity_Code'] > 3500) & (df['Activity_Code'] < 3550),
    (df['Activity_Code'] > 3599) & (df['Activity_Code'] < 4000),
    (df['Activity_Code'] > 4000) & (df['Activity_Code'] < 4400),
    (df['Activity_Code'] > 4500) & (df['Activity_Code'] < 4800),
    (df['Activity_Code'] > 4900) & (df['Activity_Code'] < 5400),
    (df['Activity_Code'] > 5500) & (df['Activity_Code'] < 5700),
    (df['Activity_Code'] > 5800) & (df['Activity_Code'] < 6400),
    (df['Activity_Code'] > 6400) & (df['Activity_Code'] < 6700),
    (df['Activity_Code'] > 6800) & (df['Activity_Code'] < 6900),
    (df['Activity_Code'] > 6900) & (df['Activity_Code'] < 7600),
    (df['Activity_Code'] > 7700) & (df['Activity_Code'] < 8300),
    (df['Activity_Code'] > 8400) & (df['Activity_Code'] < 8500),
    (df['Activity_Code'] > 8500) & (df['Activity_Code'] < 8600),
    (df['Activity_Code'] > 8600) & (df['Activity_Code'] < 9000),
    (df['Activity_Code'] > 9000) & (df['Activity_Code'] < 9400),
    (df['Activity_Code'] > 9400)]
    
    values = ['Agriculture, Livestock & Fishing', 
            'Extractive Industries', 'Manufacturing', 'Energy Supply',
            'Water Supply & Waste Management', 'Construction',
            'Wholesale & Retail Trade; Repair of Vehicles',
            'Transportation & Storage', 'Hospitality',
            'Information & Communications', 'Finance & Insurance',
            'Real Estate', 'Professional, Scientific & Technical Activities',
            'Administrative & Auxiliary Activities',
            'Public Administration & Defense', 'Education',
            'Health & Social Services', 
            'Artistic, Recreational & Entertainment', 'Other Services']
        
    df['Industry'] = np.select(conditions, values)
    #Turn Activity Code into Categorical
    df['Activity_Code'] = df['Activity_Code'].astype('str')
    df['Activity_Code'] = df['Activity_Code'].str.zfill(4)

    return df


def get_ziptoregion(pathx, pathy):
    x = pd.read_csv(pathx)
    y = pd.read_csv(pathy, sep=";")
    #There is a missing value for Lleida so I add it manually
    x.loc[len(x.index)] = [1413, 25190, 251207, 'Lleida']
    x.rename(columns={'Codi municipi': 'Codi_Municipi'}, inplace = True)
    y.rename(columns={'Codi': 'Codi_Municipi'}, inplace = True)
    merged = pd.merge(x,y[['Codi_Municipi','Codi comarca','Nom comarca']],on='Codi_Municipi', how='left')
    merged_cols = ['ID', 'Zip_Code', 'Town_Code', 'Town', 'Region_Code', 'Region']
    merged.columns = merged_cols
    merged.drop_duplicates('Zip_Code', inplace = True)
    return merged

def join_zip_to_company(companydfpath, zipdfpath):
    df = pd.read_csv(companydfpath)
    zipdf = pd.read_csv(zipdfpath)
    df = pd.merge(df,zipdf[['Zip_Code','Town','Region_Code', 'Region']],on='Zip_Code', how='left')
    df.drop_duplicates('Name', inplace = True)
    df.dropna(axis = 0, inplace = True)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df['Activity_Code'] = df['Activity_Code'].astype('str').str.zfill(4)
    df['Zip_Code'] = df['Zip_Code'].astype('str').str.zfill(5)
    df['Region_Code'] = df['Region_Code'].astype('int64')
    df['Region_Code'] = df['Region_Code'].astype('str').str.zfill(2)
    
    return df
    

