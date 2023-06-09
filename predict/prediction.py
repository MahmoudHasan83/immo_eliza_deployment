import pandas as pd
from joblib import dump, load

def predict(df):

    reg = load('model/Reg_model.pkl')
    y_pred = reg.predict(df)
    return round(y_pred[0],2)