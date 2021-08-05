import pandas as pd
import numpy as np
import pickle

# Loading User Dataframe
user_df = pd.read_csv('Testing_Df.csv')
print(user_df)


# Gathering columns length
li_col = [i for i in user_df.columns]
print(li_col)
print(len(li_col))


# Loading Regression Model
with open('LiModel.pkl','rb') as file:
    pic_model = pickle.load(file)

# Defining Sales prediction function
def Sales_Prediction(Item_Weight,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Location):
    user_df['Item_Weight']                  = Item_Weight
    user_df['Item_Visibility']              = Item_Visibility
    user_df['Item_MRP']                     = Item_MRP
    user_df['Outlet_Establishment_Year']    = Outlet_Establishment_Year
    user_df[Location] = 1
    res = pic_model.predict(user_df)[0][0]
    user_df.loc[0] = np.zeros(len(li_col))
    return np.round(res,3)