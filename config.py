prediction_labels = {
    'FATAL': 1,
    'SERIOUS': 2,
    'SLIGHT INJURY': 3
}
casualty_severity_dict = {'Fatal injury': 1, 'Serious Injury': 2, 'Slight Injury': 3}

local_authority_district_dict = {
    'Missing information': -1, 'Birmingham': 300, 'Leeds': 204, 'Westminster': 1, 'Cornwall': 596, 'Lambeth': 9,
    'Bradford': 200, 'Glasgow City': 926, 'Sheffield': 215, 'Liverpool': 91, 'Barnet': 30, 'Tower Hamlets': 5,
    'Edinburgh, City of': 923, 'Southwark': 8, 'Manchester': 102, 'West Wiltshire': 635, 'Bristol, City of': 601,
    'Wandsworth': 10, 'Ealing': 27
    }

police_force_dict = {
    'Metropolitan Police': 1, 'West Midlands': 20, 'West Yorkshire': 13, 'Kent': 46, 'Thames Valley': 43, 'Hampshire': 44,
    'Sussex': 47, 'Greater Manchester': 6, 'Devon and Cornwall': 50, 'Lancashire': 4, 'Essex': 42, 'Surrey': 45,
    'Avon and Somerset': 52, 'Strathclyde': 97, 'South Yorkshire': 14, 'Northumbria': 10, 'Nottinghamshire': 31,
    'Merseyside': 5, 'Humberside': 16, 'Cheshire': 7, 'Hertfordshire': 41, 'West Mercia': 22, 'Staffordshire': 21,
    'Derbyshire': 30, 'Lincolnshire': 32, 'Leicestershire':33, 'Cambridgeshire': 35, 'South Wales': 62, 'North Yorkshire': 12,
    'Norfolk': 36, 'Lothian and Borders': 95, 'Dorset': 55, 'Suffolk': 37, 'Bedfordshire': 40, 'Wiltshire': 54,
    'Warwickshire': 23, 'Dyfed-Powys': 63, 'North Wales': 60, 'Cumbria': 3, 'Northamptonshire': 34, 'Durham': 11,
    'Gloucestershire': 53, 'Cleveland': 17, 'Gwent': 61, 'Police Scotland': 99, 'Grampian': 92, 'Tayside': 93,
    'Northern': 91, 'Central': 96, 'Fife': 94, 'City of London': 48, 'Dumfries and Galloway': 98
    }

vehicle_manoeuvre_dict = {
    'Reversing': 1, 'Parked': 2, 'Waiting to go - held up': 3, 'Slowing or stopping': 4, 'Moving off': 5, 'U-turn': 6,
    'Turning left': 7, 'Waiting to turn left': 8, 'Turning right': 9, 'Waiting to turn right': 10, 'Changing lane to left': 11,
    'Changing lane to right': 12, 'Overtaking moving vehicle - offside': 13, 'Overtaking static vehicle - offside': 14,
    'Overtaking - nearside': 15, 'Going ahead left-hand bend': 16, 'Going ahead right-hand bend': 17, 'Going ahead other': 18,
    'unknown': 99, 'Data missing': -1
}

age_band_of_casualty_dict = {
    '0 - 5' : 1, '6 - 10' : 2, '11 - 15' : 3, '16 - 20' : 4, '21 - 25': 5, '26 - 35': 6, '36 - 45': 7, '46 - 55': 8,
    '56 - 65': 9, '66 - 75': 10, 'Over 75': 11, 'data missing': -1
    }

urban_or_rural_area_dict = {
    'Urban': 1, 'Rural': 2, 'Unallocated': 3, 'Data missing': -1
}

age_band_of_driver_dict = {'Under 18' : 1, '18-30' : 2, '31-50' : 3, 'Over 51' : 4}

day_of_week_dict = {
    'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7
}

vehicle_direction_from_dict = {
    'Parked': 0, 'North': 1, 'North East': 2, 'East': 3, 'South East': 4, 'South West': 6, 'West': 7,
    'North West': 7, 'unkown': 9
}

vehicle_direction_to_dict = {
    'Parked': 0, 'North': 1, 'North East': 2, 'East': 3, 'South East': 4, 'South West': 6, 'West': 7,
    'North West': 7, 'unkown': 9
}

accident_month_dict = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9,
    'October': 10,  'November': 11, 'December': 12
}

casualty_imd_decile_dict = {
    'Most deprived 10%': 1, 'More deprived 10-20%': 2, 'More deprived 20-30%': 3, 'More deprived 30-40%' : 4,
    'More deprived 40-50%': 5, 'Less deprived 40-50%': 6, 'Less deprived 30-40%': 7, 'Less deprived 20-30%': 8,
    'Less deprived 10-20%': 9, 'Least deprived 10%': 10, 'Data missing': -1
}

first_road_class_dict = {
    'Motorway': 1, 'A(M)': 2, 'A': 3, 'B': 4, 'C': 5, 'Unclassified': 6
}

