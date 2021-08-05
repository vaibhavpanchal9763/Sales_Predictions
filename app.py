from flask import Flask,jsonify,request
from function import Sales_Prediction


# Creating Instance of Flask
app = Flask(__name__)


# Creating Welcome API
@app.route('/')
def Welcome():
    return jsonify({"Enter following values in sequence" : ["Item_Weight","Item_Visibility","Item_MRP","Outlet_Establishment_Year","Location"]})

# Defining Prediction API
@app.route('/Total_Sales_Prediction',methods=['GET', 'POST'])
def Total_Sales_Prediction():
    User_data                        = request.form
    Item_Weight                      = float(User_data['Item_Weight'])
    Item_Visibility                  = float(User_data['Item_Visibility']) 
    Item_MRP                         = float(User_data['Item_MRP'])
    Outlet_Establishment_Year        = float(User_data['Outlet_Establishment_Year'])
    Location                         = User_data['Location']
    Result = Sales_Prediction(Item_Weight,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Location)
    return jsonify({"Result of Total sales Prediction":Result})



if __name__ == '__main__':
    app.run()