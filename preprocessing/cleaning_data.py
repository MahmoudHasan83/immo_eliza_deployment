import pandas as pd

index_data = ['Bedrooms', 'Living area (m²)',
       'How many fireplaces?', 'Terrace', 'Terrace surface (m²)',
       'Garden', 'Garden surface (m²)', 'Surface of the plot (m²)',
       'Number of frontages', 'Swimming pool', 'Basement',
       'Kitchen type scale', 'Building condition scale',
       'Type of Property_apartment', 'Type of Property_house',
       'Subtype of Property_apartment',
       'Subtype of Property_apartment block',
       'Subtype of Property_bungalow', 'Subtype of Property_castle',
       'Subtype of Property_chalet',
       'Subtype of Property_country cottage',
       'Subtype of Property_duplex',
       'Subtype of Property_exceptional property',
       'Subtype of Property_farmhouse', 'Subtype of Property_flat studio',
       'Subtype of Property_ground floor', 'Subtype of Property_house',
       'Subtype of Property_kot', 'Subtype of Property_loft',
       'Subtype of Property_manor house', 'Subtype of Property_mansion',
       'Subtype of Property_mixed use building',
       'Subtype of Property_other property',
       'Subtype of Property_penthouse',
       'Subtype of Property_service flat',
       'Subtype of Property_town house', 'Subtype of Property_triplex',
       'Subtype of Property_villa', 'Kitchen type_Hyper equipped',
       'Kitchen type_Installed', 'Kitchen type_Not installed',
       'Kitchen type_Semi equipped', 'Kitchen type_USA hyper equipped',
       'Kitchen type_USA installed', 'Kitchen type_USA semi equipped',
       'Kitchen type_USA uninstalled', 'Building condition_As new',
       'Building condition_Good', 'Building condition_Just renovated',
       'Building condition_To be done up',
       'Building condition_To renovate', 'Building condition_To restore',
       'Energy class_A', 'Energy class_A+', 'Energy class_A++',
       'Energy class_A_A+', 'Energy class_B', 'Energy class_C',
       'Energy class_C_B', 'Energy class_D', 'Energy class_D_C',
       'Energy class_E', 'Energy class_E_C', 'Energy class_E_D',
       'Energy class_F', 'Energy class_F_B', 'Energy class_G',
       'Energy class_G_A++', 'Energy class_G_C', 'Energy class_G_F',
       'Heating type_Carbon', 'Heating type_Electric',
       'Heating type_Fuel oil', 'Heating type_Gas', 'Heating type_Pellet',
       'Heating type_Solar', 'Heating type_Wood',
       'Region_Brussels capital region', 'Region_Flemish',
       'Region_Walloon']

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

def clean(data_dict: dict):
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

    return df













































































































# df_dummy = pd.read_csv('testing.csv')
# df = pd.DataFrame(columns=index_data)
# df.loc[len(df)] = 0
# print(df_dummy)
# df['Bedrooms'].iloc[0] = df_dummy['Bed_rooms'].iloc[0]
# df['Living area (m²)'].iloc[0] = df_dummy['Living_area'].iloc[0]
# df['How many fireplaces?'].iloc[0]= df_dummy['Fire_place'].iloc[0]
# df['Terrace'].iloc[0]= df_dummy['Terrace'].iloc[0]
# df['Terrace surface (m²)'].iloc[0]= df_dummy['Terrace_surface'].iloc[0]
# df['Garden'].iloc[0]= df_dummy['Garden'].iloc[0]
# df['Garden surface (m²)'].iloc[0]= df_dummy['Garden surface (m²)'].iloc[0]
# df['Surface_of_plot'].iloc[0]= df_dummy['Surface of the plot (m²)'].iloc[0]
# df['Number of frontages'].iloc[0] = df_dummy['Frontages'].iloc[0]
# df['Swimming pool'].iloc[0] = df_dummy['Swimming_pool'].iloc[0]
# df['Basement'].iloc[0] = df_dummy['Basement'].iloc[0]
# df['Number of frontages'].iloc[0] = df_dummy['Property_type'].iloc[0]


# 'Kitchen type scale', 'Building condition scale'

# match df_dummy['Property_type'].iloc[0]:
#     case "apartment":
#         df['Type of Property_apartment'].iloc[0] = 1
#     case "house":
#         df['Type of Property_house'].iloc[0] = 1


# match df_dummy['Kitchen_type'].iloc[0]:
      
#     case "USA hyper equipped":
#         df['Kitchen type_'].iloc[0] = 1

#     case "Installed":
#             df['Kitchen type_Installed'].iloc[0] = 1

#     case "Hyper equipped":
#             df['Kitchen type_Hyper equipped'].iloc[0] = 1

#     case "USA installed":
#             df['Kitchen type_USA installed'].iloc[0] = 1

#     case "Not installed":
#             df['Kitchen type_Not installed'].iloc[0] = 1

#     case "USA uninstalled":
#             df['Kitchen type_USA uninstalled'].iloc[0] = 1

#     case "Semi equipped":
#             df['Kitchen type_Semi equipped'].iloc[0] = 1

#     case "USA semi equipped":
#             df['Kitchen type_USA semi equipped'].iloc[0] = 1


    

    


    # Building_condition,
    # Property_sub_type,
    # Energy_class,
    # Heating_type,
    # Region


    # return df_dummy
