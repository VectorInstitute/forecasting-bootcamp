import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

def split_data(data, dates, num_val, num_test):
    n_samples = data.shape[0]
    num_train = n_samples - (num_val + num_test) 

    # Sample train set
    train_data = data[0:num_train, :]
    train_dates = pd.DatetimeIndex(dates.iloc[0:num_train])

    # Sample validation set
    val_data = data[num_train: num_train+num_val, :]
    val_dates = pd.DatetimeIndex(dates.iloc[num_train: num_train+num_val])

    # Sample Test Set
    test_data = data[num_train+num_val:, :]
    test_dates = pd.DatetimeIndex(dates.iloc[num_train+num_val:])

    return (train_data, train_dates), (val_data, val_dates), (test_data, test_dates)

def scale_data(data):
    scaler = StandardScaler()
    scaler.fit(data)
    scaled_data = scaler.transform(data)
    return scaled_data

def get_day_features(datetime_index):
    # Encode day of week as value between [-.5, .5]
    dow_feat = datetime_index.dayofweek / 6.0 - 0.5

    # Encode day of month as value between [-.5, .5]
    dom_feat = (datetime_index.day - 1) / 30.0 - 0.5

    # Encode day of year as value between [-.5, .5]
    doy_feat = (datetime_index.dayofyear - 1) / 365.0 - 0.5

    # Stack into time feature matrix
    time_feat = np.stack((dow_feat, dom_feat, doy_feat), axis=0).transpose(1, 0)

    return time_feat

def get_hour_features(datetime_index):
    # Encode hour of day as value between [-.5, .5]
    hod_feat =  datetime_index.hour / 23.0 - 0.5
    
    # Encode day of week as value between [-.5, .5]
    dow_feat = datetime_index.dayofweek / 6.0 - 0.
    
    # Encode day of month as value between [-.5, .5]
    dom_feat = (datetime_index.day - 1) / 30.0 - 0.5
    
    # Encode day of year as value between [-.5, .5]
    doy_feat = (datetime_index.dayofyear - 1) / 365.0 - 0.5
    
    # Stack into time feature matrix
    time_feat = np.stack((hod_feat, dow_feat, dom_feat, doy_feat), axis=0).transpose(1, 0)
    
    return time_feat