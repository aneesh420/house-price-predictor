import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, balcony, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
        
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts....Start")
    global __data_columns
    global __locations
    global __model
    with open(r"C:\Users\anees\OneDrive\Desktop\Minor Project\backend\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open(r"C:\Users\anees\OneDrive\Desktop\Minor Project\backend\banglore_home_prices_model.pickie", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts....Done")

def get_location_names():
    return __locations

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
