import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import OneHotEncoder


def garden_terrace_fix(df):
    filter_G = df["Garden surface (m²)"] == 0
    print(filter_G)
    df.loc[~filter_G,'Garden'] = 1
    filter_T = df["Terrace surface (m²)"] == 0
    df.loc[~filter_T,'Terrace'] = 1
    return df

def add_Build_scale(df):
    building_condition_scale={'As new':6,'Just renovated':5, 'Good':4, 'To renovate':2,
    'To restore':1, 'To be done up':3}
    df['Building condition scale'] = df['Building condition'].map(building_condition_scale)

    return df

def add_kitch_scale(df):
    kitchen_type_scale={'USA hyper equipped':3, 'USA installed':2, 'USA semi equipped':1, 'USA uninstalled':0,
    'Hyper equipped':3, 'Installed':2, 'Semi equipped':1, 'Not installed':0}

    df['Kitchen type scale'] = df['Kitchen type'].map(kitchen_type_scale)
    return df

def move_region_last(df):
    Region_column = df.pop('Region')
    # insert column using insert(position,column_name,first_column) function
    df.insert(19, Region_column.name, Region_column)
    return df

def set_data_types(df):
    df = df.astype({"Living area (m²)":"float", "Terrace":"float", "Garden":"float",
        "Terrace surface (m²)":"float",
        "Garden surface (m²)":"float","Surface of the plot (m²)":"float",
        "Bedrooms":"float","How many fireplaces?":"float",
        "Subtype of Property":"object","Kitchen type":"object", 
        "Building condition":"object","Energy class":"object","Heating type":"object",
        "Number of frontages":"float","Kitchen type scale":"float",
        "Building condition scale":"float","Region":"object"})
    return df

def hot_one_encode(df):
    OH_encoder = load("preprocessing/Encoded.pkl") # load and reuse the model
    object_cols = ['Type of Property', 'Subtype of Property', 'Kitchen type',
       'Building condition', 'Energy class', 'Heating type', 'Region']
    OH_cols = pd.DataFrame(OH_encoder.transform(df[object_cols]))
    OH_cols.index = df.index
    OH_cols.columns = OH_encoder.get_feature_names_out()
    df = df.drop(object_cols, axis=1)
    df = pd.concat([df, OH_cols], axis=1)
    df = df.drop(['Kitchen type_Empty', 'Building condition_Empty', 
            'Energy class_Empty', 'Heating type_Empty'], axis=1)
    return df


def preprocess(data_dict: dict):   # def clean(data_dict: dict):
    df = pd.DataFrame.from_dict(data_dict).set_index(0).T
    df = df.rename(columns = {'Zip_code':'Zip code', 'Property_type':'Type of Property', 'Living_area':'Living area (m²)', 
                              'Bed_rooms':'Bedrooms', 'Garden':'Garden', 'Terrace':'Terrace', 'Terrace_surface':'Terrace surface (m²)', 
                        'Garden_surface':'Garden surface (m²)', 'Kitchen_type':'Kitchen type', 'Swimming_pool':'Swimming pool', 
                        'Furnished':'Furnished', 'Fire_place':'How many fireplaces?', 'Surface_of_plot': 'Surface of the plot (m²)', 
                        'facades_number':'Number of frontages', 'Building_condition': 'Building condition',
                        'Property_sub_type':'Subtype of Property',"Energy_class":"Energy class", "Heating_type":"Heating type"})


    df = add_kitch_scale(df)
    df = add_Build_scale(df)
    df = move_region_last(df)
    df = set_data_types(df)
    df = hot_one_encode(df)
    df = garden_terrace_fix(df)

    return df













































































































# # df_dummy = pd.read_csv('testing.csv')
# # df = pd.DataFrame(columns=index_data)
# # df.loc[len(df)] = 0
# # print(df_dummy)
# # df['Bedrooms'].iloc[0] = df_dummy['Bed_rooms'].iloc[0]
# # df['Living area (m²)'].iloc[0] = df_dummy['Living_area'].iloc[0]
# # df['How many fireplaces?'].iloc[0]= df_dummy['Fire_place'].iloc[0]
# # df['Terrace'].iloc[0]= df_dummy['Terrace'].iloc[0]
# # df['Terrace surface (m²)'].iloc[0]= df_dummy['Terrace_surface'].iloc[0]
# # df['Garden'].iloc[0]= df_dummy['Garden'].iloc[0]
# # df['Garden surface (m²)'].iloc[0]= df_dummy['Garden surface (m²)'].iloc[0]
# # df['Surface_of_plot'].iloc[0]= df_dummy['Surface of the plot (m²)'].iloc[0]
# # df['Number of frontages'].iloc[0] = df_dummy['Frontages'].iloc[0]
# # df['Swimming pool'].iloc[0] = df_dummy['Swimming_pool'].iloc[0]
# # df['Basement'].iloc[0] = df_dummy['Basement'].iloc[0]
# # df['Number of frontages'].iloc[0] = df_dummy['Property_type'].iloc[0]


# # 'Kitchen type scale', 'Building condition scale'

# # match df_dummy['Property_type'].iloc[0]:
# #     case "apartment":
# #         df['Type of Property_apartment'].iloc[0] = 1
# #     case "house":
# #         df['Type of Property_house'].iloc[0] = 1


# # match df_dummy['Kitchen_type'].iloc[0]:
      
# #     case "USA hyper equipped":
# #         df['Kitchen type_'].iloc[0] = 1

# #     case "Installed":
# #             df['Kitchen type_Installed'].iloc[0] = 1

# #     case "Hyper equipped":
# #             df['Kitchen type_Hyper equipped'].iloc[0] = 1

# #     case "USA installed":
# #             df['Kitchen type_USA installed'].iloc[0] = 1

# #     case "Not installed":
# #             df['Kitchen type_Not installed'].iloc[0] = 1

# #     case "USA uninstalled":
# #             df['Kitchen type_USA uninstalled'].iloc[0] = 1

# #     case "Semi equipped":
# #             df['Kitchen type_Semi equipped'].iloc[0] = 1

# #     case "USA semi equipped":
# #             df['Kitchen type_USA semi equipped'].iloc[0] = 1


    

    


#     # Building_condition,
#     # Property_sub_type,
#     # Energy_class,
#     # Heating_type,
#     # Region


#     # return df_dummy
