import numpy as np
import pandas as pd

raindata = pd.read_csv('rainfall in india 1901-2015.csv')
    # print(raindata.shape)

    # raindata.columns
    #
    # print(raindata.columns)
    # print(set(raindata['SUBDIVISION']))

valid_states_rain = raindata[(raindata['SUBDIVISION'] == 'BIHAR') | (raindata['SUBDIVISION'] == 'KERALA') | (
                raindata['SUBDIVISION'] == 'Maharashtra') | (raindata['SUBDIVISION'] == 'ARUNACHAL PRADESH') | (
                                             raindata['SUBDIVISION'] == 'TAMIL NADU') | (
                                             raindata['SUBDIVISION'] == 'JAMMU & KASHMIR') | (
                                             raindata['SUBDIVISION'] == 'UTTARAKHAND') | (
                                             raindata['SUBDIVISION'] == 'ORISSA') | (
                                             raindata['SUBDIVISION'] == 'HIMACHAL PRADESH') | (
                                             raindata['SUBDIVISION'] == 'LAKSHADWEEP') | (
                                             raindata['SUBDIVISION'] == 'PUNJAB') | (
                                             raindata['SUBDIVISION'] == 'CHHATTISGARH') | (
                                             raindata['SUBDIVISION'] == 'ANDAMAN & NICOBAR ISLANDS') | (
                                             raindata['SUBDIVISION'] == 'JHARKHAND')]
    # print(set(valid_states_rain['SUBDIVISION']))
valid_states_rain = valid_states_rain[['SUBDIVISION', 'YEAR', 'ANNUAL']]

valid_states_rain = valid_states_rain[valid_states_rain['YEAR'] > 1996]
valid_states_rain.columns = ['State', 'Year', 'Rainfall']
    # valid_states_rain

cropdata = pd.read_csv('crop_production.csv')
    # cropdata

cropdata = cropdata.rename({'State_Name': 'State'}, axis=1)

    # print(set(valid_states_rain['State']))
    # print(set(cropdata['State']))

valid_states_crop = cropdata[(cropdata['State'] == 'Bihar') | (cropdata['State'] == 'Kerala') | (
                cropdata['State'] == 'Arunachal Pradesh') | (cropdata['State'] == 'Tamil Nadu') | (
                                             cropdata['State'] == 'Jammu and Kashmir ') | (
                                             cropdata['State'] == 'Uttarakhand') | (cropdata['State'] == 'Odisha') | (
                                             cropdata['State'] == 'Himachal Pradesh') | (
                                             cropdata['State'] == 'Punjab') | (cropdata['State'] == 'Chhattisgarh') | (
                                             cropdata['State'] == 'Andaman and Nicobar Islands') | (
                                             cropdata['State'] == 'Jharkhand')]

    # print(set(valid_states_crop['State']))
    # print(set(valid_states_rain['State']))

valid_states_rain = valid_states_rain[valid_states_rain.State != 'LAKSHADWEEP']
valid_states_crop = valid_states_crop.replace('Jammu and Kashmir ', 'Jammu and Kashmir')
valid_states_rain = valid_states_rain.replace('UTTARAKHAND', 'Uttarakhand')
valid_states_rain = valid_states_rain.replace('ORISSA', 'Odisha')
valid_states_rain = valid_states_rain.replace('HIMACHAL PRADESH', 'Himachal Pradesh')
valid_states_rain = valid_states_rain.replace('JHARKHAND', 'Jharkhand')
valid_states_rain = valid_states_rain.replace('ARUNACHAL PRADESH', 'Arunachal Pradesh')
valid_states_rain = valid_states_rain.replace('TAMIL NADU', 'Tamil Nadu')
valid_states_rain = valid_states_rain.replace('CHHATTISGARH', 'Chhattisgarh')
valid_states_rain = valid_states_rain.replace('JAMMU & KASHMIR', 'Jammu and Kashmir')
valid_states_rain = valid_states_rain.replace('ANDAMAN & NICOBAR ISLANDS', 'Andaman and Nicobar Islands')
valid_states_rain = valid_states_rain.replace('BIHAR', 'Bihar')
valid_states_rain = valid_states_rain.replace('PUNJAB', 'Punjab')
valid_states_rain = valid_states_rain.replace('KERALA', 'Kerala')

    # print(set(valid_states_crop['State']))
    # print(set(valid_states_rain['State']))

Rainfall_list = [0] * 77189
valid_states_crop['Rainfall'] = Rainfall_list
    # print(valid_states_crop.head())
    # print(valid_states_rain.head())

states_set = set(valid_states_crop['State'])
year_set = set(valid_states_crop['Crop_Year'])
    # print(states_set)
    # print(year_set)

for state in states_set:
    for year in year_set:
            # print(valid_states_crop[valid_states_crop['State']==state]['Year'])
        if (year in list(valid_states_crop[valid_states_crop['State'] == state]['Crop_Year'])):
                # print(state,year)
                valid_states_crop.loc[(valid_states_crop['State'] == state) & \
                                      (valid_states_crop['Crop_Year'] == year), 'Rainfall'] = \
                    list(valid_states_rain[(valid_states_rain['State'] == state) & \
                                           (valid_states_rain['Year'] == year)]['Rainfall'])[0]

    # valid_states_crop

crop_data_alpha = valid_states_crop.dropna()
crop_data_alpha = crop_data_alpha[crop_data_alpha.Production != 0.0]

    # print(set(crop_data_alpha['Crop']))

crop_data_alpha = crop_data_alpha.drop('District_Name', axis=1)
    # crop_data_alpha = crop_data_alpha.drop('Crop_Year',axis = 1)
crop_data_alpha = crop_data_alpha.sort_values(by='Crop')
crop_data_alpha = crop_data_alpha.reset_index(drop=True)

crop_data_alpha


def crop_prediction(cropname):

    output_data = crop_data_alpha[crop_data_alpha['Crop'] == cropname]
    df = output_data[(output_data.Crop_Year > 2005)]
    print("Rainfall Required for this crop:", df['Rainfall'].mean())
    ds = output_data[(output_data.Rainfall >= df['Rainfall'].mean())]
    ds = ds['State']
    states_available = ds.drop_duplicates()
    states_available = np.array(states_available)
    print("States suitable for this crop:", states_available)
    return df['Rainfall'].mean(), states_available

def state_prediction(statename):

    required_data = crop_data_alpha[crop_data_alpha['State'] == statename]
    df = required_data[(required_data.Crop_Year > 2005)]
    print("Average Rainfall of the State:", df['Rainfall'].mean())
    ds = df['Crop']
    crop_available = ds.drop_duplicates()
    crop_available = np.array(crop_available)
    print("Crops that taken in this State:", crop_available)
    return df['Rainfall'].mean(), crop_available