import streamlit as st
import pickle
from config import *
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# load models
model = pickle.load(open('final_pickle_rfc.pkl', 'rb'))


def get_keys(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


# creating option list for dropdown menu
options_day = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
options_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
option_casualty_severity = ['Fatal injury', 'Serious Injury', 'Slight Injury']
option_local_authority_district = [
    'Missing information', 'Birmingham', 'Leeds', 'Westminster', 'Cornwall', 'Lambeth', 'Bradford', 'Glasgow City',
    'Sheffield', 'Liverpool', 'Barnet', 'Tower Hamlets', 'Edinburgh, City of', 'Southwark', 'Manchester',
    'West Wiltshire', 'Bristol, City of', 'Wandsworth', 'Ealing']

option_urban_or_rural_area = [
    'Urban', 'Rural', 'Unallocated', 'Data missing'
]

option_vehicle_direction = [
    'Parked', 'North', 'North East', 'East', 'South East', 'South West', 'West', 'North West', 'unkown'
]

options_vehicle_manoeuvre = ['Reversing', 'Parked', 'Waiting to go - held up', 'Slowing or stopping', 'Moving off',
                             'U-turn', 'Turning left', 'Waiting to turn left', 'Turning right', 'Waiting to turn right',
                             'Changing lane to left', 'Changing lane to right', 'Overtaking moving vehicle - offside',
                             'Overtaking static vehicle - offside', 'Overtaking - nearside',
                             'Going ahead left-hand bend',
                             'Going ahead right-hand bend', 'Going ahead other', 'unknown', 'Data missing']

options_age_band_of_casualty = ['0 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 25', '26 - 35', '36 - 45', '46 - 55',
                                '56 - 65', '66 - 75', 'Over 75', 'Data missing']

option_police_force = [
    'Metropolitan Police', 'West Midlands', 'West Yorkshire', 'Kent', 'Thames Valley', 'Hampshire', 'Sussex',
    'Greater Manchester', 'Devon and Cornwall', 'Lancashire', 'Essex', 'Surrey', 'Avon and Somerset', 'Strathclyde',
    'South Yorkshire', 'Northumbria', 'Nottinghamshire', 'Merseyside', 'Humberside', 'Cheshire', 'Hertfordshire',
    'West Mercia', 'Staffordshire', 'Derbyshire', 'Lincolnshire', 'Leicestershire', 'Cambridgeshire', 'South Wales',
    'North Yorkshire', 'Norfolk', 'Lothian and Borders', 'Dorset', 'Suffolk', 'Bedfordshire', 'Wiltshire',
    'Warwickshire', 'Dyfed-Powys', 'North Wales', 'Cumbria', 'Northamptonshire', 'Durham', 'Gloucestershire',
    'Cleveland', 'Gwent', 'Police Scotland', 'Grampian', 'Tayside', 'Northern', 'Central', 'Fife', 'City of London',
    'Dumfries and Galloway'
]
options_age = ['18-30', '31-50', 'Over 51', 'Under 18']

option_casualty_imd_decile = [
    'Most deprived 10%', 'More deprived 10-20%', 'More deprived 20-30%', 'More deprived 30-40%',
    'More deprived 40-50%', 'Less deprived 40-50%', 'Less deprived 30-40%', 'Less deprived 20-30%',
    'Less deprived 10-20%', 'Least deprived 10%', 'Data missing'
]

option_first_road_class = ['Motorway', 'A(M)', 'A', 'B', 'C', 'Unclassified']

# features
features = ['police_force', 'number_of_vehicles', 'number_of_casualties', 'day_of_week', 'local_authority_district',
            'first_road_class', 'first_road_number', 'urban_or_rural_area', 'accident_month', 'hour',
            'age_band_of_casualty', 'casualty_severity', 'casualty_imd_decile', 'vehicle_manoeuvre',
            'vehicle_direction_from', 'vehicle_direction_to', 'age_band_of_driver', 'engine_capacity_cc',
            'age_of_vehicle'
            ]

st.markdown("<h1 style='text-align: center;'>Accident Severity Prediction Application 🚧</h1>", unsafe_allow_html=True)


def main():
    with st.form('prediction_form'):
        st.subheader("Enter the input for following features:")

        police_force = st.selectbox("Select Police Force in the area: ", options=option_police_force)
        number_of_vehicles = st.slider("Pickup count of vehicles involved: ", 1, 7, value=0, format="%d")
        number_of_casualties = st.slider("Count of casualties: ", 1, 8, value=0, format="%d")
        day_of_week = st.selectbox("Select day of the week: ", options=options_day)
        local_authority_district = st.selectbox("Select Local Authority District: ",
                                                options=option_local_authority_district)
        first_road_class = st.selectbox("Select First Road Class: ", options=option_first_road_class)
        first_road_number = st.slider("Pickup First Road Number: ", 1, 24, value=0, format="%d")
        urban_or_rural_area = st.selectbox("Select Urban or Rural area: ", options=option_urban_or_rural_area)
        accident_month = st.selectbox("Pickup Month the accident occurred: ", options=options_month)
        hour = st.slider("Pickup Hour of the day: ", 1, 24, value=0, format="%d")
        age_band_of_casualty = st.selectbox("Select age band of the casualty: ", options=options_age_band_of_casualty)
        casualty_severity = st.selectbox("Select casualty severtiy: ", options=option_casualty_severity)
        casualty_imd_decile = st.selectbox("Select casualty imd decile: ", options=option_casualty_imd_decile)
        vehicle_manoeuvre = st.selectbox("Select Vehicle Manoeuvre: ", options=options_vehicle_manoeuvre)
        vehicle_direction_from = st.selectbox("Select vehicle direction from: ", options=option_vehicle_direction)
        vehicle_direction_to = st.selectbox("Select vehicle direction to: ", options=option_vehicle_direction)
        age_band_of_driver = st.selectbox("Select age band of the driver: ", options=options_age)
        engine_capacity_cc = st.text_input("Engine Capacity of the vehicle: ", value="")
        age_of_vehicle = st.slider("Pickup Age of the vehicle: ", 1, 50, value=0, format="%d")

        submit = st.form_submit_button("Predict")

    if submit:
        police_force = police_force_dict[police_force]
        casualty_severity = casualty_severity_dict[casualty_severity]
        day_of_week = day_of_week_dict[day_of_week]
        local_authority_district = local_authority_district_dict[local_authority_district]
        first_road_class = first_road_class_dict[first_road_class]
        accident_month = accident_month_dict[accident_month]
        vehicle_manoeuvre = vehicle_manoeuvre_dict[vehicle_manoeuvre]
        age_band_of_casualty = age_band_of_casualty_dict[age_band_of_casualty]
        urban_or_rural_area = urban_or_rural_area_dict[urban_or_rural_area]
        age_band_of_driver = age_band_of_driver_dict[age_band_of_driver]
        vehicle_direction_to = vehicle_direction_to_dict[vehicle_direction_to]
        vehicle_direction_from = vehicle_direction_from_dict[vehicle_direction_from]
        casualty_imd_decile = casualty_imd_decile_dict[casualty_imd_decile]

        user_inp = np.array(
            [police_force, number_of_vehicles, number_of_casualties, day_of_week, local_authority_district,
             first_road_class, first_road_number, urban_or_rural_area, accident_month, hour,
             age_band_of_casualty, casualty_severity, casualty_imd_decile, vehicle_manoeuvre,
             vehicle_direction_from, vehicle_direction_to, age_band_of_driver, engine_capacity_cc,
             age_of_vehicle
             ]).reshape(1, -1)

        prediction = model.predict(user_inp)
        final_result = get_keys(prediction, prediction_labels)
        st.success('This Accident was :: {}'.format(final_result))


if __name__ == '__main__':
    main()
